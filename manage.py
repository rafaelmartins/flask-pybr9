#!/usr/bin/env python

from pybr9 import create_app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
