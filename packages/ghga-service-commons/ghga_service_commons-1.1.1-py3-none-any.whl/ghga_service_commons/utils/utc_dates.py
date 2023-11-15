# Copyright 2021 - 2023 Universität Tübingen, DKFZ, EMBL, and Universität zu Köln
# for the German Human Genome-Phenome Archive (GHGA)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Utilities for ensuring the consistent use of the UTC timezone."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from pydantic import GetCoreSchemaHandler
from pydantic.type_adapter import TypeAdapter
from pydantic_core import CoreSchema, core_schema

__all__ = ["DateTimeUTC", "UTC", "assert_tz_is_utc", "now_as_utc"]

UTC = timezone.utc


class DateTimeUTC(datetime):
    """A pydantic type for values that should have an UTC timezone.

    This behaves exactly like the normal datetime type, but requires that the value
    has a timezone and converts the timezone to UTC if necessary.
    """

    @classmethod
    def construct(cls, *args, **kwargs) -> DateTimeUTC:
        """Construct a datetime with UTC timezone."""
        if kwargs.get("tzinfo") is None:
            kwargs["tzinfo"] = UTC
        return cls(*args, **kwargs)

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        """Provide the schema with validation function.

        Uses `core_schema.no_info_plain_validator_function` because `cls.validate` is
        the sole validator for `DateTimeUTC`.
        """
        return core_schema.no_info_after_validator_function(
            cls.validate, handler(datetime)
        )

    @classmethod
    def validate(cls, value: Any) -> datetime:
        """Validate the given value."""
        datetime_validator = TypeAdapter(datetime)
        date_value = datetime_validator.validate_python(value)
        if date_value.tzinfo is None:
            raise ValueError(f"Date-time value is missing a timezone: {value!r}")
        if date_value.tzinfo is not UTC:
            date_value = date_value.astimezone(UTC)
        return date_value


def assert_tz_is_utc() -> None:
    """Verify that the default timezone is set to UTC.

    Raise a Runtimeerror if the default timezone is set differently.
    """
    if datetime.now().astimezone().tzinfo != UTC:
        raise RuntimeError("System must be configured to use UTC.")


def now_as_utc() -> DateTimeUTC:
    """Return the current datetime with UTC timezone.

    Note: This is different from datetime.utcnow() which has no timezone.
    """
    return DateTimeUTC.now(UTC)
