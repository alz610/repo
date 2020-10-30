#!/bin/bash

set -o xtrace

jupyter labextension install \
@jupyter-widgets/jupyterlab-manager \
dask-labextension \
@aquirdturtle/collapsible_headings \
@jupyterlab/toc \
@krassowski/jupyterlab-lsp \
@jupyterlab/mathjax3-extension \
@oriolmirosa/jupyterlab_materialdarker

jupyter serverextension enable dask_labextension

set +o xtrace
