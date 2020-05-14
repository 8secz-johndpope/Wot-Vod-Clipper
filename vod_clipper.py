#!/usr/bin/python

# Libraries
import ffmpeg
from datetime import datetime

_NIVIDIA_ACCELERATOR = 'cuvid'
_NIVIDIA_DECODER = 'h264_cuvid'
_NIVIDIA_ENCODER = 'h264_nvenc'
_FFMPEG_COPY_ENCODER = 'copy'


class VodClipper:

    def __init__(self):
        pass

    def clip(self, in_file: str, out_file: str, start_s: int = 0, duration_s: int = 60):
        self.validate(in_file, out_file, start_s, duration_s)

        process = (
            ffmpeg
                .input(in_file, ss=start_s, t=duration_s)
                .output(out_file, c='copy')
        )
        process.run(quiet=True, overwrite_output=True)
        pass

    def clip_with_nvidia(self, in_file: str, out_file: str, start_s: int = 0, duration_s: int = 60):
        self.validate(in_file, out_file, start_s, duration_s)

        output_params = {
            'vcodec': _NIVIDIA_ENCODER,
            'acodec': _FFMPEG_COPY_ENCODER,
            'preset': 'medium',
            'b:v': '2850k',
            'bufsize': '6M',
            'minrate': '2M',
            'maxrate': '3M',
            'profile:v': 'high',
            'bf': 3,
            'temporal-aq': 1,
            'rc-lookahead': 20,
            'vsync': 0
        }

        process = (
            ffmpeg
                .input(in_file, ss=start_s, t=duration_s,
                       vsync=0, vcodec=_NIVIDIA_DECODER, hwaccel=_NIVIDIA_ACCELERATOR, hwaccel_output_format='cuda')
                .output(out_file, **output_params)
        )
        start_time = datetime.now()
        process.run(quiet=True, overwrite_output=True)
        print('Finished in {}s'.format(datetime.now() - start_time))
        pass

    def validate(self, in_file, out_file, start_s, duration_s):
        self.validate_paths(in_file, out_file)
        self.validate_time(start_s, duration_s)
        pass

    @staticmethod
    def validate_time(start_s, duration_s):
        if start_s < 0:
            raise Exception("Please provide valid start time")

        if duration_s < 0:
            raise Exception("Please provide valid end time or duration")
        pass

    @staticmethod
    def validate_paths(in_file, out_file):
        if not in_file:
            raise Exception("Please provide valid input file path")

        if not out_file:
            raise Exception("Please provide valid output file path")
        pass
