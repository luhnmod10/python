Luhn (Mod 10)
=============

.. image:: https://travis-ci.org/luhnmod10/python.svg?branch=master
    :target: https://travis-ci.org/luhnmod10/python

A fast and simple in-place implementation of the `luhn check algorithm <https://en.wikipedia.org/wiki/Luhn_algorithm>`_ in Python. Implementations in other languages can be found at `github.com/luhnmod10 <https://github.com/luhnmod10>`_.

Usage
-----

Install the package:

.. code-block:: console

  pip install luhnmod10

Or:

.. code-block:: console

  easy_install luhnmod10

Then:

.. code-block:: python

  from luhnmod10
  luhnmod10.valid('4242424242424242')

Contributing
------------

Contributions are welcome! If you can improve the execution time of this implementation without increasing its complexity, please open a pull request. To test your change, run `make` in the repository to run the tests and the benchmarks.
