# Democritus Dates

[![PyPI](https://img.shields.io/pypi/v/d8s-dates.svg)](https://pypi.python.org/pypi/d8s-dates)
[![CI](https://github.com/democritus-project/d8s-dates/workflows/CI/badge.svg)](https://github.com/democritus-project/d8s-dates/actions)
[![Lint](https://github.com/democritus-project/d8s-dates/workflows/Lint/badge.svg)](https://github.com/democritus-project/d8s-dates/actions)
[![codecov](https://codecov.io/gh/democritus-project/d8s-dates/branch/main/graph/badge.svg?token=V0WOIXRGMM)](https://codecov.io/gh/democritus-project/d8s-dates)
[![The Democritus Project uses semver version 2.0.0](https://img.shields.io/badge/-semver%20v2.0.0-22bfda)](https://semver.org/spec/v2.0.0.html)
[![The Democritus Project uses black to format code](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://choosealicense.com/licenses/lgpl-3.0/)

Democritus functions<sup>[1]</sup> for working with and using dates and times.

[1] Democritus functions are <i>simple, effective, modular, well-tested, and well-documented</i> Python functions.

We use `d8s` as an abbreviation for `democritus` (you can read more about this [here](https://github.com/democritus-project/roadmap#what-is-d8s)).

## Functions

  - ```python
    def date_string_to_strftime_format(date_string):
        """Predict the strftime format from the given date_string."""
    ```
  - ```python
    def date_parse(date, *, convert_to_current_timezone: bool = False):
        """Parse the given date (can parse dates in most formats) (returns a datetime object)."""
    ```
  - ```python
    def date_now(*, convert_to_current_timezone: bool = False, utc: bool = False):
        """Get the current date.
    
    If convert_to_current_timezone is True, convert the date to the current timezone.
    If utc is True, convert the date to UTC."""
    ```
  - ```python
    def date_parse_first_argument(func):
        """."""
    ```
  - ```python
    def date_2_string(date, date_format_string: str):
        """."""
    ```
  - ```python
    def date_hour(date):
        """Find the hour from the given date."""
    ```
  - ```python
    def date_minute(date):
        """Find the minute from the given date."""
    ```
  - ```python
    def date_second(date):
        """Find the second from the given date."""
    ```
  - ```python
    def date_day(date):
        """Find the day of the month from the given date."""
    ```
  - ```python
    def date_day_of_month(date):
        """Find the day of the month from the given date."""
    ```
  - ```python
    def date_month(date):
        """Find the month from the given date."""
    ```
  - ```python
    def date_year(date):
        """Find the year from the given date."""
    ```
  - ```python
    def date_convert_to_timezone(date, timezone_string):
        """Convert the given date to the given timezone_string.
    
    This will actually **convert** time given date; it will change the hour/day of the date to the given timezone)."""
    ```
  - ```python
    def date_make_timezone_aware(datetime_object, timezone_string=None):
        """Make the given datetime_object timezone aware.
    
    This function does NOT convert the datetime_object.
    It will never change the hour/day or any value of the datetime...
      it will simply make the given datetime timezone aware."""
    ```
  - ```python
    def time_delta_examples(n=10, *, time_deltas_as_strings: bool = True):
        """Return n time deltas."""
    ```
  - ```python
    def time_examples(n=10, *, times_as_strings: bool = True):
        """Return n times."""
    ```
  - ```python
    def date_examples(n=10, *, dates_as_strings: bool = True, date_string_format: str = None):
        """Return n dates."""
    ```
  - ```python
    def datetime_examples(n=10, *, datetimes_as_strings: bool = True, datetime_string_format: str = None):
        """Return n datetimes."""
    ```
  - ```python
    def time_struct_to_datetime(struct_time_object):
        """Convert a python time.struct_time object into a datetime object."""
    ```
  - ```python
    def date_read(date_string, *, convert_to_current_timezone: bool = False):
        """Read the given date (if possible)."""
    ```
  - ```python
    def epoch_time_now():
        """Get the current epoch time."""
    ```
  - ```python
    def is_date(possible_date_string):
        """Determine if the given possible_date_string can be processed as a date."""
    ```
  - ```python
    def time_now():
        """Return the current, epoch time."""
    ```
  - ```python
    def time_since(date):
        """Return a time of the time since the given date."""
    ```
  - ```python
    def time_until(date):
        """Return an English description of the time since the given date."""
    ```
  - ```python
    def time_since_slang(date):
        """Return an English description of the time since the given date."""
    ```
  - ```python
    def time_until_slang(date):
        """Return an English description of the time until the given date."""
    ```
  - ```python
    def date_to_utc(date):
        """Convert the given date to UTC. Assume that the given date is in the system's timezone and convert it to UTC."""
    ```
  - ```python
    def time_after(time_a, time_b=None) -> bool:
        """Check if one time is before the other."""
    ```
  - ```python
    def time_before(time_a, time_b=None) -> bool:
        """Check if one time is before the other."""
    ```
  - ```python
    def date_in_future(date) -> bool:
        """Return whether or not the given date is in the future."""
    ```
  - ```python
    def time_is() -> str:
        """Time and money spent in helping men to do more for themselves is far better than mere giving. -Henry Ford"""
    ```
  - ```python
    def date_to_iso(date, *, timezone_is_utc: bool = False, use_trailing_z: bool = False):
        """Return the ISO 8601 version of the given date as a string (see https://en.wikipedia.org/wiki/ISO_8601)."""
    ```
  - ```python
    def epoch_time_standardization(epoch_time):
        """Convert the given epoch time to an epoch time in seconds."""
    ```
  - ```python
    def epoch_to_date(epoch_time):
        """Convert the epoch_time into a datetime."""
    ```
  - ```python
    def date_day_of_week(date):
        """Return the day of the week on which the given date occurred."""
    ```
  - ```python
    def date_week_of_year(date, *, sunday_is_first_day_of_week: bool = False):
        """Find the week of the year for the given date. If no date is given, return the week of the current date."""
    ```
  - ```python
    def date_to_epoch(date):
        """Convert a datetime stamp to epoch time."""
    ```
  - ```python
    def chrome_timestamp_to_epoch(chrome_timestamp):
        """Convert the given Chrome timestamp to epoch time.
    
    For more information, see: https://stackoverflow.com/questions/20458406/what-is-the-format-of-chromes-timestamps."""
    ```
  - ```python
    def time_waste(n=3):
        """If time be of all things the most precious, wasting time must be the greatest prodigality. -Benjamin Franklin"""
    ```
  - ```python
    def time_as_float(time_string: str) -> float:
        """converts a given HH:MM time string to float"""
    ```

## Development

👋 &nbsp;If you want to get involved in this project, we have some short, helpful guides below:

- [contribute to this project 🥇][contributing]
- [test it 🧪][local-dev]
- [lint it 🧹][local-dev]
- [explore it 🔭][local-dev]

If you have any questions or there is anything we did not cover, please raise an issue and we'll be happy to help.

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and Floyd Hightower's [Python project template](https://github.com/fhightower-templates/python-project-template).

[contributing]: https://github.com/democritus-project/.github/blob/main/CONTRIBUTING.md#contributing-a-pr-
[local-dev]: https://github.com/democritus-project/.github/blob/main/CONTRIBUTING.md#local-development-
