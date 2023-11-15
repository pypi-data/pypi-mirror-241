Changelog
=========

2.0.0 (2023-11-15)
------------------

- The test suite now works with Plone 5.2, Python3 and Products.ExternalEditor 3
  [ale-rt]

- Remove unused import not compatible with Plone 6
  [ale-rt]


1.0.3 (2015-08-21)
------------------

- Move controlpanel to z3c.form. Removes dependency on CMFDefault and formlib.
  [pbauer]


1.0.2 (2015-06-04)
------------------

- use the recommended way of including Products.CMFCore permissions
  in configure.zcml so it works for all Plone versions
  [jcerjak]

- Remove dependency on portal_factory (Plone 5 compatibility)
  [mattss]


1.0.1 - 2012-02-10
------------------

- preloading Products.CMFCore.permissions.zcml


1.0.0 - 2010-12-03
------------------

- Initial release [f10w]
