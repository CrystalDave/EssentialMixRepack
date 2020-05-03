# Essential Mix intake script

Spec:
In:  Chaos In The CBD - Essential Mix 2020-03-21
Out:
  Title:        %YYYY% - %artist% Essential Mix
  Artist:       %artist%
  Album Artist: BBC %YYYY%
  Album:        %YYYY% - BBC Essential Mixes
  Track#:       Sequential (might be difficult)
  Filename:     [YYYY-MM-DD] Radio 1's Essential Mix - %artist%

Full Feature:
* Check Soundcloud for tracks
* Load up list of existing tracks
* See if there's new ones / exclude old ones
  - Archive.txt?
* Download new ones
* Parse title as possible
* Check against Wikipedia list for fuzzy match?
  * https://en.wikipedia.org/w/api.php?action=parse&prop=sections&page=List_of_Essential_Mix_episodes&format=json&section=1&prop=wikitext
  * https://github.com/bcicen/wikitables
  * https://github.com/5j9/wikitextparser
* Write ID3 data <>
  * Mutagen - https://mutagen.readthedocs.io/en/latest/user/gettingstarted.html
  * Eyed3 - https://eyed3.readthedocs.io/en/latest/modules.html
* Change filename <>


MVP:
* Hit Soundcloud link, download limit 1
* Extract info from file info (or from download)
* update ID3 tags
* Change filename

Input issues:
* Could be missing a track (archive mode)
* Some entries don't have a date in title
  * There is a timestamp though, is upload date next-best-item?
* What about previous years?
