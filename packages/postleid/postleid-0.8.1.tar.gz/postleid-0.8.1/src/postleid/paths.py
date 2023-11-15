#!/usr/bin/env python

"""

postleid.paths

Paths handling and constants

Copyright (C) 2023 Rainer Schwarzbach

This file is part of postleid.

postleid is free software: you can redistribute it and/or modify
it under the terms of the MIT License.

postleid is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the LICENSE file for more details.

"""


from pathlib import Path


PACKAGE_MODULES_PATH = Path(__file__).resolve().parent
PACKAGE_DATA_PATH = PACKAGE_MODULES_PATH / "data"
PACKAGE_LOCALE_PATH = PACKAGE_MODULES_PATH / "locale"


# vim: fileencoding=utf-8 sw=4 ts=4 sts=4 expandtab autoindent syntax=python:
