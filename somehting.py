rows = 20
column = 3
playlist = []

class Song:
    def __init__(self, title, artist, explicit):
        self.title = title
        self.artist = artist
        self.explicit = explicit

i = 0
while i < rows:
    title = input("Input song name: ")
    artist = input("Input song artist: ")
    explicit = input("Is the song explicit? (yes/no): ")
    
    song = Song(title, artist, explicit)
    playlist.append(song)
    
    i += 1

for song in playlist:
    print(f"Title: {song.title}, Artist: {song.artist}, Explicit: {song.explicit}")
