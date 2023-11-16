"""This module tests the utility module.
"""

import re

import rootstalk.timestamp as ts


def test_timestamp():
    """Tests that the date and time stamp in ISO format in UTC time zone."""
    result = ts.date_time_utc()
    print(result)

    year, month, date, utc, hh, mm, ss, ms = re.split("-|_", result)
    assert len(year) == 4
    assert len(month) == 2
    assert len(date) == 2
    assert utc == "UTC"
    assert len(hh) == 2
    assert int(hh) <= 24
    assert len(mm) == 2
    assert int(mm) < 60
    assert len(ss) == 2
    assert int(ss) < 60
    assert len(ms) == 6
