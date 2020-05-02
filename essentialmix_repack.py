#!/usr/bin/env python3
"""
Produces & maintains a running archive of BBC Essential Mixes,
in a format of my preference
"""

import logzero
from logzero import logger
import youtube_dl

archiveAccount = "https://soundcloud.com/essentialmixrepost"


# TBD: Args object vs. explicit params?
def archive(args):
    opt_flags["verbose"] = args.debug
    opt_flags["simulate"] = args.simulate
    opt_flags["playlistend"] = args.limit
    with youtube_dl.YoutubeDL(opt_flags) as ydl:
        # Two different ways to download, one surfaces title info but ignores progressHook?
        ydl.download([archiveAccount])
        # info_dict = ydl.extract_info(archiveAccount, opt_flags["simulate"])
        # print(info_dict.get("title", None))


def progressHook(data):
    if data["status"] == "finished":
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
    "logger": logShim(),
    "progress_hooks": [progressHook],
    "restrictfilenames": True,
}
