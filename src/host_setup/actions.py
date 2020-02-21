import os
from pathlib import Path
from host_setup.datab import DataB
from pathlib import Path
from glob import glob
from typing import List

EXCLUDE = ["vpn"]
VALID_VIDEO = [".mp4", ".avi"]
VALID_OTHER = [".srt"]


class VideoDir:
    def __init__(self, path: str):
        self.path = path

    @staticmethod
    def _get_files(path: str, file_types: List[str]) -> List[str]:
        return [p for p in Path(path).rglob("*") if p.suffix in file_types]

    @property
    def valid_video(self):
        """checks for a valid video file in a given directory
        Returns:
            valid -- a true or false representing if a video file is present
        """
        potentials = self.video_files

        if len(potentials) > 0:
            return True
        else:
            return False  # build helpers into class

    @property
    def video_files(self):
        return self._get_files(self.path, VALID_VIDEO)

    @property
    def subtitles(self):
        return self._get_files(self.path, VALID_OTHER)


class ScanDir:
    def __init__(self, path: str, api: object):
        self.path = Path
        self.api = api

    # def scan_dir(self):
    #     # perform these in a lazy or non-blocking manner
    #     for dir in self.path:
    #         Process(dir)


# def task_state_manager(func):
#     def run_task():
def state_manager(api):
    def wrap(f):
        def action_f(*args):
            print("Inside wrapped_f()")
            print("Decorator arguments:", api)
            f(*args)
            print("After f(*args)")

        return action_f

    return wrap


class Process:
    def __init__(self, path: str, api: object):
        print(path)
        self.video = VideoDir(path)
        self.api = api
        self.run_process()

    @property
    def status(self):
        """get the status of a given entry
        """
        task = self.api.select_task_by_name("name", self.video.path)

        if len(task) == 0:
            print("this video hasn't be started")
            return 0
        elif len(task) == 1:
            return task[0][3]
        else:
            # TODO find something smart to do
            print(task)
            print("there's a problem we should kill one")
            return task[0][3]

    def run_process(self):
        print("rnn")
        self.actions[self.status](self.video, self.api)

    @property
    def actions(self):
        return {
            -1: self.video_busy,
            0: self.create_entry,
            1: self.convert_video,
            2: self.rclone,
            3: self.delete,
        }

    @staticmethod
    def video_busy(video, api):
        return None

    @staticmethod
    def create_entry(video, api):
        """if there is no video in sqlite"""
        print("creating entry")
        if video.valid_video:
            api.create_new_task(video.path)

    @staticmethod
    def convert_video(video, api):
        # check if the current step is processing
        # if complete do something

        # if not
        print("starting a conversion to mp4")
        video_path = video.video_files
        # TODO Try to run fmpgg at several settings to convert data
        # "ffmpeg -i $file -c:v libx264 -crf 19 -hide_banner -loglevel panic -preset fast $newFile"
        print(video.path)

    @staticmethod
    def rclone(video, api):

        print("starting as sync to s3")
        # "$RCLONE move --include "*.{mp4,srt}" --delete-empty-src-dirs $FILES wasab:wasab"
        pass

    @staticmethod
    def delete(video, api):
        print("starting a deletion of the file")
        os.remove(video.path)

    @staticmethod
    def processing(video, api):
        print("something is processing")
        # check for output of process if complete push to next status
        pass


def find_downloads(path, api):
    # Set the directory you want to start from

    for sub_dir in os.listdir(path):
        if sub_dir not in EXCLUDE:
            given_dir = os.path.join(path, sub_dir)
            AttemptInsert(given_dir, api)
