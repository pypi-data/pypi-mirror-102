#!/usr/bin/env python
from os import path

from setuptools import setup, find_packages

NAME = "Orange3-Shangtang"

VERSION = "0.1.0"

DESCRIPTION = "商汤教育人工智能 API 橙现智能Orange 图形化实现的插件"
LONG_DESCRIPTION = open(path.join(path.dirname(__file__), 'README.pypi')).read()


KEYWORDS = [
    # [PyPi](https://pypi.python.org) packages with keyword "orange3 add-on"
    # can be installed using the Orange Add-on Manager
    'orange3 add-on',
]

PACKAGES = find_packages()

PACKAGE_DATA = {
    'orangecontrib.shangtang.widgets': ['icons/*', 'resources/*'],
}

DATA_FILES = [
    # Data files that will be installed outside site-packages folder
]

INSTALL_REQUIRES = [
    'Orange3-zh >=3.21.0',
]

ENTRY_POINTS = {
    # Entry points that marks this package as an orange add-on. If set, addon will
    # be shown in the add-ons manager even if not published on PyPi.
    'orange3.addon': (
        'shangtang = orangecontrib.shangtang',
    ),

    # Entry point used to specify packages containing widgets.
    'orange.widgets': (
        # Syntax: category name = path.to.package.containing.widgets
        # Widget category specification can be seen in
        #    orangecontrib/example/widgets/__init__.py
        '商汤教育 = orangecontrib.shangtang.widgets',
    ),

    # Register widget help
    # "orange.canvas.help": (
    #     'html-index = orangecontrib.educational.widgets:WIDGET_HELP_PATH',)
}

NAMESPACE_PACKAGES = ["orangecontrib"]


def _discover_tests():
    import unittest
    return unittest.defaultTestLoader.discover('orangecontrib.shangtang',
                                               pattern='test_*.py',
                                               top_level_dir='.')

TEST_SUITE = "setup._discover_tests"

AUTHOR = 'SZZYIIT'
AUTHOR_EMAIL = 'gengy@zhaoyang.org.cn'
URL = "https://github.com/szzyiit/orange3-shangtang"
# DOWNLOAD_URL = "https://github.com/biolab/orange3-educational/releases"


if __name__ == '__main__':
    # include_documentation('doc/build/htmlhelp', 'help/orange3-educational')
    setup(
        name=NAME,
        version=VERSION,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=PACKAGES,
        package_data=PACKAGE_DATA,
        data_files=DATA_FILES,
        install_requires=INSTALL_REQUIRES,
        entry_points=ENTRY_POINTS,
        keywords=KEYWORDS,
        namespace_packages=NAMESPACE_PACKAGES,
        test_suite=TEST_SUITE,
        include_package_data=True,
        zip_safe=False,
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        url=URL,
        classifiers = []
    )
