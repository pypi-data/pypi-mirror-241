#!/usr/bin/env python

"""

postleid.testdata

Test data definitions

Copyright (C) 2023 Rainer Schwarzbach

This file is part of postleid.

postleid is free software: you can redistribute it and/or modify
it under the terms of the MIT License.

postleid is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the LICENSE file for more details.

"""


import dataclasses

from typing import Optional

import polars


TABLE_PATTERN_MATCHED = """
shape: (3, 2)
┌─────────────┬──────────┐
│ Country     ┆ Zip Code │
│ ---         ┆ ---      │
│ str         ┆ str      │
╞═════════════╪══════════╡
│ Netherlands ┆ 9876 XY  │
│ Germany     ┆ 12345    │
│ UK          ┆ NW1 8UH  │
└─────────────┴──────────┘
"""

TABLE_FIXABLE = """
shape: (3, 2)
┌─────────┬──────────┐
│ Country ┆ Zip Code │
│ ---     ┆ ---      │
│ str     ┆ i64      │
╞═════════╪══════════╡
│ null    ┆ 7895     │
│ Germany ┆ 1234     │
│ null    ┆ 65432    │
└─────────┴──────────┘
"""

TABLE_REQUIRING_GUESS = """
shape: (14, 3)
┌──────────────────────┬──────────────┬───────────────┐
│ Straße               ┆ Postleitzahl ┆ Stadt         │
│ ---                  ┆ ---          ┆ ---           │
│ str                  ┆ str          ┆ str           │
╞══════════════════════╪══════════════╪═══════════════╡
│ Bochowstraße         ┆ 78.089       ┆ Unterkirnach  │
│ Auf der Hohl         ┆ 55.608       ┆ Berschweiler  │
│ Alfred-Döblin-Straße ┆ 54636        ┆ Eßlingen      │
│ Anna-Paul-Straße     ┆ 31.275       ┆ Lehrte        │
│ ungültig             ┆ 80           ┆ München       │
│ Oberstraße           ┆ 94.508       ┆ Schöllnach    │
│ Finkenhütte          ┆ 56,850       ┆ Hahn          │
│ Heukers Weide        ┆ 77709        ┆ Oberwolfach   │
│ Habichtstraße        ┆ 55758        ┆ Oberhosenbach │
│ Altenburgstraße      ┆ 6484         ┆ Westerhausen  │
│ Obere Bergstraße     ┆ 67808        ┆ Imsweiler     │
│ In den Winkelwiesen  ┆ 55743        ┆ Kirschweiler  │
│ Auf dem Gäu          ┆ 24969        ┆ Großenwiehe   │
│ Anxbachstraße        ┆ 49393        ┆ Lohne         │
└──────────────────────┴──────────────┴───────────────┘
"""

TABLE_UNFIXABLE = """
shape: (4, 2)
┌──────────┬──────────┐
│ Country  ┆ Zip Code │
│ ---      ┆ ---      │
│ str      ┆ str      │
╞══════════╪══════════╡
│ Zimbabwe ┆ 7895     │
│ Germany  ┆ 999      │
│ Denmark  ┆ 65432    │
│ UK       ┆ 8UH ZZ9  │
└──────────┴──────────┘
"""


@dataclasses.dataclass
class ReprTable:

    """Table object with name, table content representation,
    and lazy dataframe cache
    """

    name: str
    table: str
    _dataframe_cache: Optional[polars.DataFrame] = dataclasses.field(
        init=False, default=None
    )

    @property
    def dataframe(self) -> polars.DataFrame:
        """Lazily load the DataFrame object"""
        if self._dataframe_cache is None:
            polars_obj = polars.from_repr(self.table)
            if not isinstance(polars_obj, polars.DataFrame):
                raise ValueError("Expected a DataFrame definition!")
            #
            self._dataframe_cache = polars_obj
        #
        return self._dataframe_cache


SOURCE_PATTERN_MATCHED = ReprTable(
    name="pattern_matched",
    table=TABLE_PATTERN_MATCHED,
)
SOURCE_FIXABLE = ReprTable(
    name="fixable",
    table=TABLE_FIXABLE,
)
SOURCE_REQUIRING_GUESS = ReprTable(
    name="requires_guess",
    table=TABLE_REQUIRING_GUESS,
)
SOURCE_UNFIXABLE = ReprTable(
    name="unfixable",
    table=TABLE_UNFIXABLE,
)


# vim: fileencoding=utf-8 sw=4 ts=4 sts=4 expandtab autoindent syntax=python:
