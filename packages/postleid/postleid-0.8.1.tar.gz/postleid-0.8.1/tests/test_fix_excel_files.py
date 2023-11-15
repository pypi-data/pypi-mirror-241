# -*- coding: utf-8 -*-

"""

tests.test_fix_excel_files

Unit test the postleid.fix_excel_files module

Copyright (C) 2023 Rainer Schwarzbach

This file is part of postleid.

postleid is free software: you can redistribute it and/or modify
it under the terms of the MIT License.

postleid is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the LICENSE file for more details.

"""


import json

from typing import Dict, List
from unittest import TestCase
from unittest.mock import patch

from postleid import commons as pl_commons
from postleid import fix_excel_files
from postleid import presets

from . import commons


KW_DATAFRAME = "dataframe"
KW_STATS = "statistics"

PLFEFC_LOAD = "postleid.fix_excel_files.commons.load_country_names_from_file"


def mock_country_names() -> Dict[str, List[str]]:
    """Mockup country names"""
    return {
        "xf": ["Freedonia", "Fredonia"],
        "xs": ["Sylvania"],
        "fd": ["Fredonia"],
    }


class CICoCoLo(TestCase):

    """Test country code lookup"""

    def test_duplicate_insert_warning(self):
        """Warning when creating duplicates"""
        with patch(PLFEFC_LOAD, new=mock_country_names):
            with self.assertLogs(
                fix_excel_files.commons.logging.getLogger(),
                pl_commons.logging.WARNING,
            ):
                lookup = fix_excel_files.CICoCoLo.from_config()
            #
            self.assertEqual(lookup["Fredonia"], "xf")
        #

    def test_missing_items(self):
        """default values or KeyError"""
        lookup = fix_excel_files.CICoCoLo.from_config(
            default=presets.DEFAULT_CC
        )
        with self.subTest("configured default"):
            with self.assertLogs(
                fix_excel_files.commons.logging.getLogger(),
                pl_commons.logging.WARNING,
            ):
                self.assertEqual(lookup[""], presets.DEFAULT_CC)
            #
        #
        with self.subTest("key error"):
            self.assertRaises(KeyError, lookup.__getitem__, "nowhere")
        #
        with self.subTest("default with get()"):
            self.assertEqual(lookup.get("nowhere", "xx"), "xx")
        #

    def test_lookup(self):
        """lookup country codes on the basis of an existing ISO-3166-1 file"""
        try:
            with open(
                "/usr/share/iso-codes/json/iso_3166-1.json",
                mode="r",
                encoding="utf-8",
            ) as iso_codes_file:
                iso_codes = json.load(iso_codes_file)
        except OSError as error:
            self.skipTest(f"Error opening ISO codes file: {error}")
            return
        #
        lookup = fix_excel_files.CICoCoLo.from_config(
            default=presets.DEFAULT_CC
        )
        known_ccs = set(lookup.values())
        for country_data in iso_codes["3166-1"]:
            names = [country_data["name"]]
            try:
                names.append(country_data["official_name"])
            except KeyError:
                pass
            #
            alpha_2 = country_data["alpha_2"].lower()
            name = country_data["name"]
            if alpha_2 not in known_ccs:
                with self.subTest(cc=alpha_2, expect_defined=False):
                    self.assertRaises(
                        KeyError,
                        lookup.__getitem__,
                        alpha_2,
                    )
                #
                with self.subTest(name=name, expect_defined=False):
                    self.assertRaises(
                        KeyError,
                        lookup.__getitem__,
                        name,
                    )
                #
                continue
            #
            with self.subTest(cc=alpha_2, expect_defined=True):
                self.assertEqual(
                    lookup[alpha_2],
                    alpha_2,
                )
            #
            with self.subTest(name=name, expected=alpha_2):
                self.assertEqual(
                    lookup[name],
                    alpha_2,
                )
            #
            # existing_cc = data_fixer.lookup_country_code(alpha_2)
            # if existing_cc == expected_cc:
            try:
                official_name = country_data["official_name"]
            except KeyError:
                continue
            #
            with self.subTest(official_name=official_name, expected=alpha_2):
                self.assertEqual(
                    lookup[official_name],
                    alpha_2,
                )
            #
        #

    def test_setitem(self):
        """set items"""
        lookup = fix_excel_files.CICoCoLo.from_config(
            default=presets.DEFAULT_CC
        )
        lookup["NowHere"] = "ZZ"
        with self.subTest("exact key"):
            self.assertNotIn("NowHere", lookup)
        #
        with self.subTest("lower key"):
            self.assertIn("nowhere", lookup)
        #
        with self.subTest("lookup result"):
            self.assertEqual(lookup["NoWhErE"], "zz")
        #


class DataFixer(TestCase):

    """DataFixer tests"""

    def test_fix_excel_files(self) -> None:
        """fix_excel_files() method"""
        for source, guess_1000s, result in commons.TESTCASES:
            source_df = source.dataframe
            result_df = result.dataframe
            # test_table = testdata.DIRECTORY[source_name]
            data_fixer = fix_excel_files.DataFixer(
                source_df,
                pl_commons.UserSettings(guess_1000s=guess_1000s),
            )
            with self.subTest(
                KW_STATS, source_name=source.name, guess_1000s=guess_1000s
            ):
                self.assertEqual(
                    data_fixer.fix_all_zip_codes(),
                    list(result.evaluation),
                )
            #
            with self.subTest(
                KW_DATAFRAME, source_name=source.name, guess_1000s=guess_1000s
            ):
                self.assertEqual(
                    data_fixer.dataframe.drop(
                        data_fixer.cc_column
                    ).to_init_repr(),
                    result_df.to_init_repr(),
                )
            #
        #


# vim: fileencoding=utf-8 ts=4 sts=4 sw=4 autoindent expandtab syntax=python:
