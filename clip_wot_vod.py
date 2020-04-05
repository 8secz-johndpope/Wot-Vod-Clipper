#!/usr/bin/python

# Libraries
import argparse

# Locals
from wot_vod_clipper import WotVodClipper
import wot_vod_parser


def main():
    print("Start clipping VOD: {}\n"
          "Output directory:   {}\n"
          "Configuration file: {}\n".format(_in_file, _out_dir, _config))
    with open(_in_file) as config_file:
        wot_vod = wot_vod_parser.parse(config_file)
    _clipper.clip(_in_file, _out_dir, wot_vod)
    pass


def parse_args():
    parser = argparse.ArgumentParser(description='Splitting Twitch VOD by a designated time interval.')
    parser.add_argument('-i', '--input', dest="input", required=True, help='Input video file path')
    parser.add_argument('-o', '--output', dest="output", default=None, help='Output video directory')
    parser.add_argument('-c', '--config', dest="configuration", required=True, help='Configuration file path')

    args = parser.parse_args()
    return args.input, args.output, args.configuration


if __name__ == '__main__':
    _in_file, _out_dir, _config = parse_args()
    _clipper = WotVodClipper()
    main()
