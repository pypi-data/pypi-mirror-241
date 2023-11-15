# -*- coding: utf-8 -*-

"""

postleid.commandline

Command line functionality


Copyright (C) 2023 Rainer Schwarzbach

This file is part of postleid.

postleid is free software: you can redistribute it and/or modify
it under the terms of the MIT License.

postleid is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the LICENSE file for more details.

"""


import argparse
import gettext
import logging
import shutil

from typing import Iterator, List

# local imports
from postleid import __version__
from postleid import commons
from postleid import fix_excel_files
from postleid import paths
from postleid import presets
from postleid import rule_checks


#
# Constants
#


TARGET_COUNTRIES = "countries"
TARGET_RULES = "rules"


#
# Rules and countries iterator functions
#


def list_countries() -> Iterator[str]:
    """Return an iterator over supported countries"""
    country_names = commons.load_country_names_from_file()
    rules = commons.load_rules_from_file()
    countries_without_rules: List[str] = []
    commons.LogWrapper.info("Unterstützte Länder:", commons.separator_line())
    for iso_cc, names in country_names.items():
        line = f"[{iso_cc}] {' / '.join(names)}"
        if iso_cc in rules:
            yield line
        else:
            countries_without_rules.append(line)
        #
    #
    rules_without_country_names = [
        f"[{iso_cc}] {country_rule.get('comment', '')}"
        for iso_cc, country_rule in rules.items()
        if iso_cc not in country_names
    ]
    if countries_without_rules:
        commons.LogWrapper.debug(
            commons.separator_line(),
            "Bekannte Länder ohne hinterlegte Regeln für den Country Code:",
            commons.separator_line(),
            *countries_without_rules,
        )
    #
    if rules_without_country_names:
        commons.LogWrapper.debug(
            commons.separator_line(),
            "Country Codes mit hinterlegten Regeln,"
            " aber ohne Klarnamen des Landes:",
            commons.separator_line(),
            *rules_without_country_names,
        )
    #


def list_rules() -> Iterator[str]:
    """Return an iterator over rules by country"""
    rules = commons.load_rules_from_file()
    commons.LogWrapper.info(
        "Regeln je Country Code",
        commons.separator_line(),
        "Legende:",
        " - a → ein Großbuchstabe",
        " - [a] → ein Großbuchstabe, optional",
        " - n → eine Ziffer",
        " - ? → entweder ein Großbuchstabe oder eine Ziffer",
        " - [a/n] → entweder ein Großbuchstabe oder eine Ziffer, optional",
        " - alle anderen Zeichen: exakt wie abgebildet",
        commons.separator_line(),
    )
    validators = rule_checks.ValidatorsCache()
    for iso_cc, single_cc_rule in rules.items():
        patterns: List[str] = []
        regexes: List[str] = []
        for variant in validators[iso_cc]:
            patterns.append(variant.full_pattern.replace("cc", iso_cc.upper()))
            regexes.append(variant.full_prx.pattern)
        #
        yield f"[{iso_cc}] {' | '.join(patterns)}"
        commons.LogWrapper.debug(
            f"{single_cc_rule['comment']} [{iso_cc}]:",
            "  Regular expression(s):",
        )
        for index, single_re in enumerate(regexes):
            commons.LogWrapper.debug(f"   - {patterns[index]} → {single_re}")
        #
        commons.LogWrapper.debug("  Konfiguration:")
        for line in commons.dump_yaml(single_cc_rule):
            commons.LogWrapper.debug(f"    {line}")
        #
    #


#
# classes
#


