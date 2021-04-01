#!/bin/bash

set -o xtrace

jupyter labextension install \
@jupyter-widgets/jupyterlab-manager \
@aquirdturtle/collapsible_headings \
@jupyterlab/toc \
@jupyterlab/mathjax3-extension \
@oriolmirosa/jupyterlab_materialdarker # \
# dask-labextension \
#@krassowski/jupyterlab-lsp

# jupyter serverextension enable dask_labextension

set +o xtrace
