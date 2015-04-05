#!/bin/bash

wget \
    --mirror \
    --convert-links \
    --adjust-extension \
    --page-requisites \
    --no-parent \
    --content-on-error \
    http://127.0.0.1:5000/

sed \
    -i \
    "s,examples/ex11,examples/ex11.txt,g" \
    "127.0.0.1:5000/index.html"

mv \
    "127.0.0.1:5000/examples/ex11" \
    "127.0.0.1:5000/examples/ex11.txt"

github-pages-publish \
    --verbose \
    --cname pybr9.rafaelmartins.eng.br \
    . "127.0.0.1:5000"

rm -rf "127.0.0.1:5000"
