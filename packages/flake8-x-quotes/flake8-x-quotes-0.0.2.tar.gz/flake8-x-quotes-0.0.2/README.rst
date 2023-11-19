flake8-x-quotes - fork of flake8-x-quotes with an update for f-strings
======================================================================

..
   TODO: Implement GitHub CI & show badge here

Major update from flake8-quotes 2.0.0
-------------------------------------
We automatically encourage avoiding escaping quotes as per `PEP 8 <https://www.python.org/dev/peps/pep-0008/#string-quotes>`_. To disable this, use ``--no-avoid-escape`` (can be used in configuration file via ``avoid-escape``).

Deprecated option removed from this fork of flake8-quotes
---------------------------------------------------------

- ``--quotes`` - now renamed to ``--inline-quotes``.

Usage
-----

If you are using flake8 it's as easy as:

.. code:: shell

    pip install flake8-x-quotes

Now you don't need to worry about people like @sectioneight constantly
complaining that you are using double-quotes and not single-quotes.

Warnings
--------

This package adds flake8 warnings with the prefix ``Q0``. You might want to
enable this warning inside your flake8 configuration file. Typically that
will be ``.flake8`` inside the root folder of your project.

.. code:: ini

    select = Q0

The current set of warnings is:

==== =========================================================================
Code Description
---- -------------------------------------------------------------------------
Q000 Remove bad quotes
Q001 Remove bad quotes from multiline string
Q002 Remove bad quotes from docstring
Q003 Change outer quotes to avoid escaping inner quotes
Q099 [flake8-x-quotes] Remove bad quotes from f-string - CODE IS SUBJECT TO CHANGE
==== =========================================================================

Configuration
-------------

By default, we expect single quotes (') and look for unwanted double quotes (") (other way around for f-string quotes, multiline quotes, and docstring quotes). To expect double quotes (") and find unwanted single quotes ('), use the CLI option:

.. code:: shell

    flake8 --inline-quotes '"'
    # We also support "double" and "single"
    # flake8 --inline-quotes 'double'
    #
    # We also support configuration for multiline quotes
    # flake8 --inline-quotes '"' --multiline-quotes "'"
    # We also support "'''"
    # flake8 --inline-quotes '"' --multiline-quotes "'''"
    #
    # We also support docstring quotes similarly
    # flake8 --inline-quotes '"' --docstring-quotes "'"
    # flake8 --inline-quotes '"' --docstring-quotes "'''"

    # We also support disabling escaping quotes
    # flake8 --no-avoid-escape

    # [flake8-x-quotes] configure for f-string vs normal string literal:
    flake8 --inline-quotes 'double' --f-string-quotes 'single'

or configuration option in `tox.ini`/`setup.cfg`.

.. code:: ini

    [flake8]
    inline-quotes = "
    # We also support "double" and "single"
    # inline-quotes = double
    #
    # We also support configuration for multiline quotes
    # multiline-quotes = '
    # We also support "'''"
    # multiline-quotes = '''
    #
    # We also support docstring quotes similarly
    # docstring-quotes = '
    # docstring-quotes = '''
    #
    # We also support disabling escaping quotes
    # avoid-escape = False
    #
    # [flake8-x-quotes] configure for f-string vs normal string literal:
    # inline-quotes = double
    # f-string-quotes = single

Supported Python versions
-------------------------

- minimum Python version tested & supported with: 3.8
- known issue with f-string starting with Python 3.12: <https://github.com/zheller/flake8-quotes/issues/117>

Caveats
-------

We follow the `PEP8 conventions <https://www.python.org/dev/peps/pep-0008/#string-quotes>`_ to avoid backslashes in the string. So, no matter what configuration you are using (single or double quotes) these are always valid strings

.. code:: python

    s = 'double "quotes" wrapped in singles are ignored'
    s = "single 'quotes' wrapped in doubles are ignored"
