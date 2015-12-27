from flask import Flask, render_template, Markup, abort
import pypandoc
from ituHelpers import *

DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'password'

app = Flask(__name__)
app.config.from_object(__name__)

site_content = SiteGenerator('mdcontent').content_tree


@app.route('/')
@app.route('/home')
def show_index():
    try:
        markdn = Markup(site_content['home'].html.decode("utf8"))
    except Exception:
        abort(404)
    return render_template('index.html', curm="home", curpg="home", markdn=markdn, menus=site_content)


@app.route('/<menu>/<page>/')
def show_page(menu, page):
    try:
        markdn = Markup(site_content[menu.lower()][page.lower()].html.decode("utf8"))
    except:
        abort(404)
    return render_template('index.html', curm=menu.lower(), curpg=page.lower(), markdn=markdn, menus=site_content)

if __name__ == '__main__':
    app.run()
