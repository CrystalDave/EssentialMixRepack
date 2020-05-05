# EssentialMixRepack
 Archives & repacks essential mixes for my own structure.
 **ALPHA**, don't rely on this yet.

## Desired Behavior
```
In:  Chaos In The CBD - Essential Mix 2020-03-21
Out:
  Title:        %YYYY% - %artist% Essential Mix
  Artist:       %artist%
  Album Artist: BBC %YYYY%
  Album:        %YYYY% - BBC Essential Mixes
  Track#:       Sequential (might be difficult)
  Filename:     [YYYY-MM-DD] Radio 1's Essential Mix - %artist%
```

### MVP:
* Hit Soundcloud link, download limit 1
* Extract info from file info (or from download)
* Change filename

### Full Feature
* Check Soundcloud for tracks
* Load up list of existing tracks
* See if there's new ones / exclude old ones
  - Archive.txt?
* Download new one(s)
* Parse title as possible
* Check against Wikipedia list for fuzzy match?
  * https://en.wikipedia.org/w/api.php?action=parse&prop=sections&page=List_of_Essential_Mix_episodes&format=json&section=1&prop=wikitext
  * https://github.com/bcicen/wikitables
  * https://github.com/5j9/wikitextparser
* Write ID3 data
  * Mutagen - https://mutagen.readthedocs.io/en/latest/user/gettingstarted.html
  * Eyed3 - https://eyed3.readthedocs.io/en/latest/modules.html
* Change filename
