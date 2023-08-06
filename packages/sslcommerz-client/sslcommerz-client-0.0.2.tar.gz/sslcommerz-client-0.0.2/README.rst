========
Overview
========

A Sane SSLCommerz Client for Python.

* Free software: MIT license

Installation
============

::

    pip install sslcommerz-client

You can also install the in-development version with::

    pip install https://gitlab.com/codesigntheory/python-sslcommerz-client/-/archive/master/python-sslcommerz-client-master.zip


Documentation
=============


https://python-sslcommerz-client.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
