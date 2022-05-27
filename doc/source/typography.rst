Formatting examples
===================

In all cases, click the "Page Source" link in the footer to inspect the source
code that generates the content here.

- :file:`filename` role for filenames
- :kbd:`key` keyboard role
- :term:`term` role for terms
- :guilabel:`guilabel` for indicating GUI elements to interact with
- :class:`example_package.example.Demo` to refer to a documented class
- :func:`example_package.example.super_complex_operation` to refer to
  a documented function
- :meth:`example_package.example.Demo.run` to refer to a documented method

.. currentmodule:: example_package.example

- :func:`super_complex_operation`, after setting ``.. currentmodule::
  example_package.example``


.. code-block:: python

    # Example of syntax highlighting for Python
    import this
    for i in range(len(x)):
        print(x)
        if i > 10:
            raise ValueError('too high!')

.. code-block:: bash

    # Some bash
    export PATH="$PATH:/opt/bin"
    $(echo "ls") /opt/bin &> log