class Program:

    """Command line program"""

    name: str = "postleid"
    description: str = "Postleitzahlen in Excel-Dateien korrigieren"

    def __init__(self, *args: str) -> None:
        """Parse command line arguments and initialize the logger

        :param args: a list of command line arguments
        """
        self.__arguments = self._parse_args(*args)
        commons.LogWrapper(self.arguments.loglevel)

    @property
    def arguments(self) -> argparse.Namespace:
        """Property: command line arguments

        :returns: the parsed command line arguments
        """
        return self.__arguments

    def list_capabilities(self) -> int:
        """List the capabilities of the script
        (ie. supported countries and country rules).
        Return the exit code for the script.
        """
        if self.arguments.target == TARGET_COUNTRIES:
            list_function = list_countries
        elif self.arguments.target == TARGET_RULES:
            list_function = list_rules
        else:
            commons.LogWrapper.error(
                f"Ungültiges Argument {self.arguments.target!r}"
            )
            return commons.RETURNCODE_ERROR
        #
        try:
            for line in list_function():
                print(line)
            #
        except OSError as error:
            commons.LogWrapper.error(f"{error}")
            return commons.RETURNCODE_ERROR
        #
        return commons.RETURNCODE_OK

    def fix_excel_data(self) -> int:
        """Check the zip codes in the input file,
        and write fixed results to the output file if necessary.
        Return the exit code for the script.
        """
        source_path = self.arguments.excel_file.resolve()
        target_path = self.arguments.output_file
        if target_path:
            target_path = target_path.resolve()
        else:
            target_path = (
                source_path.parent
                / f"{presets.DEFAULT_FIXED_FILE_PREFIX}{source_path.name}"
            )
        #
        if not self.arguments.settings_file.exists():
            default_settings_path = (
                paths.PACKAGE_DATA_PATH / "default_user_settings.yaml"
            )
            commons.LogWrapper.info(
                f"Einstellungsdatei {self.arguments.settings_file}"
                " noch nicht vorhanden",
                f" → erzeuge eine neue aus {default_settings_path} …",
            )
            shutil.copy2(default_settings_path, self.arguments.settings_file)
            commons.LogWrapper.info("… ok")
        #
        commons.LogWrapper.info(
            f"Lade Einstellungen aus {self.arguments.settings_file} …"
        )
        loaded_settings = commons.load_yaml_from_path(
            self.arguments.settings_file
        )
        user_settings = commons.UserSettings(**loaded_settings)
        if self.arguments.guess_1000s:
            user_settings.guess_1000s = True
        #
        commons.LogWrapper.info("… ok")
        commons.LogWrapper.info(commons.separator_line())
        return fix_excel_files.process_file(
            source_path,
            target_path,
            user_settings=user_settings,
        )

    def _parse_args(self, *args: str) -> argparse.Namespace:
        """Parse command line arguments using argparse
        and return the arguments namespace.

        :param args: the command line arguments
        :returns: the parsed command line arguments as returned
            by argparse.ArgumentParser().parse_args()
        """
        # ------------------------------------------------------------------
        # Argparse translation code adapted from
        # <https://github.com/s-ball/i18nparse>
        translation = gettext.translation(
            "argparse",
            localedir=paths.PACKAGE_LOCALE_PATH,
            languages=["de"],
            fallback=True,
        )
        argparse._ = translation.gettext  # type: ignore
        argparse.ngettext = translation.ngettext  # type: ignore
        # ------------------------------------------------------------------
        main_parser = argparse.ArgumentParser(
            prog=self.name,
            description=self.description,
        )
        main_parser.set_defaults(loglevel=logging.INFO)
        main_parser.add_argument(
            "--version",
            action="version",
            version=__version__,
            help="Version anzeigen und beenden",
        )
        logging_group = main_parser.add_argument_group(
            "Logging-Optionen",
            "steuern die Meldungsausgaben (Standard-Loglevel: INFO)",
        )
        verbosity = logging_group.add_mutually_exclusive_group()
        verbosity.add_argument(
            "-v",
            "--verbose",
            action="store_const",
            const=logging.DEBUG,
            dest="loglevel",
            help="alle Meldungen ausgeben (Loglevel DEBUG)",
        )
        verbosity.add_argument(
            "-q",
            "--quiet",
            action="store_const",
            const=logging.WARNING,
            dest="loglevel",
            help="nur Warnungen und Fehler ausgeben (Loglevel WARNING)",
        )
        subparsers = main_parser.add_subparsers(
            required=True,
            title="Teilbefehle",
            help="'list': Länder bzw. Regeln ausgeben und beenden;"
            " 'fix': Daten korrigieren."
            " Hilfe zum jeweiligen Aufruf mit nachfolgendem -h",
        )
        list_parser = subparsers.add_parser(
            "list",
            description="Unterstützte Länder"
            " bzw. Muster pro Country Code auflisten",
        )
        list_parser.add_argument(
            "target",
            choices=(TARGET_COUNTRIES, TARGET_RULES),
            help=f"{TARGET_COUNTRIES!r}: Länder"
            f" oder {TARGET_RULES!r}: Muster pro Country Code",
        )
        list_parser.set_defaults(func=self.list_capabilities)
        fix_parser = subparsers.add_parser(
            "fix", description="Postleitzahlen in Excel-Dateien korrigieren"
        )
        fix_parser.add_argument(
            "-g",
            "--guess-1000s",
            action="store_true",
            help="Postleitzahlen unter 1000 mit 1000 multiplizieren",
        )
        fix_parser.add_argument(
            "-o",
            "--output-file",
            metavar="AUSGABEDATEI",
            type=paths.Path,
            help="die Ausgabedatei (Standardwert: Name der Original-Exceldatei"
            f" mit vorangestelltem {presets.DEFAULT_FIXED_FILE_PREFIX!r})",
        )
        fix_parser.add_argument(
            "-s",
            "--settings-file",
            metavar="EINSTELLUNGSDATEI",
            type=paths.Path,
            help="die Datei mit Benutzereinstellungen"
            " (Standardwert: %(default)s im aktuellen Verzeichnis)",
        )
        fix_parser.add_argument(
            "excel_file",
            metavar="EXCELDATEI",
            type=paths.Path,
            help="die Original-Exceldatei",
        )
        fix_parser.set_defaults(
            func=self.fix_excel_data,
            settings_file=paths.Path(presets.DEFAULT_USER_SETTINGS_FILE_NAME),
        )
        return main_parser.parse_args(args=args or None)

    def execute(self) -> int:
        """Execute the program
        :returns: the returncode for the script
        """
        return self.arguments.func()


# vim: fileencoding=utf-8 ts=4 sts=4 sw=4 autoindent expandtab syntax=python:
