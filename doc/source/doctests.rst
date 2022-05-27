Doctests
========

If you add the `doctest extension
<https://www.sphinx-doc.org/en/master/usage/extensions/doctest.html>`_ to your
:file:`conf.py` (add ``sphinx.ext.doctest`` to the ``extensions`` list), you can
run tests on your documentation to guarantee that it is correct.

You will likely also need to modify the ``sys.path`` within :file:`conf.py` so
that your module is on the path -- after all, it needs to be loaded when it's
being tested.

Here's a test; click the "Page Source" link in the footer to see the source.

Run the doctests with ``make doctest`` from the command line.

.. testsetup::

    from example_package import example

.. testcode::

    print('does this work?')

And the expected output:

.. testoutput::

    does this work?

Here's a doctest block:

.. doctest::

    # In a doctest-style block, you interleave code and output.
    #
    # Like regular doctests, you can use ellipses to act as wildcards
    #
    # Note that a (hidden) .. testsetup: block has already imported the module
    # we are testing
    >>> d = example.Demo(None)
    >>> example.simpler_function(d)
    <example_package.example.Demo object at 0x...>
