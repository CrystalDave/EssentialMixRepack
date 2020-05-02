#!/usr/bin/env python3
"""
Produces & maintains a running archive of BBC Essential Mixes,
in a format of my preference
"""

import logzero
from logzero import logger
import youtube_dl

archiveAccount = "https://soundcloud.com/essentialmixrepost"

def progressHook(data):
    if data['status'] == 'finished':
        print("Finished downloading")

# TBD whether this ends up needed
class logShim(object):
    def debug(self, msg):
        logger.info(msg)

    def warning(self, msg):
        logger.warn(msg)

    def error(self, msg):
        logger.error(msg)

opt_flags = {
    'logger': logShim(),
    'progress_hooks': [progressHook]
}

def archive(args):
    opt_flags['verbose'] = args.debug
    opt_flags['simulate'] = args.simulate
    opt_flags['playlistend'] = args.limit
    with youtube_dl.YoutubeDL(opt_flags) as ydl:
        ydl.download([archiveAccount])
