#!/bin/bash

set -o xtrace

jupyter labextension install @jupyter-widgets/jupyterlab-manager --no-build


conda install memory_profiler -y
conda install jupyterthemes -y

conda install -c conda-forge dask-labextension -y
jupyter labextension install dask-labextension --no-build
jupyter serverextension enable dask_labextension

# conda install -c bokeh jupyter_bokeh -y
# jupyter labextension install @bokeh/jupyter_bokeh --no-build

conda install -c conda-forge ipywidgets -y

conda install -c conda-forge ipympl -y

jupyter labextension install jupyterlab-drawio --no-build

jupyter labextension install @ryantam626/jupyterlab_code_formatter --no-build
conda install -c conda-forge jupyterlab_code_formatter -y
jupyter serverextension enable --py jupyterlab_code_formatter
conda install black isort -y

jupyter labextension install @krassowski/jupyterlab_go_to_definition --no-build  # JuupyterLab 2.x

jupyter labextension install @aquirdturtle/collapsible_headings --no-build

jupyter labextension install @jupyterlab/toc --no-build

pip install jupyter-lsp
jupyter labextension install @krassowski/jupyterlab-lsp --no-build  # for JupyterLab 2.x
conda install -c conda-forge python-language-server -y

jupyter labextension install @jupyterlab/mathjax3-extension --no-build

jupyter labextension install @jupyterlab/katex-extension --no-build

jupyter labextension install @oriolmirosa/jupyterlab_materialdarker --no-build

jupyter labextension install @lckr/jupyterlab_variableinspector --no-build

conda install -c conda-forge ipysheet -y
jupyter labextension install ipysheet --no-build

conda install -c conda-forge -c plotly jupyter-dash -y


jupyter lab build

set +o xtrace
