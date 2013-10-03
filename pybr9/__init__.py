# -*- coding: utf-8 -*-

from flask import Flask

from pybr9.utils import highlight_example, load_examples
from pybr9.views import views


def create_app(config_file=None):
    app = Flask(__name__)

    app.config['TITLE'] = u'Construindo aplicações de grande porte com o Flask'

    if config_file is not None:
        app.config.from_pyfile(config_file)

    @app.context_processor
    def context_processor():
        return {'title': app.config['TITLE'],
                'highlight_example': highlight_example}

    app.register_blueprint(views)
    load_examples(app)
    return app
