Configuration
=============

After installing Sphinx, run ``sphinx-quickstart`` from the command-line to
initialize documentation. This populates the directory structure, in particular
writing the :file:`conf.py` and :file:`index.rst` files.

Extensions are added the the :file:`conf.py` file, as strings in the
``extensions`` list. The extension you're using will tell you what to add
there. For example, here we're using the ``sphinx-autoapi`` extension.
Extensions are often configured in :file:`conf.py`, as is the case here for the
``sphinx-autoapi`` extension.

In some cases you may need to modify your ``sys.path`` to let Sphinx find
extensions or source code.

The answers to the questions from ``sphinx-quickstart`` are added to
:file:`conf.py` and :file:`index.rst`, so you can always change things there.

Shpinx comes with the `napolean
<https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html>`_
extension so you can easily document your Python with NumPy-style docstrings.

If you install (with conda or pip) the `sphinx-autoapi
<https://sphinx-autoapi.readthedocs.io/en/latest/>`_ package, as is done here,
you can automatically document Python, Go, JavaScript, and .NET. This is
different (and more convenient) than using the Sphinx-included ``autodoc``
extension, which can be a bit finicky to use.

See the `Alabaster theme docs
<https://alabaster.readthedocs.io/en/latest/customization.html>`_ for
customization specific to this default theme

For more themes, see Sphinx's `built-in themes
<https://www.sphinx-doc.org/en/master/usage/theming.html>`_ or the full `Sphinx
theme gallery <https://sphinx-themes.org/>`_.

You can customize CSS; for example see the relevant `Alabaster docs
<https://alabaster.readthedocs.io/en/latest/customization.html#custom-stylesheet>`_.
