from flask import Flask, render_template, Blueprint, abort
from jinja2 import TemplateNotFound

simple_page = Blueprint('simple_page', __name__,template_folder='templates')

@simple_page.route('/', defaults={'page': 'index'})
@simple_page.route('/<page>')
def show(page):
    print page
    try:
        return render_template('%s.html' % page)
    except TemplateNotFound:
        abort(404)

# admin_page = Blueprint('admin_page',__name__, static_folder='flaskr/static/admin', static_url_path='/static_admin', template_folder='flaskr/template',url_prefix='/admin')
#
# @admin_page.route('/member')
# def member():
#     pass