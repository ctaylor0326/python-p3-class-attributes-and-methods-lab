class Song:
    
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        self.name = name
        self.artist = artist
        self.genre = genre

    @classmethod
    def add_song_to_count(cls):
        Song.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in Song.genre_count:
            Song.genres.append(genre)
            Song.genre_count[genre] = 1
        else:
            Song.genre_count[genre] += 1

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in Song.artist_count:
            Song.artists.append(artist)
            Song.artist_count[artist] = 1
        else:
            Song.artist_count[artist] += 1
    
 

