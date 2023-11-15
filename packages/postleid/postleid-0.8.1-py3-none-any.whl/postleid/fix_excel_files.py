#!/usr/bin/env python

"""

postleid.fix_excel_files

Class for fixing postal codes in excel files

Copyright (C) 2023 Rainer Schwarzbach

This file is part of postleid.

postleid is free software: you can redistribute it and/or modify
it under the terms of the MIT License.

postleid is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the LICENSE file for more details.

"""


import re

from typing import Any, Dict, Iterable, List, Optional, Set, Tuple, Union

import polars

from qrstu import reduce

# local imports
from postleid import commons
from postleid import paths
from postleid import presets
from postleid import rule_checks


PRX_OPTIONAL_PART = re.compile(r"\<(.+?)\>")


def any_part_in(source: str, parts: Iterable[str]) -> bool:
    """Return True if any of the parts is contained in source"""
    for single_part in parts:
        if single_part in source:
            return True
        #
    #
    return False


def reduced_lowercase(source: str) -> str:
    """Reduce text - if possible -
    and return the lowercased result
    """
    try:
        reduced_source = reduce.reduce_text(source)
    except UnicodeError:
        reduced_source = source
    #
    return reduced_source.lower()


class CICoCoLo(dict):

    """Case Insensitive Country Code Lookup"""

    def __init__(
        self,
        mapping: Optional[Dict[str, str]] = None,
        default: str = presets.DEFAULT_CC,
    ) -> None:
        """Initialize the dict"""
        if mapping is None:
            mapping = {}
        super().__init__(
            {
                reduced_lowercase(key): value.lower()
                for (key, value) in mapping.items()
            }
        )
        self.__default = default.lower()

    def __getitem__(self, name):
        """Return the exactly matched item"""
        if not isinstance(name, str):
            return self.__default
        #
        try:
            return super().__getitem__(reduced_lowercase(name))
        except KeyError as error:
            if not name:
                commons.LogWrapper.warning(
                    f"{name!r} not found → lookup result: {self.__default!r}"
                )
                return self.__default
            #
            raise error
        #

    def __setitem__(self, name, value):
        """Set the value always in lowercase"""
        super().__setitem__(reduced_lowercase(name), value.lower())

    def get(self, name, default=None):
        """Return the exactly matched item"""
        try:
            return self[name]
        except KeyError:
            return default
        #

    @classmethod
    def from_config(cls, default: str = presets.DEFAULT_CC) -> "CICoCoLo":
        """Build the country code lookup mapping from the
        country codes configuration file
        """
        mapping: Dict[str, str] = {}
        for (
            iso_cc,
            country_names,
        ) in commons.load_country_names_from_file().items():
            keys: Set[str] = set([iso_cc])
            for configured_name in country_names:
                has_optional_part = PRX_OPTIONAL_PART.search(configured_name)
                if has_optional_part:
                    # Add both variants:
                    # with the optional part deleted,
                    # and with the optional part without the enclosing <>.
                    keys.add(
                        PRX_OPTIONAL_PART.sub("", configured_name).strip()
                    )
                    keys.add(PRX_OPTIONAL_PART.sub(r"\1", configured_name))
                else:
                    keys.add(configured_name)
                #
            #
            for single_key in keys:
                try:
                    existing_cc_entry = mapping[single_key]
                except KeyError:
                    mapping[single_key] = iso_cc
                else:
                    if existing_cc_entry != iso_cc:
                        commons.LogWrapper.warning(
                            f"Not adding {single_key} → {iso_cc} lookup",
                            f"because {single_key} → {existing_cc_entry}"
                            " has already been defined.",
                        )
                    #
                #
            #
        #
        commons.LogWrapper.debug(
            f"Country codes lookup ({len(mapping)} items):"
        )
        for single_key, iso_cc in sorted(mapping.items()):
            commons.LogWrapper.debug(f" - {single_key!r} → {iso_cc!r}")
        #
        return cls(mapping=mapping, default=default)


