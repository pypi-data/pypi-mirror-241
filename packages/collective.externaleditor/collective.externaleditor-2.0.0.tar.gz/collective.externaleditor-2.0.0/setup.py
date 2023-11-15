from setuptools import find_packages
from setuptools import setup

import os


version = "2.0.0"

setup(
    name="collective.externaleditor",
    version=version,
    description="Specific Plone layer for Products.ExternalEditor",
    long_description=open("README.rst").read()
    + "\n"
    + open(os.path.join("docs", "HISTORY.rst")).read(),
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Plone :: 5.2",
        "Framework :: Plone :: 6.0",
        "Framework :: Plone :: Addon",
        "Framework :: Plone",
        "Framework :: Plone",
        "Framework :: Zope :: 4",
        "Framework :: Zope :: 5",
        "Framework :: Zope",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python",
    ],
    keywords="Plone",
    author="atReal",
    author_email="contact@atreal.net",
    url="https://github.com/collective/collective.externaleditor/",
    projext_urls={
        "PyPI": "https://pypi.org/project/collective.externaleditor/",
        "Source": "https://github.com/collective/collective.externaleditor",
        "Tracker": "https://github.com/collective/collective.externaleditor/issues",
    },
    license="GPL",
    packages=find_packages(exclude=["ez_setup"]),
    namespace_packages=["collective"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "Plone",
        "Products.CMFCore",
        "Products.CMFPlone",
        "Products.ExternalEditor>=1.1.0dev",
        "Products.GenericSetup",
        "Products.statusmessages",
        "setuptools",
        # -*- Extra requirements: -*-
    ],
    extras_require={
        "test": [
            "plone.app.testing",
            "plone.app.robotframework[debug]",
        ],
    },
    python_requires=">=3.7",
    entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
)
