from typing import Union
from dateutil.parser import parse
import pytz
from datetime import datetime, timedelta


def timestamp_to_influx_string(timestamp: Union[str, datetime], offset: int = None) -> str:
    if type(timestamp) is str:
        timestamp = parse(timestamp)
    if offset is not None:
        timestamp = timestamp - timedelta(hours=int(offset))
    return timestamp.strftime("%Y-%m-%dT%H:%M:%S.%fZ")


def localize_dt(dt: datetime, timezone: str = 'Europe/Ljubljana', to_str: bool = False):
    tz = pytz.timezone(timezone)
    dt_localized = tz.localize(dt)
    offset = dt_localized.utcoffset().total_seconds() / 60 / 60
    dt = dt_localized.replace(tzinfo=None) + timedelta(hours=offset)
    if to_str:
        dt = str(dt)
    return dt


def dt_to_utc(dt: datetime, timezone: str = 'Europe/Ljubljana', to_str: bool = False):
    tz = pytz.timezone(timezone)
    dt_localized = tz.localize(dt)
    offset = dt_localized.utcoffset().total_seconds() / 60 / 60
    dt = dt_localized.replace(tzinfo=None) - timedelta(hours=offset)
    if to_str:
        dt = str(dt)
    return dt


def format_large_number(number):
    if number < 1000:
        return str(number)
    elif number < 1_000_000:
        return f"{number / 1000:.2f}k"
    elif number < 1_000_000_000:
        return f"{number / 1_000_000:.6f}M"
    else:
        return f"{number / 1_000_000_000:.6f}B"


if __name__ == '__main__':
    print(localize_dt(datetime.now()))
