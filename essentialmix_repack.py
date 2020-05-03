#!/usr/bin/env python3
"""
Produces & maintains a running archive of BBC Essential Mixes,
in a format of my preference
"""

import datetime
import logzero
from logzero import logger
import youtube_dl

archiveAccount = "https://soundcloud.com/essentialmixrepost"
finalFilename = "[%(date)s] Radio 1's Essential Mix - %(artist)s.%(ext)s"
albumTemplate = "%(year)s - BBC Essential Mixes"
albumArtist = "BBC %(year)s"
trackTitle = "%(year)s - %(artist)s Essential Mix"

# TBD: Args object vs. explicit params?
def archive(args):
    opt_flags["verbose"] = args.debug
    opt_flags["simulate"] = args.simulate
    opt_flags["playlistend"] = args.limit
    with youtube_dl.YoutubeDL(opt_flags) as ydl:
        # Two different ways to download, one surfaces title info but ignores progressHook?
        info_dict = ydl.extract_info(archiveAccount, False)
        for entry in info_dict.get("entries"):
            title = entry.get("title")
            timestamp = datetime.date.fromtimestamp(entry.get("timestamp"))
            artist = extractTitleData(title)
            print("Entry: " + artist + " - " + str(timestamp))
        ydl.download([archiveAccount])


"""
    Problem: No guaranteed consistency of title.
    Most common:
        * Chaos in the CBD - Essential Mix 2020-03-21
    Complications:
        * Seb Wildwood - BBC Radio 1 Essential Mix
        * Dimension Essential Mix - BBC Radio 1
        * TNGHT ESSENTIAL MIX 2019
        * rezz essential mix
        * Maya Jane Coles - Live @ Ants Ushuaia Ibiza 2019 [Essential Mix]
"""


def extractTitleData(title):
    artist, _, rest = title.partition(" - ")
    return artist


def progressHook(data):
    if data["status"] == "finished":
        print("Finished downloading, at " + data["filename"])


# TBD whether this ends up needed
class logShim(object):
    def debug(self, msg):
        logger.info(msg)

    def warning(self, msg):
        logger.warn(msg)

    def error(self, msg):
        logger.error(msg)


opt_flags = {
    "format": "bestaudio/best",
    "logger": logShim(),
    "progress_hooks": [progressHook],
    # "restrictfilenames": True,
    "outtmpl": "%(title)s.%(ext)s",
}
