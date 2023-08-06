#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tempfile
import os
import sqlite3
from aldemsubs.db import DBHandler
from aldemsubs.feed import FeedHandler


TEMP_DB_FILE_PATH = os.path.join(tempfile.gettempdir(), "aldemsubstemp.db")


def create_and_delete_temp_db(f):

    def wrapper():

        if os.path.exists(TEMP_DB_FILE_PATH):
            os.remove(TEMP_DB_FILE_PATH)

        db = DBHandler(TEMP_DB_FILE_PATH)

        try:
            f(db)
        finally:
            del db
            if os.path.exists(TEMP_DB_FILE_PATH):
                os.remove(TEMP_DB_FILE_PATH)


def test_initialize_db():

    if os.path.exists(TEMP_DB_FILE_PATH):
        os.remove(TEMP_DB_FILE_PATH)

    db = DBHandler(TEMP_DB_FILE_PATH)

    try:

        db.cursor.execute("SELECT * FROM videos WHERE video_id=\"abc\"")
        result = db.cursor.fetchall()
        assert not result

        assert os.path.isfile(TEMP_DB_FILE_PATH)

        db.cursor.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='channels';")
        assert db.cursor.fetchone()[0] == 1
        db.cursor.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='videos';")
        assert db.cursor.fetchone()[0] == 1
        db.cursor.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='dfkjhdskjh';")
        assert db.cursor.fetchone()[0] == 0

    finally:
        del db
        if os.path.exists(TEMP_DB_FILE_PATH):
            os.remove(TEMP_DB_FILE_PATH)


def test_write_channel_dict_to_db():

    if os.path.exists(TEMP_DB_FILE_PATH):
        os.remove(TEMP_DB_FILE_PATH)

    db = DBHandler(TEMP_DB_FILE_PATH)

    try:

        chid = "UCXuqSBlHAE6Xw-yeJA0Tunw"
        feed = FeedHandler(chid)
        channel_dict = feed.get_channel_dict()
        db.add_channel(channel_dict)

        db.cursor.execute("SELECT count(*) FROM channels WHERE channel_id='UCXuqSBlHAE6Xw-yeJA0Tunw';")
        assert db.cursor.fetchone()[0] == 1
        db.cursor.execute("SELECT count(*) FROM channels WHERE channel_id='UCXuqSBTunw';")
        assert db.cursor.fetchone()[0] == 0

        del db
        db = DBHandler(TEMP_DB_FILE_PATH)
        db.cursor.execute("SELECT count(*) FROM channels WHERE channel_id='UCXuqSBlHAE6Xw-yeJA0Tunw';")
        assert db.cursor.fetchone()[0] == 1
        db.cursor.execute("SELECT count(*) FROM channels WHERE channel_id!='UCXuqSBlHAE6Xw-yeJA0Tunw';")
        assert db.cursor.fetchone()[0] == 0
        
    finally:
        del db
        if os.path.exists(TEMP_DB_FILE_PATH):
            os.remove(TEMP_DB_FILE_PATH)


def test_write_video_dict_to_db():

    if os.path.exists(TEMP_DB_FILE_PATH):
        os.remove(TEMP_DB_FILE_PATH)

    db = DBHandler(TEMP_DB_FILE_PATH)

    try:

        chid = "UCXuqSBlHAE6Xw-yeJA0Tunw"
        feed = FeedHandler(chid)
        channel_dict = feed.get_channel_dict()

        video_dict = feed.get_video_dict(feed.feed.entries[0])

        # try to add video to database without adding channel first
        # should raise exception
        try:
            db.add_videos(video_dict)
        except sqlite3.IntegrityError:
            assert True

        db.add_channel(channel_dict)
        db.add_videos(video_dict)
        db.cursor.execute("SELECT count(*) FROM videos WHERE channel_id='UCXuqSBlHAE6Xw-yeJA0Tunw';")
        assert db.cursor.fetchone()[0] == 1
        db.cursor.execute("SELECT count(*) FROM videos WHERE channel_id!='UCXuqSBlHAE6Xw-yeJA0Tunw';")
        assert db.cursor.fetchone()[0] == 0

    finally:
        del db
        if os.path.exists(TEMP_DB_FILE_PATH):
            os.remove(TEMP_DB_FILE_PATH)


def setup_test_db():

    if os.path.exists(TEMP_DB_FILE_PATH):
        os.remove(TEMP_DB_FILE_PATH)

    db = DBHandler(TEMP_DB_FILE_PATH)

    chids = [
        "UCGwu0nbY2wSkW8N-cghnLpA",
        "UCXuqSBlHAE6Xw-yeJA0Tunw",
        "UCO7fujFV_MuxTM0TuZrnE6Q"
    ]
    feeds = [FeedHandler(chid) for chid in chids]

    video_list = []
    for feed in feeds:
        db.add_channel(feed.get_channel_dict())
        video_list.extend(feed.get_video_list())

    db.add_videos(*video_list)

    return db


def test_get_download_info():

    db = setup_test_db()

    dl_info = db.get_download_info_new_videos()

    try:

        for video in dl_info:
            video["video_id"]
            video["url"]
            video["channel_title"]
            video["title"]

        dl_info = db.get_download_info()

        for video in dl_info:
            video["video_id"]
            video["url"]
            video["channel_title"]
            video["title"]

    finally:
        del db
        if os.path.exists(TEMP_DB_FILE_PATH):
            os.remove(TEMP_DB_FILE_PATH)


def test_get_video_ids_channel_ids():

    db = setup_test_db()

    try:
        chids = db.get_channel_ids()
        video_ids = db.get_video_ids()

        assert isinstance(chids[1], str)
        assert isinstance(video_ids[1], str)

    finally:
        del db
        if os.path.exists(TEMP_DB_FILE_PATH):
            os.remove(TEMP_DB_FILE_PATH)


def test_mark_video_new_downloaded():

    db = setup_test_db()

    try:

        dl_info = db.get_download_info_new_videos()

        removed_new_flag = dl_info[0:20]
        removed_new_flag = [video["video_id"] for video in removed_new_flag]

        db.set_video_new_flag(False, *removed_new_flag)

        dl_info_new = db.get_download_info_new_videos()
        video_ids_new_videos = [video["video_id"] for video in dl_info_new]

        assert all([rem not in video_ids_new_videos for rem in removed_new_flag])

        marked_downloaded = dl_info[15:35]
        marked_downloaded = [video["video_id"] for video in marked_downloaded]

        for video_id in marked_downloaded:
            db.mark_video_downloaded(video_id, "test")

        dl_info_new = db.get_download_info_new_videos()
        video_ids_new_videos = [video["video_id"] for video in dl_info_new]
        
        assert all([dl not in video_ids_new_videos for dl in marked_downloaded])

        downloaded_videos = db.get_downloaded_videos()
        downloaded_videos = [video["video_id"] for video in downloaded_videos]

        assert all([dl in downloaded_videos for dl in marked_downloaded])
        
        db.set_video_new_flag(True, *marked_downloaded)
        for video_id in marked_downloaded:
            db.mark_video_deleted(video_id)

        dl_info = db.get_download_info()
        video_ids = [video["video_id"] for video in dl_info]
        dl_info_new = db.get_download_info_new_videos()
        video_ids_new = [video["video_id"] for video in dl_info_new]

        assert all([dl in video_ids for dl in marked_downloaded])
        assert all([dl not in video_ids_new for dl in marked_downloaded])

    finally:
        del db
        if os.path.exists(TEMP_DB_FILE_PATH):
            os.remove(TEMP_DB_FILE_PATH)

