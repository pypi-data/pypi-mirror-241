# -*- coding: utf-8 -*-

"""

tests.test_commandline

Unit test the commandline module


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
import logging
import pathlib
import re
import tempfile

from typing import Dict, Iterator, List, Union
from unittest import TestCase
from unittest.mock import patch

from postleid import commons as pl_commons
from postleid import commandline

from . import commons


EMPTY = ""
KW_FIRST = "first"
KW_MIDDLE = "middle"
KW_LAST = "last"
INDEXES: Dict[str, int] = {KW_FIRST: 0, KW_LAST: -1}
CAPABILITIES: Dict[str, Dict[str, Union[List, str]]] = {
    commons.ARG_COUNTRIES: {
        KW_FIRST: "[ad] <Principality of> Andorra / Principat d’Andorra"
        " / <Fürstentum> Andorra / AND",
        KW_MIDDLE: [
            "[jp] Japan / 日本 / 日本国 / J",
            "[me] Montenegro / Crna Gora / Црна Гора / MNE",
        ],
        KW_LAST: "[zm] <Republic of> Zambia / <Republik> Sambia / Z",
    },
    commons.ARG_RULES: {
        # Andorra
        KW_FIRST: "[ad] ADnnn",
        KW_MIDDLE: [
            # Gibraltar
            "[gi] GX11 1AA",
            # Ireland
            "[ir] nnnnn-nnnnn | nnnnnnnnnn",
        ],
        # Zambia
        KW_LAST: "[zm] nnnnn",
    },
}
MSG_OUTPUT = "output"
MSG_RETURNCODE = "returncode"
PREFIX_LOG_WARNING = "WARNING:root:"

ESCAPED: Dict[int, str] = {
    index: re.escape(phrase)
    for (index, phrase) in pl_commons.STAT_PHRASES.items()
}


class ExecResult(commons.GenericCallResult):

    """Program execution result"""

    @classmethod
    def do_call(cls, *args, **kwargs):
        """Do the real function call"""
        program = commandline.Program(*args)
        return program.execute()


class Functions(TestCase):

    """Test the module functions"""

    def __evaluate_results(self, iterator: Iterator, subject: str) -> None:
        """Run tests on iterator results"""
        output_lines = list(iterator)
        for position, expected in CAPABILITIES[subject].items():
            if isinstance(expected, list):
                for single_expectation in expected:
                    with self.subTest(
                        MSG_OUTPUT,
                        subject=subject,
                        position=position,
                        expect=single_expectation,
                    ):
                        self.assertIn(
                            single_expectation,
                            output_lines,
                        )
                    #
                #
            else:
                with self.subTest(
                    MSG_OUTPUT,
                    subject=subject,
                    position=position,
                    expect=expected,
                ):
                    self.assertEqual(
                        output_lines[INDEXES[position]],
                        expected,
                    )
                #
            #
        #

    def test_list_countries(self) -> None:
        """list_countries() method"""
        self.__evaluate_results(
            commandline.list_countries(), commons.ARG_COUNTRIES
        )

    def test_list_rules(self) -> None:
        """list_rules() method"""
        self.__evaluate_results(commandline.list_rules(), commons.ARG_RULES)


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
            commandline.__version__,
        )

    def test_list_capabilities(self) -> None:
        """list_capabilities() method, version output"""
        for subject in (commons.ARG_COUNTRIES, commons.ARG_RULES):
            with patch(
                commons.SYS_STDOUT, new_callable=io.StringIO
            ) as mock_stdout:
                with self.subTest(MSG_RETURNCODE, subject=subject):
                    self.assertEqual(
                        ExecResult.do_call(
                            commons.OPT_QUIET, commons.ARG_LIST, subject
                        ),
                        commons.RETURNCODE_OK,
                    )
                #
                output_lines = list(
                    mock_stdout.getvalue().strip().splitlines()
                )
                for position, expected in CAPABILITIES[subject].items():
                    if isinstance(expected, list):
                        for single_expectation in expected:
                            with self.subTest(
                                MSG_OUTPUT,
                                subject=subject,
                                position=position,
                                expect=single_expectation,
                            ):
                                self.assertIn(
                                    single_expectation,
                                    output_lines,
                                )
                            #
                        #
                    else:
                        with self.subTest(
                            MSG_OUTPUT,
                            subject=subject,
                            position=position,
                            expect=expected,
                        ):
                            self.assertEqual(
                                output_lines[INDEXES[position]],
                                expected,
                            )
                        #
                    #
                #
            #
        #

    def test_fix(self) -> None:
        """execute() method with fix"""
        with tempfile.TemporaryDirectory() as tempdir:
            temppath = pathlib.Path(tempdir)
            for source, guess_1000s, result in commons.TESTCASES:
                source_df = source.dataframe
                source_path = temppath / f"{source.name}.xlsx"
                source_df.write_excel(source_path)
                arguments = [commons.OPT_QUIET, commons.ARG_FIX]
                if guess_1000s:
                    arguments.append(commons.OPT_GUESS)
                #
                with self.assertLogs(
                    commandline.commons.logging.getLogger(), logging.INFO
                ) as cmgr:
                    with self.subTest(
                        MSG_RETURNCODE,
                        source_name=source.name,
                        guess_1000s=guess_1000s,
                    ):
                        self.assertEqual(
                            ExecResult.do_call(*arguments, str(source_path)),
                            commons.RETURNCODE_OK,
                        )
                    #
                    if not guess_1000s:
                        collected_logs = cmgr.output
                        expected_messages = [pl_commons.S_UNCHANGED] + list(
                            result.evaluation
                        )
                        expected_error = pl_commons.S_UNCHANGED
                        row_number = 0
                        for line in collected_logs:
                            if expected_error:
                                with self.subTest(
                                    "error message",
                                    source_name=source.name,
                                    row_number=row_number,
                                    expected_error=expected_error,
                                ):
                                    self.assertRegex(
                                        line,
                                        f"^{PREFIX_LOG_WARNING}\\s+"
                                        f"{ESCAPED[expected_error]}",
                                    )
                                #
                                expected_error = pl_commons.S_UNCHANGED
                            elif line.startswith(f"{PREFIX_LOG_WARNING}Zeile"):
                                row_number = int(line.split()[1])
                                expected_error = expected_messages[row_number]
                                expected_messages[
                                    row_number
                                ] = pl_commons.S_UNCHANGED
                            #
                        #
                        missing_error_messages = [
                            message
                            for message in expected_messages
                            if message in pl_commons.STATES_ERROR
                        ]
                        with self.subTest(
                            "missing error messages",
                            source_name=source.name,
                        ):
                            self.assertFalse(missing_error_messages)
                        #
                    #
                #
            #
        #


# vim: fileencoding=utf-8 ts=4 sts=4 sw=4 autoindent expandtab syntax=python:
