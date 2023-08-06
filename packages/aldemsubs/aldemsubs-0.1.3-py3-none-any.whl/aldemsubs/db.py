#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import aldemsubs.utils as utils


class DBHandler():

    def __init__(self, filepath):
        self.filepath = filepath
        self.db = None
        self.cursor = None
        self.connect()
        self.initialize_database()

    def connect(self):
        if not self.is_connected():
            self.db = sqlite3.connect(self.filepath)
            self.db.row_factory = sqlite3.Row
            self.cursor = self.db.cursor()

    def is_connected(self):
        return not (self.db is None or self.cursor is None)

    def disconnect(self):

        if self.is_connected():
            self.db.close()
            self.db = None
            self.cursor = None

    def initialize_database(self):
        self.cursor.execute("PRAGMA foreign_keys=ON")
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS
                channels(
                    channel_id text primary key,
                    title text,
                    url text
                );"""
        )
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS
                videos(
                    video_id text primary key,
                    channel_id text REFERENCES channels(channel_id),
                    title text,
                    url text,
                    published_date text,
                    added_date text,
                    download_date text,
                    downloaded integer,
                    file_path text,
                    new integer
                );
        """)
        self.cursor.execute("""
            CREATE VIEW IF NOT EXISTS download_info AS
            SELECT
                v.video_id, v.title, v.url, v.new, v.downloaded, v.channel_id,
                v.published_date, c.title AS channel_title
            FROM videos AS v
            INNER JOIN channels AS c
            USING(channel_id)
        """)

        self.commit()

    def commit(self):
        self.db.commit()

    def add_channel(self, channel_dict):
        self.cursor.execute("""
            INSERT INTO channels VALUES (
                :channel_id,
                :title,
                :url)""", channel_dict)
        self.commit()

    def channel_get_video_ids(self, *channel_ids):
        self.cursor.executemany(
            "SELECT video_id FROM videos WHERE channel_id == ?",
            channel_ids)
        results = self.cursor.fetchall()
        return [row[0] for row in results]

    def add_videos(self, *video_dicts):
        self.cursor.executemany(
            """INSERT INTO videos VALUES (
                :video_id,
                :channel_id,
                :title,
                :url,
                :published_date,
                :added_date,
                :download_date,
                :downloaded,
                :file_path,
                :new
            )""", video_dicts
        )
        self.commit()

    def get_channel_list(self):
        self.cursor.execute("""
            SELECT channel_id, title FROM channels
        """)
        return self.cursor.fetchall()

    def channel_id_in_channels(self, channel_id):
        self.cursor.execute("""
            SELECT count(channel_id) FROM channels WHERE channel_id=?
        """, channel_id)
        result = self.cursor.fetch()
        return result[0] == 1

    def get_channel_ids(self):
        self.cursor.execute("""
            SELECT channel_id FROM channels
        """)
        results = self.cursor.fetchall()
        return [row["channel_id"] for row in results]

    def delete_channel(self, channel_id):
        self.cursor.execute("""
            DELETE FROM videos WHERE channel_id=?
        """, (channel_id,))

        self.cursor.execute("""
            DELETE FROM channels WHERE channel_id=?
        """, (channel_id,))

        self.commit()

    def get_video_ids(self):
        self.cursor.execute("""
            SELECT video_id FROM videos ORDER BY published_date DESC
        """)
        results = self.cursor.fetchall()
        return [row["video_id"] for row in results]

    def get_new_videos(self):
        self.cursor.execute("""
            SELECT * FROM videos WHERE new=1
        """)
        return self.cursor.fetchall()

    def set_video_new_flag(self, value, *video_ids):
        rows = [(value, video_id) for video_id in video_ids]
        self.cursor.executemany("""
            UPDATE videos SET new=? WHERE video_id=?
        """, rows)
        self.commit()

    def get_download_info(self):
        self.cursor.execute("""
            SELECT video_id, url, title, channel_title FROM download_info
            WHERE downloaded=0
        """)
        return self.cursor.fetchall()

    def get_download_info_new_videos(self):
        self.cursor.execute("""
            SELECT video_id, url, title, published_date, channel_title
            FROM download_info
            WHERE new=1 AND downloaded=0
        """)
        return self.cursor.fetchall()

    def get_downloaded_videos(self):
        self.cursor.execute("""
            SELECT * FROM videos WHERE downloaded=1
        """)
        return self.cursor.fetchall()

    def mark_video_deleted(self, video_id):
        self.cursor.execute("""
            UPDATE videos SET downloaded=0, new=0 WHERE video_id=?
        """, (video_id,))

    def mark_video_downloaded(self, video_id, file_path):
        dl_date = utils.now_string()
        self.cursor.execute("""
            UPDATE videos
            SET file_path=?, downloaded=1, download_date=?
            WHERE video_id=?
        """, (file_path, dl_date, video_id))
        self.commit()

    def delete_videos(self, *video_ids):
        self.cursor.executemany("""
            DELETE FROM videos WHERE video_id=?
        """, ((video_id,) for video_id in video_ids))
        self.commit()

    def __del__(self):
        self.disconnect()
