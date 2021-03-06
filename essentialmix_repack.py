#!/usr/bin/env python3
"""
Produces & maintains a running archive of BBC Essential Mixes,
in a format of my preference
"""

import datetime
import logzero
from logzero import logger
import re
import youtube_dl

archiveAccount = "https://soundcloud.com/essentialmixrepost"
finalFilename = "[{date}] Radio 1's Essential Mix - {artist}.%(ext)s"
albumTemplate = "{year} - BBC Essential Mixes"
albumArtist = "BBC {year}"
trackTitle = "{year} - {artist} Essential Mix"

# TBD whether this ends up needed
class logShim(object):
    def debug(self, msg):
        logger.info(msg)

    def warning(self, msg):
        logger.warn(msg)

    def error(self, msg):
        logger.error(msg)


def progressHook(data):
    if data["status"] == "finished":
        print("Finished downloading, at " + data["filename"])


opt_flags = {
    "format": "bestaudio/best",
    "logger": logShim(),
    "progress_hooks": [progressHook],
    "outtmpl": "%(title)s.%(ext)s",
}


def archive(args):
    """Core archival logic, split out to sub-functions as they make sense"""
    opt_flags["verbose"] = args.debug
    opt_flags["simulate"] = args.simulate
    opt_flags["playlistend"] = args.limit
    downloadInfo()
    with youtube_dl.YoutubeDL(opt_flags) as ydl:
        ydl.download([archiveAccount])


def downloadInfo():
    """Download info **about** track, but don't download the track yet"""
    with youtube_dl.YoutubeDL(opt_flags) as ydl:
        # Two different ways to download, one surfaces title info but ignores progressHook?
        info_dict = ydl.extract_info(archiveAccount, False)
        for entry in info_dict.get("entries"):
            titleData = extractTitleData(entry.get("title"))
            if titleData["date"] is None:
                # Fallback to upload date
                timestamp = datetime.date.fromtimestamp(entry.get("timestamp"))
                titleData["date"] = str(timestamp)
            if titleData["artist"] is None:
                # Fallback to uploader
                titleData["artist"] = entry.get("uploader")
            opt_flags["outtmpl"] = finalFilename.format(**titleData)


def extractTitleData(title):
    """
        Problem: No guaranteed consistency of title.
        Most common:
            [x] Carista - Essential Mix 2020-03-21
        Complications:
            [x] Seb Wildwood - BBC Radio 1 Essential Mix
            [x] Dimension Essential Mix - BBC Radio 1
            [ ] TNGHT ESSENTIAL MIX 2019
            [ ] rezz essential mix
            [x] Maya Jane Coles - Live @ Ants Ushuaia Ibiza 2019 [Essential Mix]
            [ ] Kasra | Essential Mix | BBC Radio 1 | 20.07.2019
            [ ] BBC Radio 1 Essential Mix (15/06/19) (Missing, check post data for artist?)
        This is going to be brittle (unless I figure out something better)
    """
    happyPath = re.compile(r"(?P<artist>.+?) - Essential Mix (?P<date>\d+-\d+-\d+)")
    result = {"artist": None, "date": None}
    if happyPath.match(title):
        # Validate date?
        result = happyPath.match(title).groupdict()
    elif "-" in title:
        # A rough guess fallback for now, will break on hyphen in artist name
        # TBD: Case sensitivity
        artist, _, _ = title.partition(" -")
        result["artist"] = artist.partition(" BBC")[0].partition(" Essential")[0]
    return result
