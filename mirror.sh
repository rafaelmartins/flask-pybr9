#!/bin/bash

wget \
    --mirror \
    --convert-links \
    --adjust-extension \
    --page-requisites \
    --no-parent \
    http://127.0.0.1:5000/

github-pages-publish \
    --verbose \
    --cname pybr9.rafaelmartins.eng.br \
    . "127.0.0.1:5000"

rm -rf "127.0.0.1:5000"
