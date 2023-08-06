#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import platform
import pytest
import aldemsubs.utils as utils
from aldemsubs.aldemsubs import AlDemSubsMain, AlreadySubscribed
from aldemsubs.feed import EmptyFeed


if os.name == 'posix':
    TEST_CFG_PATH = "./testconfig.ini"
elif platform.system() == 'Windows':
    TEST_CFG_PATH = os.path.expandvars("%cd%\\testconfig_windows.ini")


def test_subscribe():

    try:
        ads = AlDemSubsMain(TEST_CFG_PATH)

        chids = ["UCGwu0nbY2wSkW8N-cghnLpA",
                 "UCXuqSBlHAE6Xw-yeJA0Tunw",
                 "UCO7fujFV_MuxTM0TuZrnE6Q"]

        for chid in chids:
            ads.subscribe(chid)
            assert chid in ads.channel_ids

        # subscribe to channel already subscribed to
        try:
            ads.subscribe("UCGwu0nbY2wSkW8N-cghnLpA")
            assert False, "AlreadySubscribed should have been raised"
        except AlreadySubscribed:
            pass

        # subscribe to invalid channel id
        try:
            ads.subscribe("shd")
            assert False, "EmptyFeed should be raised"
        except EmptyFeed:
            pass

        # delete object and recreate to test persistance of db
        del ads
        ads = AlDemSubsMain(TEST_CFG_PATH)

        for chid in chids:
            assert chid in ads.channel_ids

    finally:
        if os.path.exists(ads.config["db_file_path"]):
            os.remove(ads.config["db_file_path"])


def test_update_subscriptions():

    try:
        ads = AlDemSubsMain(TEST_CFG_PATH)
        chids = ["UCGwu0nbY2wSkW8N-cghnLpA",
                 "UCXuqSBlHAE6Xw-yeJA0Tunw",
                 "UCO7fujFV_MuxTM0TuZrnE6Q"]
        for chid in chids:
            ads.subscribe(chid)

        deleted_videos = ads.video_ids[:13]
        ads.db.delete_videos(*deleted_videos)
        ads.update_buffer()

        assert all(video not in ads.video_ids for video in deleted_videos)

        ads.update_subscriptions()

        assert all(video in ads.video_ids for video in deleted_videos)

    finally:
        if os.path.exists(ads.config["db_file_path"]):
            os.remove(ads.config["db_file_path"])


def test_unsubscribe():

    try:
        ads = AlDemSubsMain(TEST_CFG_PATH)
        chids = ["UCGwu0nbY2wSkW8N-cghnLpA",
                 "UCXuqSBlHAE6Xw-yeJA0Tunw",
                 "UCO7fujFV_MuxTM0TuZrnE6Q"]

        for chid in chids:
            ads.subscribe(chid)

        unsubscribed = chids[1]
        print(unsubscribed)
        ads.unsubscribe(unsubscribed)

        assert unsubscribed not in ads.channel_ids
        assert unsubscribed not in ads.db.get_channel_ids()
        assert chids[0] in ads.channel_ids
        assert chids[0] in ads.db.get_channel_ids()

    finally:
        if os.path.exists(ads.config["db_file_path"]):
            os.remove(ads.config["db_file_path"])


@pytest.mark.skip(reason="takes too long to test every time")
def test_download_new_videos():

    try:
        ads = AlDemSubsMain(TEST_CFG_PATH)
        chids = ["UCGwu0nbY2wSkW8N-cghnLpA",
                 "UCo8bcnLyZH8tBIH9V1mLgqQ"]
        for chid in chids:
            ads.subscribe(chid)

        ads.update_subscriptions()

        dl_info = ads.db.get_download_info_new_videos()
        video_ids = [video["video_id"] for video in dl_info]
        print(video_ids)
        ads.download_new_videos()

        ads.db.cursor.execute("""
            SELECT video_id, file_path FROM videos WHERE downloaded=1
        """)
        results = ads.db.cursor.fetchall()
        downloaded_video_ids = [r["video_id"] for r in results]
        downloaded_file_paths = [r["file_path"] for r in results]
        print(downloaded_file_paths)

        assert all(video_id in downloaded_video_ids for video_id in video_ids)
        assert all(os.path.exists(fp) for fp in downloaded_file_paths)
        videos_per_channel = ads.config['after_subscribe_download_n_videos']
        assert len(downloaded_file_paths) <= videos_per_channel*len(chids)

    finally:
        if os.path.exists(ads.config["db_file_path"]):
            os.remove(ads.config["db_file_path"])


@pytest.mark.skip(reason="takes too long to test every time")
def test_delete_old_videos():

    try:
        ads = AlDemSubsMain(TEST_CFG_PATH)
        # youtube channel that hasn't seen any uploads in a while
        chids = ["UCGwu0nbY2wSkW8N-cghnLpA",
                 "UCo8bcnLyZH8tBIH9V1mLgqQ"]
        for chid in chids:
            ads.subscribe(chid)

        ads.update_subscriptions()
        ads.download_new_videos()

        downloaded = ads.db.get_downloaded_videos()
        downloaded_ids = [video["video_id"] for video in downloaded]
        expired = downloaded[2:]
        expired_ids = [video["video_id"] for video in expired]
        expired_paths = [video['file_path'] for video in expired]

        for fp in expired_paths:
            assert os.path.isfile(fp)

        dl_dates = [
            ('2018-01-11T16:37:24+00:00', vid)
            for vid in expired_ids]
        ads.db.cursor.executemany("""
            UPDATE videos SET download_date=? WHERE video_id=?
        """, dl_dates)
        ads.db.commit()

        ads.delete_old_videos()

        for fp in expired_paths:
            assert not os.path.isfile(fp)

        downloaded_after = ads.db.get_downloaded_videos()
        downloaded_ids_after = [video["video_id"] for video in downloaded_after]
        downloaded_paths_after = [video['file_path'] for video in downloaded_after]

        assert downloaded_after  # checks for non-empty list
        for fp in downloaded_paths_after:
            assert os.path.isfile(fp)
        assert all(vid not in downloaded_ids_after for vid in expired_ids)

    finally:
        if os.path.exists(ads.config["db_file_path"]):
            os.remove(ads.config["db_file_path"])




