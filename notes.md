# Essential Mix intake script

* https://github.com/ytdl-org/youtube-dl/blob/master/README.md#embedding-youtube-dl
  - https://github.com/ytdl-org/youtube-dl/blob/master/youtube_dl/extractor/soundcloud.py
* https://soundcloud.com/essentialmixrepost
* Mutagen - https://mutagen.readthedocs.io/en/latest/user/gettingstarted.html
* Eyed3 - https://eyed3.readthedocs.io/en/latest/modules.html

In:  Chaos In The CBD - Essential Mix 2020-03-21
Out:
  Title:        %YYYY% - %artist% Essential Mix
  Artist:       %artist%
  Album Artist: BBC %YYYY%
  Album:        %YYYY% - BBC Essential Mixes
  Track#:       Sequential (might be difficult)
  Filename:     [YYYY-MM-DD] Radio 1's Essential Mix - %artist%


1. Check Soundcloud for tracks
1. Load up list of existing tracks
1. See if there's new ones / exclude old ones
  - Archive.txt?
1. Download new ones
1. Split file title into Artist, Date; validate
  - validate date gap > 1 week?
1. Write ID3 data <>
1. Change filename <>

https://docs.python-guide.org/writing/structure/
