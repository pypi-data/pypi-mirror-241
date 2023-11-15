# -*- coding: utf-8 -*-

"""

tests.test_main

Unit test the __main__ module


Copyright (C) 2023 Rainer Schwarzbach

This file is part of postleid.

postleid is free software: you can redistribute it and/or modify
it under the terms of the MIT License.

postleid is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the LICENSE file for more details.

"""


import io

from unittest import TestCase

from unittest.mock import patch

from postleid import __main__ as pkg_main

from . import commons


class ExecResult(commons.GenericCallResult):

    """Program execution result"""

    @classmethod
    def do_call(cls, *args, **kwargs):
        """Do the real function call"""
        return pkg_main.main(*args)


class Program(TestCase):

    """Test the Program class"""

    @patch(commons.SYS_STDOUT, new_callable=io.StringIO)
    def test_version(self, mock_stdout: io.StringIO) -> None:
        """execute() method, version output"""
        with self.assertRaises(SystemExit) as cmgr:
            ExecResult.do_call(commons.OPT_VERSION)
        #
        self.assertEqual(cmgr.exception.code, commons.RETURNCODE_OK)
        self.assertEqual(
            mock_stdout.getvalue().strip(),
            pkg_main.commandline.__version__,
        )


# vim: fileencoding=utf-8 ts=4 sts=4 sw=4 autoindent expandtab syntax=python:
