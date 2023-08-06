#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aldemsubs.feed import FeedHandler
import tempfile
import os
from datetime import (
    datetime,
    timezone,
)


def test_feedlink_from_channel_id():
    chid = "abcde"
    link = FeedHandler.feed_link_from_channel_id(chid)
    assert link == f"https://www.youtube.com/feeds/videos.xml?channel_id={chid}"


def test_feed_handler_init():
 
    chid = "invalid"

    # Exception should be raised on invalid channel id
    try:
        feed = FeedHandler(chid)
        assert False, "No exception was raised on invalid channel id"
    except Exception:
        assert True

    chid = "UCXuqSBlHAE6Xw-yeJA0Tunw" #Linus Tech Tips

    try:
        feed = FeedHandler(chid)
    except Exception:
        assert False, "Exception raised on valid channel id"


def test_create_channel_video_dict():
    """
    Very basic test for create_video_dict() and create_channel_dict().
    Only purpose is to see when they throw exceptions.
    """
    
    chid = "UCXuqSBlHAE6Xw-yeJA0Tunw" #Linus Tech Tips
    feed = FeedHandler(chid)

    feed.get_channel_dict()
    feed.get_video_dict(feed.feed.entries[1])
