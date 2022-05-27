Initial setup
=============

.. code-block:: bash

    conda create -p ./env --file requirements.txt
    conda activate ./env
    mkdir doc
    cd doc
    sphinx-quickstart

    # "y" to separate source and build directories
    # Entered author and project title
    # Otherwise used defaults

Edit `doc/source/conf.py` to add extensions, e.g.:

.. code-block:: python

    extensions = [
        'sphinx.ext.autodoc',
        'sphinx.ext.autosummary',
        'sphinx.ext.doctest',
        'sphinx.ext.napoleon',
    ]

If you're documenting code, it needs to be importable by Sphinx, which means
adding it to the path in :file:`conf.py`:

.. code-block:: python

    import os
    import sys
    sys.path.insert(0, os.path.abspath('../../src'))

Create a new ``gh-pages`` branch, push it, and get back to main:

.. code-block:: bash

    git checkout -b gh-pages
    git push origin gh-pages
    git checkout main
