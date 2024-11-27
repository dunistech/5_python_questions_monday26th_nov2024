class Song:
    """
    Represents a song with its name and duration in minutes and seconds.
    """

    def __init__(self, name, time):
        self.__name = name
        minutes, seconds = map(int, time.split(":"))
        self.__minutes = minutes
        self.__seconds = seconds

    def get_name(self):
        return self.__name

    def get_minutes(self):
        return self.__minutes

    def get_seconds(self):
        return self.__seconds


class Album:
    """
    Represents an album containing a list of songs, artist, and release date.
    """

    def __init__(self, title, artist, date):
        self.__title = title
        self.__artist = artist
        self.__date = date
        self.__songs = []

    def get_title(self):
        return self.__title

    def get_artist(self):
        return self.__artist

    def get_date(self):
        return self.__date

    def get_songs(self):
        return self.__songs

    def add_song(self, song):
        self.__songs.append(song)

    def calculate_total_length(self):
        total_seconds = sum(song.get_minutes() * 60 + song.get_seconds() for song in self.__songs)
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"


def main():
    """
    Main function to demonstrate the use of Album and Song classes.
    """
    album_title = input("Enter name of album: ")
    artist_name = input("Enter the name of the artist: ")
    release_date = input("Enter the release date: ")
    num_songs = int(input("How many songs? "))

    album = Album(album_title, artist_name, release_date)

    for _ in range(num_songs):
        song_name = input("Enter name of song: ")
        song_length = input("Enter the length of the song (mm:ss): ")
        album.add_song(Song(song_name, song_length))

    print(f"Album length (hh:mm:ss) is {album.calculate_total_length()}")


if __name__ == "__main__":
    main()