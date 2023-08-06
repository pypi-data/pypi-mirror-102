#!/usr/bin/env python
# -*- coding: utf-8 -*-

import aldemsubs.utils as utils


def test_date_conversion():

    datestring = "2021-01-02T05:06:02+0000"

    date = utils.string_to_datetime(datestring)

    assert date.day == 2
    assert date.month == 1
    assert date.year == 2021

    datestring2 = "2021-01-02T05:06:02+00:00"
    date2 = utils.string_to_datetime(datestring2)

    assert date == date2

    back_to_string = utils.datetime_to_string(date)

    assert datestring == back_to_string

    try:
        date = utils.string_to_datetime("dhkfahd9889da7s")
        assert False, "No exception was raised on invalid input"
    except ValueError:
        pass

    try:
        date = utils.string_to_datetime("2021-01-0205:06:02+00:00")
        assert False, "No exception was raised on invalid input"
    except ValueError:
        pass

    assert utils.older_than_n_days(datestring, 5)

    date = utils.datetime.now(tz=utils.timezone.utc) - utils.timedelta(days=4)
    datestring = utils.datetime_to_string(date)

    assert not utils.older_than_n_days(datestring, 5)
