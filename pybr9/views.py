from flask import Blueprint, make_response, render_template
from pygments.formatters import HtmlFormatter

views = Blueprint('views', __name__)


@views.route('/')
def main():
    return render_template('slides.html')


@views.route('/pygments.css')
def pygments_css():
    formatter = HtmlFormatter(style='friendly')
    response = make_response(formatter.get_style_defs())
    response.headers['Content-Type'] = 'text/css'
    return response
