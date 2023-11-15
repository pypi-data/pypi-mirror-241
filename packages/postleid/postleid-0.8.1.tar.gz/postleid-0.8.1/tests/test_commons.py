# -*- coding: utf-8 -*-

"""

tests.test_commons

Unit test the postleid.commons module

Copyright (C) 2023 Rainer Schwarzbach

This file is part of postleid.

postleid is free software: you can redistribute it and/or modify
it under the terms of the MIT License.

postleid is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the LICENSE file for more details.

"""


import logging
import random

from unittest import TestCase

from postleid import commons


class Fuctions(TestCase):

    """Helper functions"""

    def test_log_formatted(self):
        """LogWrapper.log_formatted function"""
        for loglevel in (
            logging.DEBUG,
            logging.INFO,
            logging.WARNING,
            logging.ERROR,
        ):
            level_name = logging.getLevelName(loglevel)
            with self.subTest(level=level_name):
                nb_messages = random.randint(1, 5)
                expected_messages = []
                with self.assertLogs(level=level_name) as log_cm:
                    for message_no in range(nb_messages):
                        expected_messages.append(
                            f"{level_name}:root:"
                            f"testing {level_name} #{message_no}"
                        )
                        commons.LogWrapper.log_formatted(
                            loglevel, f"testing {level_name} #{message_no}"
                        )
                    #
                #
                for message_no in range(nb_messages):
                    self.assertEqual(log_cm.output, expected_messages)
                #
            #
        #

    def test_separator_line(self):
        """separator_line function"""
        for width in range(16, 32, 77):
            for codepoint in range(1024):
                element = chr(codepoint)
                with self.subTest(element=element, width=width):
                    self.assertEqual(
                        commons.separator_line(element=element, width=width),
                        element * width,
                    )
                #
            #
        #


# vim: fileencoding=utf-8 ts=4 sts=4 sw=4 autoindent expandtab syntax=python:
