from host_setup.decorators import state_manager, logger
from host_setup.media.base_media import BaseMedia
import subprocess
import os
from typing import Dict


class Process:
    def __init__(self, media: BaseMedia, api: object):
        self.media = media
        self.api = api
        self.run_process()

    @property
    def status(self):
        """get the status of a given entry
        """
        return self.api.get_task_status(self.media.name)

    def run_process(self):
        self.actions[self.status](self.media, self.api)

    @property
    def actions(self):
        return {
            0: self.create_entry,
            1: self.convert_media,
            2: self.rclone,
            3: self.delete,
        }

    @staticmethod
    @state_manager
    @logger
    def create_entry(media, api):
        """if there is no media in sqlite"""
        if media.valid_media:
            api.create_new_task(media.name, media.r_path)
            return True

    @staticmethod
    @state_manager
    @logger
    def convert_media(media, api):
        media.process_media()

    @staticmethod
    @state_manager
    @logger
    def rclone(media, api):
        # move this to async
        print("starting as sync to s3")
        subprocess.call(
            [
                os.environ["RCLONE"],
                "move",
                "--include mp4,srt",
                "--delete-empty-src-dirs" "FILES wasab:wasab",
            ]
        )

    @staticmethod
    @state_manager
    @logger
    def delete(media, api):
        print("starting a deletion of the file")
        os.remove(media.path)
