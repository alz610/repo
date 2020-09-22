#!/bin/bash

set -o xtrace

jupyter labextension install \
@jupyter-widgets/jupyterlab-manager \
dask-labextension \
@bokeh/jupyter_bokeh \
jupyterlab-drawio \
@ryantam626/jupyterlab_code_formatter \
@krassowski/jupyterlab_go_to_definition \
@aquirdturtle/collapsible_headings \
@jupyterlab/toc \
@krassowski/jupyterlab-lsp \
@jupyterlab/mathjax3-extension \
@jupyterlab/katex-extension \
@oriolmirosa/jupyterlab_materialdarker \
@lckr/jupyterlab_variableinspector \
@ijmbarr/jupyterlab_spellchecker \
jupyterlab-plotly \
plotlywidget #\
# --no-build

# jupyter lab build

jupyter serverextension enable dask_labextension
jupyter serverextension enable --py jupyterlab_code_formatter

set +o xtrace
