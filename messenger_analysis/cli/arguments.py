'''CLI argument parsing'''


import os
import sys
from argparse import ArgumentParser
from typing import Any, List
from .config import CONFIG


def parse_arguments(args: List[Any] = None):
    '''Parses CLI arguments'''
    if args is None:
        args = sys.argv[1:]

    parser = ArgumentParser(description='explore your messaging habits')

    # Input
    parser.add_argument('-d', '--datasource',
                        type=str,
                        default=os.path.join('.', 'data', 'messages'),
                        help='messenger data directory. defaults to ./data/messages')
    parser.add_argument('--stopwords',
                        type=str,
                        default=os.path.join('.', 'data', 'stopwords.txt'),
                        help='additional custom stopwords to ignore overrused words.' +
                             'each word should be on a separate line')

    # Actions
    parser.add_argument('--plotTimestamps',
                        type=int,
                        choices=[5, 15, 30, 60],
                        help='plot message timestamp frequencies, in intervals of 5, 15, 30, or 60 minutes')
    parser.add_argument('--plotTopWords',
                        type=int,
                        help='show the top N words')

    # Output
    parser.add_argument('--output',
                        type=str,
                        default=os.path.join('.', 'output'),
                        help='output directory. defaults to ./output')

    # Filtering chats
    parser.add_argument('--includeNames',
                        nargs=1,
                        help='comma-separated list of names to include')
    parser.add_argument('--excludeGroups',
                        action='store_true',
                        help='exclude group chats with >2 participants')
    parser.add_argument('--excludeArchived',
                        action='store_true',
                        help='exclude archived chats')

    # Filtering words
    parser.add_argument('--includeWords',
                        nargs=1,
                        help='comma-separated list of regexes for words to include')
    parser.add_argument('--excludeWords',
                        nargs=1,
                        help='comma-separated list of regexes for words to exclude')
    parser.add_argument('--matchWords',
                        nargs=1,
                        help='basic regex to match against words to include')
    parser.add_argument('--matchExcludeWords',
                        nargs=1,
                        help='basic regex to match against words to exclude')

    # Debug
    parser.add_argument('--validate',
                        action='store_true',
                        help='debug. perform additional validation on dataset')

    CONFIG.update(parser.parse_args(args))
