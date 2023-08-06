#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from glob import glob
from youtube_dl import YoutubeDL
from youtube_dl.utils import DownloadError
import aldemsubs.utils as utils
from aldemsubs.feed import FeedHandler
from aldemsubs.db import DBHandler
from aldemsubs.config import ConfigHandler


class AlDemSubsMain():

    def __init__(self, config_file_path):
        self.config = ConfigHandler(config_file_path)
        db_dir = os.path.dirname(self.config['db_file_path'])
        if not os.path.exists(db_dir):
            os.makedirs(os.path.dirname(self.config['db_file_path']))
        self.db = DBHandler(self.config["db_file_path"])
        self.update_buffer()

    def update_buffer(self):
        """
        Preloads the video- and channel-ids from the database to reduce number
        of reads from disk.
        """
        self.channel_ids = self.db.get_channel_ids()
        self.video_ids = self.db.get_video_ids()

    def subscribe(self, channel_id):
        if channel_id in self.channel_ids:
            raise AlreadySubscribed(channel_id)
        feed = FeedHandler(channel_id)
        video_list = feed.get_video_list()
        n_videos_to_download = self.config["after_subscribe_download_n_videos"]
        if n_videos_to_download >= 0:
            self.only_n_most_recent_marked_new(video_list, n_videos_to_download)
        channel_dict = feed.get_channel_dict()
        self.db.add_channel(channel_dict)
        self.db.add_videos(*video_list)
        self.update_buffer()

    @staticmethod
    def only_n_most_recent_marked_new(video_list, n):
        if len(video_list) > n:
            for video in video_list[n:]:
                video['new'] = False

    def list_channels(self):
        channel_list = self.db.get_channel_list()
        for ch in channel_list:
            print(f"{ch['channel_id']}\t{ch['title']}")

    def unsubscribe(self, channel_id):
        self.db.delete_channel(channel_id)
        self.update_buffer()

    def update_subscriptions(self):
        new_videos = []
        for chid in self.channel_ids:
            feed = FeedHandler(chid)
            video_list = self.filter_new_videos(feed.get_video_list())
            new_videos.extend(video_list)
        if new_videos:
            self.db.add_videos(*new_videos)
            self.update_buffer()
        self.unset_new_flag()

    def filter_new_videos(self, video_list):

        new_videos = []

        # exploits that videos in feed are sorted by date, newest first
        # => if one video is in the database, the remaining don't need to be
        # checked

        for video in video_list:
            if video["video_id"] in self.video_ids:
                break
            new_videos.append(video)

        return new_videos

    def unset_new_flag(self):
        new_videos = self.db.get_new_videos()
        old_videos = []
        for video in new_videos:
            added_date = video["added_date"]
            ndays = self.config["mark_videos_old_after"]
            if utils.older_than_n_days(added_date, ndays):
                old_videos.append(video["video_id"])
        self.db.set_video_new_flag(False, *old_videos)

    def download_new_videos(self):
        dl_info = self.db.get_download_info_new_videos()
        for video in dl_info:
            self.download_video(video)

    def download_video(self, dl_info):

        pubdate = utils.string_to_datetime(dl_info['published_date'])

        # replace slashes and percent signs in video title
        title = ''.join(dl_info["title"].split('/'))
        title = 'prc'.join(title.split('%'))

        title = f'{pubdate.year}-{pubdate.month:02}-{pubdate.day:02} {title}'

        # replace slashes and percent signs in channel title
        channel_title = ''.join(dl_info["channel_title"].split('/'))
        channel_title = 'prc'.join(channel_title.split('%'))

        url = dl_info["url"]
        dl_path = self.config["download_path"]
        full_path = os.path.realpath(
                os.path.join(dl_path, channel_title, title))
        opts = {"outtmpl": f"{full_path}.%(ext)s"}

        with YoutubeDL(opts) as ydl:
            try:
                ydl.download([url])
            except DownloadError:
                print(f'ERROR: Could not download {url}')
                return

            # find actual file name to store in db (extension varies)
            file_name_matches = glob(f"{full_path}.*")
            if not file_name_matches:
                raise FileNotFoundError(f'No matches found for "{full_path}.*"')
            file_path = file_name_matches[0]

        self.db.mark_video_downloaded(dl_info["video_id"], file_path)

    def delete_old_videos(self):
        videos = self.db.get_downloaded_videos()
        for video in videos:
            dl_date = video["download_date"]
            ndays = self.config["delete_downloads_after"]
            video_is_old = utils.older_than_n_days(dl_date, ndays)
            file_exists = os.path.isfile(video["file_path"])
            if video_is_old and file_exists:
                os.remove(video["file_path"])
                self.db.mark_video_deleted(video["video_id"])
            elif video_is_old and not file_exists:
                self.db.mark_video_deleted(video["video_id"])


class AlreadySubscribed(Exception):
    pass
