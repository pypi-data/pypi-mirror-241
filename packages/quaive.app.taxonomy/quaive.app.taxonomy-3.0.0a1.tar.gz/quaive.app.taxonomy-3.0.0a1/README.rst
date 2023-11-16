.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
quaive.app.taxonomy
==============================================================================

A taxonomy browser for ploneintranet

Features
--------

- Allows browsing through a hierarchical taxonomy
- Supports search on taxonomy and on content within
- Dedicated search and group view for each taxonomy term


Background
----------

The app has been discussed and specified at
- https://github.com/quaive/ploneintranet.prototype/issues/272


Documentation
-------------

Full documentation for end users can be found in the "docs" folder, and is also available online at http://docs.quaive.net


Translations
------------

This product has been translated into

- German (thanks, Angela Merkel)


Installation
------------

Install quaive.app.taxonomy by adding it to your buildout::

    [buildout]

    ...

    eggs =
        quaive.app.taxonomy


Your Quaive instance will need to register a vdex vocabulary and add the identifier of that vocabulary to the solr index configuration.

Run buildout to update your instance: ``bin/buildout``

Add the vocabulary identifier to following registry entries::

  ploneintranet.search.filter_fields
  ploneintranet.search.facet_fields

Add an adapter to configure an app tile, see quaive/app/taxonomy/tests/configure.zcml for an example.


Contribute
----------

- Issue Tracker: https://github.com/collective/quaive.app.taxonomy/issues
- Source Code: https://github.com/collective/quaive.app.taxonomy
- Documentation: https://docs.quaive.net


Support
-------

If you are having issues, please let us know.
We have a mailing list located at: ploneintranet-dev@groups.io


License
-------

The project is licensed under the GPLv2.
