.. Documentation template documentation master file, created by
   sphinx-quickstart on Thu May 19 10:39:23 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Setting up Sphinx documentation
===============================

This page illustrates how to set up `Sphinx <sphinx-doc.org/>`_ with automatic
API documentation for your Python code and host it on GitHub Pages.

The corresponding repository is
https://github.com/nichd-bspc/documentation-template. It has an example Python
module along with the source for this documentation.

.. Hi, welcome to the ReST source! This is a ReST comment which will not be rendered.

Initial setup
-------------

This section describes how to initially set up your documentation.

Dependencies
~~~~~~~~~~~~

First, create an environment with dependencies. Here we happen to be using
`conda <https://docs.conda.io/en/latest/>`_ but pip, venv, apt, homebrew are
other options.

For reference, here are the contents of :file:`requirements.txt` from the repo:

.. literalinclude:: ../../requirements.txt

To use this file:

.. code-block:: bash

    conda create -p ./env --file requirements.txt
    conda activate ./env


Run ``sphinx-quickstart``
~~~~~~~~~~~~~~~~~~~~~~~~~

Since this template is intended to illustrate documentation living alongside
a Python package, we create a :file:`doc` subdirectory and run
``sphinx-quickstart`` from there to set up the directory structure.

We also assume that the Python module is living next to :file:`doc`, in
a :file:`src` directory. Check the `repo
<https://github.com/nichd-bspc/documentation-template>`_ to see how this was
set up.

.. code-block:: bash

    mkdir doc
    cd doc
    sphinx-quickstart

    # "y" to separate source and build directories
    # Entered author and project title
    # Otherwise used defaults

This will set up the directory structure. the contents of :file:`doc` should look like this::

    ├── build           # Built html will eventually go here
    ├── make.bat        # Used for windows
    ├── Makefile        # Main makefile to use
    └── source          # ReST source and config go here
        ├── conf.py     # Default config file, ready to edit
        ├── index.rst   # Default index file, ready to edit
        ├── _static     # Empty for now, CSS can go here
        └── _templates  # used for themes and templates (advanced)

Build docs
~~~~~~~~~~

In the :file:`doc` directory, you should now be able to run:

.. code-block:: bash

    make html

At the end you'll get a message, *The HTML pages are in build/html*. Open
:file:`build/html/index.html` in a web browser to see the docs.

From here on out it's a matter of tweaking configuration and actually writing
the documentation.



Next steps
~~~~~~~~~~

Take a look around these docs. Click the "Page source" link in the footer of
the page to see the ReStructured Text input used to generate this page or any
other pages in these docs.



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
