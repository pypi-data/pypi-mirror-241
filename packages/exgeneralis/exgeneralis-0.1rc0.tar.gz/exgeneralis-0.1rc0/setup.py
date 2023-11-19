#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

## {{{ ---- [ SCM/COPYRIGHT/LICENSE HEADER ] -------------------------
#
# File:
#
#   git:/setup.py
#
# Copyright:
#
#   N/A
#
# License:
#
#   This file contains generic, boiler-plate code to bootstrap
#   setuptools, and is therefore considered to be in the public
#   domain.
#
## }}} ---- [ SCM/COPYRIGHT/LICENSE HEADER ] -------------------------

from setuptools import setup, find_packages

setup(
  name = 'exgeneralis',
  version = '0.1-pre',
  description = \
    'Small collection of functions and classes oft-recreated in my own projects',
  packages = find_packages(),
  classifiers = [
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
  ],
  python_requires = '>= 3.10.12',
)

##
# vim: ts=2 sw=2 et fdm=marker :
##
