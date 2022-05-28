Configuration
=============

Running ``sphinx-quickstart`` from the command-line initializes documentation.
This populates the directory structure, in particular writing the
:file:`conf.py` and :file:`index.rst` files.

The answers to the questions from ``sphinx-quickstart`` are added to these
files, so you can always change things there. The only thing that is not easily
adjustable is the separation of build and source directories; if you want to
change that then it's easier to start over in an empty directory and run
``sphinx-quickstart`` again.

Adding pages
------------

The ``.. toctree::`` directive creates a table of contents. Add pages to this
directive, as relative paths without the ``.rst`` suffix, to include them in the
built documentation. Compare the home page of these docs with the `index.rst
source code
<https://raw.githubusercontent.com/NICHD-BSPC/documentation-template/main/doc/source/index.rst>`_
to see it in action.


.. warning::

    When adding pages to the ``.. toctree::`` directive; pay attention to the
    indentation of the auto-generated index.rst file. If your editor is set up
    for 4 spaces = 1 tab, then building the docs might complain that pages are
    missing, because that extra space is interpreted to be *the first character
    of the filename*. That is:

    .. code-block::

        .. toctree::
           :maxdepth: 2   # option to only go 2 headings deep
        ^^^
        Only three spaces in the default-generated index.rst.


           # paths to ReST files should be the same
           # indentation as the options
           rst_file1
           path/to/rst_file2

In this documentation, if you look at the source, you won't see anything
referring to the API docs even though there's an entry in the built
documentation. That's because that entry is automatically added by the
``sphinx-autoapi`` extension.

Extensions
----------

Extensions are added the the :file:`conf.py` file, as strings in the
``extensions`` list. The extension you're using will tell you what to add
there. For example, here we're using the ``sphinx-autoapi`` extension.
Extensions are often configured in :file:`conf.py`, as is the case here for the
``sphinx-autoapi`` extension, by adding extra variables in :file:`conf.py`.

.. seealso::

    The Sphinx `extension section
    <https://www.sphinx-doc.org/en/master/usage/extensions/index.html>`_ shows
    lots of built-in extensions as well as links to third-party extensions.
    There's also information on how to `build your own
    <https://www.sphinx-doc.org/en/master/extdev/index.html#dev-extensions>`_.

In some cases you may need to modify your ``sys.path`` to let Sphinx find
extensions or source code. If you're documenting code that's going to be tested,
it needs to be importable by Sphinx, which means adding it to the path in
:file:`conf.py`:

.. code-block:: python

    # This is in conf.py
    import os
    import sys
    sys.path.insert(0, os.path.abspath('../../src'))

Here are some useful extensions that come with Sphinx, but that need to be
explicity added to :file:`conf.py`:

- The `napolean
  <https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html>`_
  extension lets you document your Python with NumPy-style docstrings.

- The `doctest
  <https://www.sphinx-doc.org/en/master/usage/extensions/doctest.html>`_
  extension enables writing and running doctests in your Sphinx documentation.
  See :ref:`doctests` elsewhere in these docs for more advice..

- The `viewcode
  <https://www.sphinx-doc.org/en/master/usage/extensions/viewcode.html>`_
  extension, which will link directly to the source code of documented Python
  objects.

- If you install (with conda or pip) the `sphinx-autoapi
  <https://sphinx-autoapi.readthedocs.io/en/latest/>`_ package, as is done here,
  you can automatically document Python, Go, JavaScript, and .NET. This is
  different (and more convenient) than using the Sphinx-included ``autodoc``
  extension, which can be a bit finicky to use.

Themes
------

See the `Alabaster theme docs
<https://alabaster.readthedocs.io/en/latest/customization.html>`_ for
customization specific to this default theme.

For more themes, see Sphinx's `built-in themes
<https://www.sphinx-doc.org/en/master/usage/theming.html>`_ or the full `Sphinx
theme gallery <https://sphinx-themes.org/>`_.

You can customize CSS; for example see the relevant `Alabaster docs
<https://alabaster.readthedocs.io/en/latest/customization.html#custom-stylesheet>`_.
