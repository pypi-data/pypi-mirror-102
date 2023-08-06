#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta, timezone


def string_to_datetime(datestring):
    date = datetime.strptime(datestring, "%Y-%m-%dT%H:%M:%S%z")
    return date


def datetime_to_string(date):
    return date.strftime("%Y-%m-%dT%H:%M:%S%z")


def now():
    return datetime.now(tz=timezone.utc)


def now_string():
    return datetime_to_string(now())


def older_than_n_days(datestring, ndays):
    date = string_to_datetime(datestring)
    delta = now() - date
    return delta > timedelta(days=ndays)

