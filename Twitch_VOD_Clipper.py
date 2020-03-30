import argparse
import datetime
import ffmpeg
import math
import ntpath
from pathlib import Path

from vod_clipper import VodClipper


def compute_video_length():
    metadata = ffmpeg.probe(input_file)
    video_length_seconds = math.ceil(float(metadata['streams'][0]['duration']))
    print('Video length {}s'.format(video_length_seconds))
    return video_length_seconds


def trim_clip(start_second):
    filename = compute_output_filename(start_second, start_second + duration)
    print('Trimming clip: ' + filename)
    clipper = VodClipper()
    clipper.clip(input_file, filename, start_second, duration)


def compute_output_filename(start_second, end_second):
    clip_filename = '{}-{}{}'.format(
        convert_seconds_to_filename_datetime(start_second),
        convert_seconds_to_filename_datetime(end_second),
        input_ext)
    return ntpath.join(output_directory, clip_filename)


def convert_seconds_to_datetime(seconds):
    return str(datetime.timedelta(seconds=seconds))


def convert_seconds_to_filename_datetime(seconds):
    datetime_str = convert_seconds_to_datetime(seconds)
    return datetime_str.replace(':', '.')


def main():
    print('Input file: {}\n'
          'Output path: {}\n'
          'Video clip duration: {}s'
          .format(input_file, output_path, duration))
    video_length = compute_video_length()
    for start_second in range(0, video_length, duration):
        trim_clip(start_second)


def parse_args():
    parser = argparse.ArgumentParser(description='Splitting Twitch VOD by a designated time interval.')
    parser.add_argument('-i', '--input', dest="input", required=True, help='Input video file path')
    parser.add_argument('-o', '--output', dest="output", default=None, help='Output video directory')
    parser.add_argument('-d', '--duration', dest="duration", default=1200, type=int,
                        help='Duration of each video clip, in seconds')

    args = parser.parse_args()
    _input_file = args.input
    _output_path = args.output

    if _output_path is None:
        _output_path = compute_default_output_path(_input_file)

    _input_file = ntpath.abspath(_input_file)
    _output_path = ntpath.abspath(_output_path)

    return _input_file, _output_path, args.duration


def compute_default_output_path(file_path):
    filename = ntpath.basename(file_path)
    return file_path.replace(filename, '')


def prepare_output_directory():
    Path(output_directory).mkdir(parents=True, exist_ok=True)


if __name__ == '__main__':
    input_file, output_path, duration = parse_args()
    input_name, input_ext = ntpath.splitext(ntpath.basename(input_file))
    output_directory = ntpath.join(output_path, input_name)
    prepare_output_directory()
    main()
