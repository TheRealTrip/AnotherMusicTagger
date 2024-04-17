# Another Music Tagger
Things to note:
 - This script processes one album at a time.
 - It expects you to organize your music according to the Jellyfin standard. [here](https://jellyfin.org/docs/general/server/media/music/)
 - I have accounted for very few edge cases, it was built for a simple album without multiple discs or anything of the sort. (contributions welcome)
 - This is the first release and quite possibly the only release as there are probably other repos that do this better already.
 - This script will fill in the following tags: artist name, track number, song name and album name.
 
## Usage

- Download ``processor.py``
- Open it with a text editor of your choice and edit 'ABSOLUTEPATHTOANINDIVIDUALALBUM' to the absolute path to an individual album.
- Install the two dependencies pytaglib and musicbrainzngs. Keep in mind pytaglib needs the underlying C library also installed.
- Run ``processor.py``

