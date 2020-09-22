conda install memory_profiler

conda install -c conda-forge dask-labextension
jupyter labextension install dask-labextension --no-build
jupyter serverextension enable dask_labextension

conda install -c bokeh jupyter_bokeh
jupyter labextension install @jupyter-widgets/jupyterlab-manager --no-build
jupyter labextension install @bokeh/jupyter_bokeh --no-build

conda install -c conda-forge ipywidgets

conda install -c conda-forge ipympl
jupyter labextension install @jupyter-widgets/jupyterlab-manager --no-build

jupyter labextension install jupyterlab-drawio --no-build

jupyter labextension install @ryantam626/jupyterlab_code_formatter --no-build
conda install -c conda-forge jupyterlab_code_formatter
jupyter serverextension enable --py jupyterlab_code_formatter
conda install black isort

jupyter labextension install @krassowski/jupyterlab_go_to_definition --no-build  # JuupyterLab 2.x

jupyter labextension install @aquirdturtle/collapsible_headings --no-build

jupyter labextension install @jupyterlab/toc

# pip install jupyter-lsp
# jupyter labextension install @krassowski/jupyterlab-lsp --no-build  # for JupyterLab 2.x
# conda install -c conda-forge python-language-server

jupyter labextension install @jupyterlab/mathjax3-extension --no-build

jupyter labextension install @jupyterlab/katex-extension --no-build

jupyter labextension install @oriolmirosa/jupyterlab_materialdarker --no-build

jupyter lab build
