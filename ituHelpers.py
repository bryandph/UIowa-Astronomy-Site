import os
from fnmatch import fnmatch


def rake_md_content():
    root = "mdcontent"
    pattern = "*.md"
    pages = {}
    menus = []

    for path, subdirs, files in os.walk(root):
        menus = menus + subdirs
    menus = [m.lower() for m in menus]

    for menu in menus:
        for path, subdirs, files in os.walk((root + "/" + menu)):
            pages[menu] = [f for f in files if fnmatch(f, pattern)]

    return pages, menus
