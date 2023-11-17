Bankline Direct Parser
======================

Python module for parsing Natwest/RBS Bankline Direct Data Services files.

Requirements
------------

Only Python 3.7+ is supported.

Installation
------------

.. code-block:: shell

    pip install bankline-direct-parser

Usage
-----

.. code-block:: python

    from bankline_parser.data_services import parse

    # from file
    with open(filename) as f:
        parsed = parse(f)
        if parsed.is_valid():
            print(parsed.accounts[0].records[0].transaction_code)
        else:
            print(parsed.errors)

    # from list of rows
    parsed = parse(lines)

Model Layout
------------

.. code-block::

    DataServicesFile
        VolumeHeaderLabel
        [Account]
            FileHeaderLabel
            UserHeaderLabel
            [DataRecord|BalanceRecord]
            UserTrailerLabel

Development
-----------

.. image:: https://github.com/ministryofjustice/bankline-direct-parser/actions/workflows/test.yml/badge.svg?branch=main
    :target: https://github.com/ministryofjustice/bankline-direct-parser/actions/workflows/test.yml

.. image:: https://github.com/ministryofjustice/bankline-direct-parser/actions/workflows/lint.yml/badge.svg?branch=main
    :target: https://github.com/ministryofjustice/bankline-direct-parser/actions/workflows/lint.yml

Please report bugs and open pull requests on `GitHub`_.

To work on changes to this library, it’s recommended to install it in editable mode into a virtual environment,
i.e. ``pip install --editable .``

Use ``python -m tests`` to run all tests locally.
Alternatively, you can use ``tox`` if you have multiple python versions.

[Only for GitHub team members] Distribute a new version to `PyPI`_ by:

- updating the ``VERSION`` tuple in ``bankline_parser/__init__.py``
- adding a note to the `History`_
- publishing a release on GitHub which triggers an upload to PyPI;
  alternatively, run ``python -m build; twine upload dist/*`` locally

History
-------

0.8
    Migrated test, build and release processes away from deprecated setuptools commands.
    No significant library changes.

0.7
    Maintenance release, no library changes.

0.2 - 0.6
    No significant library changes, other than support for newer versions of python.

0.1
    Original release.

Copyright
---------

Copyright (C) 2023 HM Government (Ministry of Justice Digital & Technology).
See LICENSE.txt for further details.

.. _GitHub: https://github.com/ministryofjustice/bankline-direct-parser
.. _PyPI: https://pypi.org/project/bankline-direct-parser/