class DataFixer:

    """Fix cells in a workbook"""

    cc_column = "country_code"

    results_by_error = {
        rule_checks.InvalidFormatError: commons.S_WRONG_FORMAT,
        rule_checks.MissingRulesError: commons.S_MISSING_RULES,
        rule_checks.OutOfRangeError: commons.S_OUT_OF_RANGE,
        rule_checks.UnsupportedDataTypeError: commons.S_WRONG_DATA_TYPE,
    }

    def __init__(
        self,
        dataframe: polars.DataFrame,
        user_settings: commons.UserSettings,
    ) -> None:
        """Find the active sheet in the workbook"""
        self.user_settings = user_settings
        self.zip_column = ""
        self.__worksheet: List[Dict[str, Any]] = dataframe.to_dicts()
        country_column = ""
        postal_code_heading_parts = [
            part.lower()
            for part in self.user_settings.postal_code_heading_parts
        ]
        country_headings = [
            heading.lower() for heading in self.user_settings.country_headings
        ]
        for column_name in dataframe.columns:
            if column_name == self.cc_column:
                self.cc_column = f"{column_name}_x"
            #
            preprocessed_name = column_name.strip().lower()
            if not self.zip_column:
                if any_part_in(preprocessed_name, postal_code_heading_parts):
                    self.zip_column = column_name
                    continue
                #
            #
            if not country_column:
                if preprocessed_name in country_headings:
                    country_column = column_name
                #
            #
        #
        # Build a cc column
        if country_column:
            commons.LogWrapper.debug(
                f"Reading country data from {country_column}"
            )
            cc_lookup = CICoCoLo.from_config(
                default=self.user_settings.default_country_code
            )
        else:
            commons.LogWrapper.debug(
                "No country column found, skipping __build_cc_lookup()"
            )
            cc_lookup = CICoCoLo(
                default=self.user_settings.default_country_code
            )
        #
        for row in self.__worksheet:
            country = row.get(country_column)
            row[self.cc_column] = cc_lookup.get(country, default="??")
            commons.LogWrapper.debug(str(row))
        #
        self.__validator = rule_checks.ValidatorsCache(
            default_cc=self.user_settings.default_country_code
        )

    @property
    def dataframe(self) -> polars.DataFrame:
        """Return a dataframe from the internal data list"""
        return polars.from_dicts(self.__worksheet)

    def fix_all_zip_codes(self) -> List[int]:
        """Fix all zip codes in an Excel workbook.
        Returns statistics (a list of status codes).
        """
        statistics: List[int] = []
        new_table: List[Dict[str, Any]] = []
        for index, row in enumerate(self.__worksheet):
            result, new_row = self.fix_row(index, row)
            statistics.append(result)
            new_table.append(new_row)
        #
        self.__worksheet = new_table
        return statistics

    def fix_row(
        self, row_number: int, row: Dict[str, Any]
    ) -> Tuple[int, Dict[str, Any]]:
        """Fix the zip code in a single row.
        Delegate fixing to the appropriate operation
        for the cell content type and log the message.
        Return the operation result and the new row in a tuple.
        """
        display_row_number = f"Zeile {row_number + 1}"
        original_value = row[self.zip_column]
        preprocessed_value = self.__preprocess_cell_value(original_value)
        error_details: List[str] = []
        result = commons.S_MISSING_RULES
        try:
            new_value = self.__validator.output_validated(
                preprocessed_value, country=row[self.cc_column]
            )
        except rule_checks.ValidatorError as error:
            error_details.extend(error.args)
            error_details.extend(error.additional_information)
            result = self.results_by_error[type(error)]
        #
        if error_details:
            commons.LogWrapper.warning(
                f"{display_row_number} →  Originalwert: {original_value!r}",
                f"     {commons.STAT_PHRASES[result]} - {error_details[0]}",
            )
            commons.LogWrapper.debug(
                *[f"         - {detail}" for detail in error_details[1:]],
                "     --- Typ nach Vorbehandlung:"
                f" {type(preprocessed_value)}",
            )
        else:
            if new_value == original_value:
                result, details = commons.S_UNCHANGED, "keine Anpassung nötig"
            else:
                row[self.zip_column] = new_value
                result, details = commons.S_FIXED, f"neuer Wert: {new_value!r}"
            #
            commons.LogWrapper.debug(
                f"{display_row_number} →  Originalwert: {original_value!r}",
                f"     {commons.STAT_PHRASES[result]} – {details}",
            )
        #
        return result, row

    def __preprocess_cell_value(
        self, original_value: Any
    ) -> Union[float, int, str]:
        """Return a preprocessed variant of the original value"""
        preprocessed_value = original_value
        if isinstance(original_value, str):
            try:
                preprocessed_value = float(original_value.replace(",", "."))
            except ValueError:
                pass
            else:
                commons.LogWrapper.debug(
                    f"       --- {original_value}"
                    f" → Float: {preprocessed_value}"
                )
            #
        #
        if isinstance(preprocessed_value, int):
            preprocessed_value = int(preprocessed_value)
        elif isinstance(preprocessed_value, float):
            preprocessed_value = float(preprocessed_value)
        #
        if (
            isinstance(preprocessed_value, (int, float))
            and self.user_settings.guess_1000s
            and preprocessed_value < 1000
        ):
            return preprocessed_value * 1000
        #
        return preprocessed_value

    def sort_rows(self):
        """Sort table rows by country code and zip"""
        commons.LogWrapper.info(
            "Sortiere Daten nach Land und Postleitzahl ..."
        )
        new_table = self.dataframe.sort(
            [self.cc_column, self.zip_column]
        ).to_dicts()
        self.__worksheet = new_table

    def save(self, output_file: paths.Path) -> None:
        """Save the dataframe"""
        export_dataframe = self.dataframe.drop(self.cc_column)
        export_dataframe.write_excel(output_file, autofit=True)


