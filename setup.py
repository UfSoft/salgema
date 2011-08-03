#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: sw=4 ts=4 fenc=utf-8 et
# ==============================================================================
# Copyright © 2011 UfSoft.org - Pedro Algarvio <ufs@ufsoft.org>
#
# License: BSD - Please view the LICENSE file for additional information.
# ==============================================================================

from setuptools import setup, find_packages
import salgema as package

setup(name=package.__package__,
      version=package.__version__,
      author=package.__author__,
      author_email=package.__email__,
      url=package.__url__,
      download_url='http://python.org/pypi/%s' % package.__package__,
      description=package.__summary__,
      long_description=package.__description__,
      license=package.__license__,
      platforms="OS Independent - Anywhere Python, OpenSSL and ZeroMQ is known to run.",
      keywords = "ZeroMQ ZMQ Authorization Encryption",
      packages = find_packages(),
      classifiers=[
          'Development Status :: 5 - Alpha',
          'Environment :: Web Environment',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Communications',
          'Topic :: Internet',
          'Topic :: Software Development',
          'Topic :: System :: Networking',
          'Topic :: Utilities',
      ]
)
