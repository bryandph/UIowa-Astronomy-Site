import os
import re
import pypandoc
from fnmatch import fnmatch
from bs4 import BeautifulSoup


class dirlevel:

    def __init__(self, path):
        self.path = path
        self.displayname = os.path.basename(path)
        self.htmlname = os.path.basename(path).lower()
        self.dirs = {}
        self.pages = {}

    def __getitem__(self, index):
        if index in self.dirs:
            return self.dirs[index]
        elif index in self.pages:
            return self.pages[index]
        else:
            return None

    def mkeys(self):
        return self.dirs.keys()

    def pgkeys(self):
        return self.pages.keys()


class pagelevel:

    def __init__(self, path):
        self.path = path
        self.filename = os.path.basename(self.path)
        self.displayname = self.filename.split('.')[0]
        self.htmlname = re.sub(r'[^a-zA-Z0-9 ]', r'',
                               self.displayname).replace(' ', '').lower()
        self.html = ''
        self.gen_html()

    def gen_html(self):
        html_corrections = {'figure': ('class', 'figure'), 'img': (
            'class', 'figure-img img-responsive img-rounded center-block'), 'figcaption': ('class', 'figure-caption')}

        with open(self.path, "r") as md:
            self.html = pypandoc.convert(
                md.read(), 'html5', format='md', extra_args=["--mathjax"])

        soup = BeautifulSoup(self.html, 'html.parser')

        for correction in html_corrections.keys():
            tag = correction
            arrt, val = html_corrections[correction]
            for inst in soup.findAll(tag):
                inst[arrt] = val

        self.html = str(soup)


class SiteGenerator:

    def __init__(self, contentroot=r"mdcontent"):
        self.content_root = contentroot
        self.content_tree = dirlevel(self.content_root)
        self.gather_content(self.content_tree)

    def gather_content(self, pdirlevel):
        """
        Recursive function that walks a directory and returns a tree as
        a dictionary.
        """

        for item in sorted(os.listdir(pdirlevel.path)):
            if not item.startswith("."):
                item_path = os.path.join(pdirlevel.path, item)
                if os.path.isdir(item_path):
                    newdir = dirlevel(item_path)
                    pdirlevel.dirs.update(
                        {newdir.htmlname: self.gather_content(newdir)})
                else:
                    newpg = pagelevel(item_path)
                    pdirlevel.pages.update({newpg.htmlname: newpg})
        return pdirlevel
