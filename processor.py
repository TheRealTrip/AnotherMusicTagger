import os, taglib, musicbrainzngs
folder = "ABSOLUTEPATHTOANINDIVIDUALALBUM"
musicbrainzngs.set_useragent("Library Tagger", "0.1", "therealtrip3@gmail.com")




def songNamesLookup(album, artist):
    result = musicbrainzngs.search_releases(artist=artist, release=album,
                                       limit=1)
    if not result['release-list']:
        sys.exit("no release found")
    for (idx, release) in enumerate(result['release-list']):
        id = release['id']
    release_info = musicbrainzngs.get_release_by_id(id, includes=["recordings"])
    tracks_info = release_info['release']['medium-list'][0]['track-list']
    track_names = []
    for track in tracks_info:
        track_name = track['recording']['title']
        track_names.append(track_name)
    return track_names




def addMetadata(file, tracknumber, album, artist, tracks):
    print("File path is " + str(file))
    print("Track number is " + str(tracknumber))
    print("Album is " + str(album))
    print("Artist is " + str(artist))
    print("Adding tags...")
    with taglib.File(file, save_on_exit=True) as song:
        song.tags["ALBUM"] = [album]
        song.tags["ARTIST"] = [artist]
        song.tags["TRACKNUMBER"] = [str(tracknumber)]
        song.tags["TITLE"] = [tracks[int(tracknumber)-1]]
       

files = os.path.join(folder, os.listdir(folder)[0])
album = files.split('/')[-2]
artist = files.split('/')[-3]
tracks = songNamesLookup(album, artist)


for file in os.listdir(folder):
    f = os.path.join(folder, file)
    if os.path.isfile(f):
        track = file.split(' ')[1].split('.')[0]
        albumname = f.split('/')[-2]
        artist = f.split('/')[-3]
        addMetadata(f, track, albumname, artist, tracks)
