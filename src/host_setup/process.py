from host_setup.video_dir import VideoDir
from host_setup.decorators import state_manager, logger
import subprocess
import os
from typing import Dict


class Process:
    def __init__(self, path: str, api: object):
        self.video = VideoDir(path)
        self.api = api
        self.run_process()

    @property
    def status(self):
        """get the status of a given entry
        """
        return self.api.get_task_status(self.video.name)

    def run_process(self):
        self.actions[self.status](self.video, self.api)

    @property
    def actions(self):
        return {
            -1: self.video_busy,
            0: self.create_entry,
            1: self.convert_media,
            2: self.rclone,
            3: self.delete,
        }

    @staticmethod
    def video_busy(video, api):
        # TODO place a timeout here
        return None

    @staticmethod
    @state_manager
    @logger
    def create_entry(video, api):
        """if there is no video in sqlite"""
        if video.valid_video:
            api.create_new_task(video.name, video.r_path)
            return True

    @staticmethod
    @state_manager
    @logger
    def convert_media(video, api):
        # TODO Try to run fmpgg at several settings to convert data
        for vid in video.video_files:
            old_file = os.path.join(video.path, vid)
            new_file = os.path.join(video.path, video.name)
            Process._convert_vid_ffmpeg(old_file, new_file)
            return True

    @staticmethod
    @logger
    def _convert_vid_ffmpeg(old_vid, new_vid):
        return subprocess.call(
            [
                "ffmpeg",
                f"-i {old_vid}",
                "-c:v",
                "libx264",
                "-crf 19",
                "-hide_banner",
                "-loglevel panic",
                "-preset fast",
                new_vid,
            ]
        )

    @staticmethod
    @state_manager
    @logger
    def rclone(video, api):
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
    def delete(video, api):
        print("starting a deletion of the file")
        os.remove(video.path)
