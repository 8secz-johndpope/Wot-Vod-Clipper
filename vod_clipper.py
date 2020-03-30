#!/usr/bin/python

# Libraries
import ffmpeg


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
