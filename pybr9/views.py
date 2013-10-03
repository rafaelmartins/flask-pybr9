from flask import Blueprint, make_response, render_template
from pygments.formatters import HtmlFormatter

views = Blueprint('views', __name__)


@views.route('/')
def main():
    return render_template('slides.html',
                           stylesheet='themes/style/web-2.0-full.css')


@views.route('/low/')
def low():
    return render_template('slides.html',
                           stylesheet='themes/style/web-2.0-low.css')


@views.route('/pygments.css')
def pygments_css():
    formatter = HtmlFormatter(style='friendly')
    response = make_response(formatter.get_style_defs())
    response.headers['Content-Type'] = 'text/css'
    return response
