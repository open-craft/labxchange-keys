#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Package metadata for labxchange_keys.
"""
from __future__ import absolute_import, print_function, unicode_literals

import os
import re
import sys

from setuptools import setup


def get_version(*file_paths):
    """
    Extract the version string from the file at the given relative path fragments.
    """
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


def load_requirements(*requirements_paths):
    """
    Load all requirements from the specified requirements files.

    Returns:
        list: Requirements file relative path strings
    """
    requirements = set()
    for path in requirements_paths:
        requirements.update(
            line.split('#')[0].strip() for line in open(path).readlines()
            if is_requirement(line.strip())
        )
    return list(requirements)


def is_requirement(line):
    """
    Return True if the requirement line is a package requirement.

    Returns:
        bool: True if the line is not blank, a comment, a URL, or an included file
    """
    return not (
        line == '' or
        line.startswith('-r') or
        line.startswith('#') or
        line.startswith('-e') or
        line.startswith('git+')
    )


VERSION = get_version('labxchange_keys', '__init__.py')

if sys.argv[-1] == 'tag':
    print("Tagging the version on github:")
    os.system("git tag -a %s -m 'version %s'" % (VERSION, VERSION))
    os.system("git push --tags")
    sys.exit()

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

setup(
    name='labxchange-keys',
    version=VERSION,
    description="""Registers custom OpaqueKeys used by LabXchange""",
    long_description=README,
    author='OpenCraft',
    author_email='help@opencraft.com',
    url='https://gitlab.com/opencraft/client/LabXchange/labxchange-keys',
    packages=[
        'labxchange_keys',
    ],
    include_package_data=True,
    install_requires=load_requirements('requirements/base.in'),
    license="AGPL 3.0",
    zip_safe=False,
    keywords='labxchange',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.8',
    ],
    entry_points={
        'context_key': [
            'lx-pathway = labxchange_keys:PathwayLocator',
        ],
        'usage_key': [
            'lx-pb = labxchange_keys:PathwayUsageLocator',
        ],
    },
)
