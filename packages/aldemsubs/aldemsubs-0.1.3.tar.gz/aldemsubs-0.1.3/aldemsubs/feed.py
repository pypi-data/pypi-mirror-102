#!/usr/bin/env python
# -*- coding: utf-8 -*-

import feedparser
import aldemsubs.utils as utils
#from aldemsubs.types import VideoDict


class FeedHandler():

    def __init__(self, channel_id):
        feedlink = self.feed_link_from_channel_id(channel_id)
        self.feed = self.feed_from_link(feedlink)
        if self.feed_is_empty(self.feed):
            raise EmptyFeed("Invalid link or empty feed.")
        self.current_date = utils.now_string()


    @staticmethod
    def feed_link_from_channel_id(channel_id):
        return f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"


    @staticmethod
    def feed_is_empty(feed):
        return not feed.entries


    @staticmethod
    def feed_from_link(feedlink):
        feed = feedparser.parse(feedlink)
        return feed


    def get_channel_title(self):
        return self.feed.feed.title


    def get_channel_id(self):
        return self.feed.feed.yt_channelid


    def get_channel_url(self):
        return self.feed.feed.href


    def get_channel_rss(self):
        return self.feed.href


    def get_channel_dict(self):

        channel_dict = dict(
            channel_id = self.get_channel_id(),
            title = self.get_channel_title(),
            url = self.get_channel_url(),
        )

        return channel_dict


    @staticmethod
    def get_video_title(feed_entry):
        return feed_entry.title


    @staticmethod
    def get_video_id(feed_entry):
        return feed_entry.yt_videoid


    @staticmethod
    def get_video_published_date(feed_entry):
        return feed_entry.published


    @staticmethod
    def get_video_url(feed_entry):
        return feed_entry.link


    def get_video_dict(self, feed_entry):

        video_dict = dict(
            video_id = self.get_video_id(feed_entry),
            channel_id = self.get_channel_id(),
            title = self.get_video_title(feed_entry),
            url = self.get_video_url(feed_entry),
            published_date = self.get_video_published_date(feed_entry),
            added_date = self.current_date,
            download_date = None,
            downloaded = False,
            file_path = None,
            new = True,
        )

        return video_dict


    def get_video_list(self):
        return [self.get_video_dict(entry) for entry in self.feed.entries]


class EmptyFeed(Exception):
    pass
