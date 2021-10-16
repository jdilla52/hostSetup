import os
import subprocess
from host_setup.decorators import logger
from host_setup.media.base_media import BaseMedia


class TV(BaseMedia):
    def process_media(self):
        # conversion process + settings
        if self.needs_convert:
            for vid in self.to_convert_files:
                old_file = os.path.join(self.path, vid)
                new_file = os.path.join(self.path, self.name)
                self._convert_vid_ffmpeg(old_file, new_file)
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
