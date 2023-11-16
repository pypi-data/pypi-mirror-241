"""This module creates UTC time stamp."""

from datetime import datetime


def date_time_utc() -> str:
    """Returns the date and time stamp in ISO format in UTC time zone.

    Example:
        2023-11-15_UTC_17_06_13_007269
    """
    ts = datetime.utcnow().isoformat()  # The "naive object in UTC"
    ts = ts.replace(":", "_").replace(".", "_")  # Overwrite ":", "." with "_"
    ts = ts.replace("T", "_UTC_")  # Overwrite T with UTC time zone indication
    return ts