def process_file(
    source_path: paths.Path,
    target_path: paths.Path,
    user_settings: commons.UserSettings = commons.UserSettings(),
) -> int:
    """Process the file provided in source_path,
    write output to target_path
    and return the appropriate return code
    """
    commons.LogWrapper.info(f"Lade Datei {source_path} …")
    dataframe = polars.read_excel(source_path)
    commons.LogWrapper.info("… ok")
    data_fixer = DataFixer(dataframe, user_settings)
    statistics = data_fixer.fix_all_zip_codes()
    evaluation = commons.evaluate_results(statistics)
    commons.LogWrapper.info(commons.separator_line())
    if evaluation.data_changed:
        if evaluation.everything_is_fine:
            data_fixer.sort_rows()
        else:
            commons.LogWrapper.warning(
                "Da die Orignaldaten nicht fehlerfrei waren,"
                " wurden sie nicht nach Land und Postleitzahl sortiert."
            )
        #
        commons.LogWrapper.info(f"Schreibe Ausgabedatei {target_path} …")
        try:
            data_fixer.save(target_path)
        except OSError as error:
            commons.LogWrapper.error(str(error))
            return commons.RETURNCODE_ERROR
        #
        commons.LogWrapper.info("… ok")
    else:
        if evaluation.everything_is_fine:
            no_errors = "keine Fehler"
        else:
            no_errors = "keine automatisiert behebbaren Fehler"
        #
        commons.LogWrapper.info(
            "Es wird keine Ausgabedatei geschrieben,",
            f"weil die Daten {no_errors} enthalten.",
        )
    #
    return commons.RETURNCODE_OK


# vim: fileencoding=utf-8 sw=4 ts=4 sts=4 expandtab autoindent syntax=python:
