Changelog
=========


3.0.0a1 (2023-11-16)
--------------------

- Plone 6 compatibility.
  [thet]

- Support for new form styling


2.1.2 (2022-11-07)
------------------

- Use explicit pat-navigation trigger class on navigation elements which were pre Patternslib 9.2 also initialized.
  [thet]


2.1.1 (2022-07-06)
------------------

- Update translations


2.1.0 (2022-03-09)
------------------

- Fixed search box.
- Fixed sidebar links.


2.0.3 (2022-02-16)
------------------

- Update translations.


2.0.2 (2022-01-17)
------------------

- Update translations.
- Translated app tile title.


2.0.1 (2021-08-31)
------------------

- Made compatible with changes in proto (multi-tasking)


2.0.0 (2021-07-27)
------------------

- Consolidate translations management, refs #quaive/ploneintranet/3907.


1.4.0 (2020-06-18)
------------------

- Python3 compatibility (#9)


1.3.2 (2020-03-27)
------------------

- Remove unittest2 dependency.
  [thet]


1.3.1 (2019-03-27)
------------------

- Return an empty dict instead of None in the results_by_* methods
  [ale]


1.3.0 (2018-12-07)
------------------

- Update to the latest Quaive (Fixes #6)


1.2.2 (2017-11-20)
------------------

- Public release.


1.2.1 (2017-08-28)
------------------

Fixes:

- (slc #15736) Don't throw error if search term is unicode [deroiste]


1.2.0 (2017-05-02)
------------------

Fixes:

- Decorate the app view with IAppView to make the app
  compatible with ploneintranet master.
  [ale]


1.1.7 (2016-12-01)
------------------

New features:

- Translation labels.
  [angeldasangel]


1.1.6 (2016-11-21)
------------------

- Nothing changed.


1.1.5 (2016-11-17)
------------------

Fixes:

- Fix sidebar search injection [deroiste]
- Sidebar Search: search by partial taxonomy terms [deroiste]


1.1.4 (2016-10-24)
------------------

New features:

- Sort by date when grouping by workspace and author [deroiste]

Fixes:

- Fix test setup: import config for docconv


1.1.3 (2016-10-14)
------------------

Fixes:

- Adapt to new App structure. All parameters come from the App now,
  not the request
- Adapt to changed search / proto view in ploneintranet


1.1.2 (2016-09-09)
------------------

Fixes:

- Fix tests: use the app as the search tile context [deroiste]
- Fix sidebar enlarger target [pilz]


1.1.1 (2016-09-08)
------------------

Fixes:

- Fix injection target [pilz]


1.1 (2016-09-08)
----------------

Fixes/New features:

- Sort grouped results by title
- Add search grouping by workspace and author
- sidebar-search: use solr instead of the catalog
  The normal Sidebar view uses the catalog, presumably to avoid the delay
  caused by asynchronous indexing with solr.
- sidebar-search: handle unicode vocab terms
- Add the option to configure a separate vocab index
  This allows the search index to have a different id from the
  vocabulary. It's configured on the app_parameters e.g.
  {'vocabulary_index': 'someidx'}
- Also search by vocab terms
- Implement sidebar search
  Design: quaive/ploneintranet.prototype#272
- Updated to app objects
  Also, the vocabulary does not need to be passed as a GET parameter any
  more, since it is now defined in the app_parameters.
- Include documents in the sidebar, implement search
- Improved testing, better handling of values


1.0a1 (2016-07-16)
------------------

- Initial release.
  [pilz]
