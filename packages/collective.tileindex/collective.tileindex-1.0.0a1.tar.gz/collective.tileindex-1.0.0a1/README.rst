.. This README is meant for consumption by humans and PyPI. PyPI can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on PyPI or github. It is a comment.

.. image:: https://github.com/collective/collective.tileindex/actions/workflows/plone-package.yml/badge.svg
    :target: https://github.com/collective/collective.tileindex/actions/workflows/plone-package.yml

.. image:: https://img.shields.io/pypi/v/collective.tileindex.svg
    :target: https://pypi.python.org/pypi/collective.tileindex/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/status/collective.tileindex.svg
    :target: https://pypi.python.org/pypi/collective.tileindex
    :alt: Egg Status

.. image:: https://img.shields.io/pypi/pyversions/collective.tileindex.svg?style=plastic   :alt: Supported - Python Versions

.. image:: https://img.shields.io/pypi/l/collective.tileindex.svg
    :target: https://pypi.python.org/pypi/collective.tileindex/
    :alt: License


====================
collective.tileindex
====================

An add-on for Plone

Features
--------

- Catalog index that tells you which tiles are in use.
  Think of Mosaic or collective.cover, or any package that builds on ``plone.app.blocks``.
- ``tile-types-view`` for a page, showing which tiles this page uses.
- ``tile-types-overview`` for the Plone site root, with a total for the whole site, including search results for individual tiles.


Documentation
-------------

The documentation is this README file.


Translations
------------

This product has been translated into

- Dutch


Installation
------------

Install collective.tileindex by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.tileindex


and then running ``bin/buildout``.
Go to the Add-ons control panel to activate it.
This goes through the whole Plone Site and updates the index for items with the ``plone.layoutaware`` behavior.


Authors
-------

- Fred van Dijk (Zest Software)
- Maurits van Rees (Zest Software)


Contribute
----------

- Issue Tracker: https://github.com/collective/collective.tileindex/issues
- Source Code: https://github.com/collective/collective.tileindex


Support
-------

If you are having issues, please let us know.
We have a mailing list located at: project@example.com


License
-------

The project is licensed under the GPLv2.
