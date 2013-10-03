from flask import Flask, current_app
from jinja2 import Markup
from importlib import import_module
from inspect import getsource
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name, TextLexer
from werkzeug.wsgi import DispatcherMiddleware
import os


def highlight_object(obj, language=None):
    try:
        lexer = get_lexer_by_name(language or 'python')
    except ValueError:
        lexer = TextLexer()
    source = getsource(obj)
    formatter = HtmlFormatter(noclasses=False)
    return Markup(highlight(source, lexer, formatter))


def highlight_example(name, obj_name=None, language=None):
    obj = current_app.examples.get(name)
    if obj is None:
        raise RuntimeError('Example not found: %s' % name)
    if obj_name is not None:
        for piece in obj_name.split('.'):
            try:
                obj = getattr(obj, piece)
            except AttributeError:
                raise RuntimeError('Object not found: %s' % obj_name)
    return highlight_object(obj, language)


def load_examples(flask_app):
    # this is a wsgi middleware that makes our main flask app run the examples.
    cwd = os.path.dirname(os.path.abspath(__file__))
    examples_dir = os.path.join(cwd, 'examples')
    apps = {}
    flask_app.examples = {}
    for import_name in set(os.path.splitext(i)[0]
                           for i in os.listdir(examples_dir)
                           if not i.startswith('__init__.py')):
        try:
            mod = import_module('pybr9.examples.%s' % import_name)
        except ImportError:
            continue
        app = getattr(mod, 'app', None)
        app = getattr(mod, 'application', app)  # mod_wsgi default
        if app is None:  # let's try to load from a factory.
            factory = getattr(mod, 'create_app')
            if factory is None:
                continue
            app = factory()
        if not isinstance(app, Flask):
            continue
        # transfer global settings to the example app
        app.config.update(flask_app.config)
        # disable debug for the example app
        app.debug = False
        apps['/examples/%s' % import_name] = app
        # bind the example to the main flask, so we can reuse it later.
        # we can't use 'g' here because we are outside of app context, and if
        # we create a context here, it isn't going to be reused by the real
        # browser requests :(
        flask_app.examples[import_name] = mod

    # register a build-only url rule, so we can use url_for :)
    flask_app.add_url_rule('/examples/<example>', endpoint='examples',
                           build_only=True)
    flask_app.wsgi_app = DispatcherMiddleware(flask_app.wsgi_app, apps)
