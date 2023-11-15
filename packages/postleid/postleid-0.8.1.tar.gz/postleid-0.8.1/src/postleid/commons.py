#!/usr/bin/env python

"""

postleid.commons

Common functions and classes

Copyright (C) 2023 Rainer Schwarzbach

This file is part of postleid.

postleid is free software: you can redistribute it and/or modify
it under the terms of the MIT License.

postleid is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the LICENSE file for more details.

"""


import bisect
import dataclasses
import logging
import textwrap

from collections import Counter

from typing import Any, Dict, Iterator, List, Tuple, Union

import yaml

# local imports
from postleid import paths
from postleid import presets


# Magic numbers for statistics
S_UNCHANGED = 0
S_FIXED = 1
S_MISSING_RULES = 2
S_WRONG_FORMAT = 3
S_WRONG_DATA_TYPE = 4
S_OUT_OF_RANGE = 5

STATES_OK = (S_UNCHANGED, S_FIXED)
STATES_ERROR = (S_WRONG_DATA_TYPE, S_WRONG_FORMAT, S_OUT_OF_RANGE)

STAT_PHRASES: Dict[int, str] = {
    S_UNCHANGED: "(=) unverändert",
    S_FIXED: "(✔) korrigiert",
    S_MISSING_RULES: "(✘) Regeln fehlen",
    S_WRONG_FORMAT: "(✘) falsches Format",
    S_WRONG_DATA_TYPE: "(✘) falscher Datentyp",
    S_OUT_OF_RANGE: "(✘) außerhalb des Bereichs",
}

# Return codes
RETURNCODE_OK = 0
RETURNCODE_ERROR = 1


class LogWrapper:

    """wraps logging functionality"""

    textwrapper = textwrap.TextWrapper(presets.LOG_MESSAGE_MAX_WIDTH)

    def __init__(self, loglevel: int) -> None:
        """Initialize logging"""
        logging.basicConfig(
            format=presets.LOG_MESSAGE_FORMAT,
            level=loglevel,
        )

    @classmethod
    def log_formatted(cls, level: int, *messages: str) -> None:
        """Log the already formatted messages with loglevel,
        wrapping them to a line length of
        at most preferences.LOG_MESSAGE_MAX_WIDTH characters
        """
        output_lines = []
        for single_message in messages:
            output_lines.extend(cls.textwrapper.wrap(single_message))
        #
        for line in output_lines:
            logging.log(level, line)
        #

    @classmethod
    def info(cls, *messages: str) -> None:
        """Log with INFO level"""
        cls.log_formatted(logging.INFO, *messages)

    @classmethod
    def debug(cls, *messages: str) -> None:
        """Log with DEBUG level"""
        cls.log_formatted(logging.DEBUG, *messages)

    @classmethod
    def error(cls, *messages: str) -> None:
        """Log with ERROR level"""
        cls.log_formatted(logging.ERROR, *messages)

    @classmethod
    def warning(cls, *messages: str) -> None:
        """Log with WARNING level"""
        cls.log_formatted(logging.WARNING, *messages)


@dataclasses.dataclass
class UserSettings:

    """Container object for keeping user settings"""

    default_country_code: str = presets.DEFAULT_CC
    guess_1000s: bool = presets.GUESS_1000S
    country_headings: Union[
        List[str], Tuple[str, ...]
    ] = presets.COUNTRY_HEADINGS
    postal_code_heading_parts: Union[
        List[str], Tuple[str, ...]
    ] = presets.POSTAL_CODE_HEADING_PARTS


@dataclasses.dataclass(frozen=True)
class EvaluatedResults:

    """Container object for keeping results"""

    data_changed: bool = False
    everything_is_fine: bool = False


def separator_line(
    element: str = "–", width: int = presets.LOG_MESSAGE_MAX_WIDTH
) -> str:
    """Return a separator line"""
    return element * width


def dump_yaml(data_structure: Any, sort_keys: bool = False) -> Iterator[str]:
    """Return an iterator over the lines of a yaml dump"""
    for line in yaml.safe_dump(
        data_structure, indent=2, default_flow_style=False, sort_keys=sort_keys
    ).splitlines():
        yield line
    #


def evaluate_results(statistics: List[int]) -> EvaluatedResults:
    """Evaluate results, show a summary,
    and return two flags: "everything is fine" and "data changed"
    """
    statistics.sort()
    results = Counter(statistics)
    successful: Counter = Counter()
    errors: Counter = Counter()
    for keyword in sorted(set(statistics)):
        if keyword in (S_FIXED, S_UNCHANGED):
            target = successful
        else:
            target = errors
        #
        start = bisect.bisect_left(statistics, keyword)
        end = bisect.bisect_right(statistics, keyword)
        target.update({keyword: end - start})
        #
    #
    evaluated_results = EvaluatedResults(
        data_changed=bool(results[S_FIXED]),
        everything_is_fine=not sum(errors.values()),
    )
    LogWrapper.log_formatted(
        logging.DEBUG
        if evaluated_results.everything_is_fine
        else logging.WARNING,
        separator_line(),
    )
    max_kw_width = max(len(STAT_PHRASES[status]) for status in results)
    LogWrapper.info(
        f"Ergebnis: {sum(results.values())} Datensätze verarbeitet, davon:",
    )
    for category in (successful, errors):
        for status, frequency in category.items():
            LogWrapper.log_formatted(
                logging.INFO if status in STATES_OK else logging.WARNING,
                f" {f'{STAT_PHRASES[status]}:':<{max_kw_width + 1}}"
                f" {frequency}",
            )
        #
    #
    return evaluated_results


def load_yaml_from_path(path: paths.Path) -> Any:
    """Load a YAML file from the provided path
    and return its deserialized contents
    """
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def load_yaml_data_file(file_name: Union[str, paths.Path]) -> Any:
    """Load YAML from the provided file
    located in the data subdirectory
    and return its deserialized contents
    """
    return load_yaml_from_path(paths.PACKAGE_DATA_PATH / file_name)


def load_rules_from_file() -> Any:
    """Load the postal code rules by country code
    from the appropriate file
    """
    return load_yaml_data_file("postal_code_rules_by_cc.yaml")


def load_country_names_from_file() -> Any:
    """Load the country names by country code
    from the appropriate file
    """
    return load_yaml_data_file("country_names_by_cc.yaml")


# vim: fileencoding=utf-8 sw=4 ts=4 sts=4 expandtab autoindent syntax=python:
