from flask import Flask, render_template, Markup, abort
import pypandoc
from ituHelpers import *

DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'password'

app = Flask(__name__)
app.config.from_object(__name__)

# os.chdir("/Users/bryan/Desktop/markdownApp")
mdcontentroot = "mdcontent/"
pages, menus = rake_md_content()


@app.route('/')
def show_index():
    with open(mdcontentroot + "index.md", "r") as md:
        markdn = Markup(pypandoc.convert(md.read(), 'html5', format='md', extra_args=[
                        "--mathjax"]))
    return render_template('index.html', current="home", markdn=markdn, menus=menus, pages=pages)


@app.route('/<menu>/<page>/')
def show_page(menu, page):
    menu, page = str(menu), str(page)
    if menu not in menus:
        abort(404)
    else:
        if (page + ".md") in pages[menu]:
            with open(mdcontentroot + menu + "/" + page + ".md", "r") as md:
                markdn = Markup(pypandoc.convert(
                    md.read(), 'html5', format='md', extra_args=["--mathjax"]))
        else:
            abort(404)
    return render_template('index.html', current=menu, markdn=markdn, menus=menus, pages=pages)

if __name__ == '__main__':
    app.run()
