.. Documentation template documentation master file, created by
   sphinx-quickstart on Thu May 19 10:39:23 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Documentation template
======================

This page illustrates how to set up Sphinx with automatic API documentation for
your Python code and host it on GitHub Pages.

.. This is a ReST comment which will not be rendered.

Click the "Page source" link in the footer of the page to see the ReStructured
Text input used to generate this page or any other pages in these docs.


.. warning::

    Pay attention to the indentation of the auto-generated index.rst file.

    .. code-block::

        .. toctree::
           :maxdepth: 2
        ^^^
        only three spaces in the default-generated index.rst 

The ``.. toctree::`` directive creates a table of contents. Options to
directives take the form of ``:optionname: value``, and are indented under the
``.. directive::`` line. Take a peek at the source code to see it in action.
Below the options are names of ``.rst`` files -- but without the ``.rst``
extension.

Here is the table of contents:


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   configuration


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
