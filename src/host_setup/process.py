from host_setup.video_dir import VideoDir
from host_setup.decorators import state_manager, logger
import os


class Process:
    def __init__(self, path: str, api: object):
        self.video = VideoDir(path)
        self.api = api
        self.run_process()

    @property
    def status(self):
        """get the status of a given entry
        """
        status = self.api.get_task_status(self.video.name)
        print(status)
        return status

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
    @state_manager
    # @logger
    def create_entry(video, api):
        """if there is no video in sqlite"""
        if video.valid_video:
            print("creating entry")
            api.create_new_task(video.name, video.path)

    @staticmethod
    @state_manager
    def convert_video(video, api):
        # check if the current step is processing
        # if complete do something

        # if not
        print("starting a conversion to mp4")
        video_path = video.video_files
        # TODO Try to run fmpgg at several settings to convert data
        # "ffmpeg -i $file -c:v libx264 -crf 19 -hide_banner -loglevel panic -preset fast $newFile"
        print(video.path)
        return None

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


# def find_downloads(path, api):
#     # Set the directory you want to start from

#     for sub_dir in os.listdir(path):
#         if sub_dir not in EXCLUDE:
#             given_dir = os.path.join(path, sub_dir)
#             AttemptInsert(given_dir, api)
