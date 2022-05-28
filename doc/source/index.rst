.. Documentation template documentation master file, created by
   sphinx-quickstart on Thu May 19 10:39:23 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Setting up Sphinx documentation
===============================

This page illustrates how to set up Sphinx with automatic API documentation for
your Python code and host it on GitHub Pages.

.. This is a ReST comment which will not be rendered.


Initial setup
~~~~~~~~~~~~~

Here is how this repo, and the hosted pages, were set up:


.. code-block:: bash

    conda create -p ./env --file requirements.txt
    conda activate ./env
    mkdir doc
    cd doc
    sphinx-quickstart

    # "y" to separate source and build directories
    # Entered author and project title
    # Otherwise used defaults

Edit :file:`doc/source/conf.py` to add extensions, e.g.:

.. code-block:: python

    extensions = [
        'autoapi.extension', # Automatically display docstrings; needs sphinx-autoapi installed
        'sphinx.ext.doctest', # Built-in extension. Write doctests in your sphinx docs
        'sphinx.ext.napoleon', # Built-in extension. Use if you like NumPy style docstrings
    ]


If you're documenting code that's going to be tested, it needs to be importable
by Sphinx, which means adding it to the path in :file:`conf.py`:

.. code-block:: python

    import os
    import sys
    sys.path.insert(0, os.path.abspath('../../src'))

If you're going to be hosting code on GitHub Pages, create a new ``gh-pages``
branch, push it, and get back to main. The ``gh-pages`` branch needs to exist
for the GitHub Actions to work.

.. code-block:: bash

    git checkout -b gh-pages
    git push origin gh-pages
    git checkout main

You'll also want to copy the :file:`.github/workflows/main.yml` file to use as a template.

Next steps
~~~~~~~~~~

Take a look around these docs. Click the "Page source" link in the footer of
the page to see the ReStructured Text input used to generate this page or any
other pages in these docs.

When adding pages to the table of contents (the ``.. toctree::`` directive; see
the source of this page), pay attention to the indentation of the
auto-generated index.rst file. That is:

.. code-block::

    .. toctree::
       :maxdepth: 2
    ^^^
    Only three spaces in the default-generated index.rst.

The ``.. toctree::`` directive creates a table of contents. Options to
directives take the form of ``:optionname: value``, and are indented under the
``.. directive::`` line. Take a peek at the source code to see it in action.
Below the options are names of ``.rst`` files -- but without the ``.rst``
extension.

Here is the table of contents. If you look at the source, you won't see
anything referring to the API docs. That's because that entry is automatically
added by the ``sphinx-autoapi`` extension.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   configuration
   typography
   doctests
   github_setup


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
