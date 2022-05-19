# Initial setup

```bash
conda create -p ./env --file requirements.txt
conda activate ./env
mkdir doc
cd doc
sphinx-quickstart

# "y" to separate source and build directories
# Entered author and project title
# Otherwise used defaults
```

Edit `doc/source/conf.py` to add extensions, e.g.:

```python
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.napoleon',
]
```

Create a new gh-pages branch, push it, and get back to main:

```bash
git checkout -b gh-pages
git push origin gh-pages
git checkout main
```
