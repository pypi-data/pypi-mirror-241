#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

## {{{ ---- [ SCM/COPYRIGHT/LICENSE HEADER ] -------------------------
#
# File:
#
#   git:/exgeneralis/main.py
#
# Copyright:
#
#   Copyright (c) 2023 Francis M <ukmcplyr@gmail.com>
#
# License:
#
#   SPDX-License-Identifier: GPL-2.0
#
#   Ex Generalis is free software; you can redistribute it and/or
#   modify it under the terms of version 2.0 of the GNU General
#   Public License as published by the Free Software Foundation.
#
#   For the full terms, see the file LICENSE.txt in the top-level
#   of this repository/distribution.  Alternatively they can be
#   viewed via <https://spdx.org/licenses/GPL-2.0-only.html>.
#
## }}} ---- [ SCM/COPYRIGHT/LICENSE HEADER ] -------------------------

## {{{ typeof(obj)
def typeof(obj):
  type_str = str(type(obj))
  if type_str.startswith("<class '") and type_str.endswith("'>"):
    return type_str[8:-2]
  return type(obj).__name__
## }}}

## {{{ to_str(obj, [encoding='utf-8', errors='strict'])
def to_str(obj, encoding='utf-8', errors='strict'):
  if typeof(obj) == 'bytes':
    return obj.decode(encoding, errors)
  else:
    return str(obj)
## }}}

##
# vim: ts=2 sw=2 et fdm=marker :
##
