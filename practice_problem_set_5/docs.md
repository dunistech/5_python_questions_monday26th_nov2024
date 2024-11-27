 Problem 1: Sorting a List of Names (sort_list.py)

```python
def find_next(names, start_index):
    """
    Finds the index of the smallest string alphabetically in the unsorted portion of the list.
    :param names: List of names
    :param start_index: Index where the unsorted portion begins
    :return: Index of the smallest string in the unsorted portion
    """
    min_index = start_index
    for i in range(start_index + 1, len(names)):
        if names[i] < names[min_index]:
            min_index = i
    return min_index


def put_in_order(names, start_index, min_index):
    """
    Swaps the element at start_index with the element at min_index.
    :param names: List of names
    :param start_index: Index of the first element in the unsorted portion
    :param min_index: Index of the smallest element in the unsorted portion
    """
    names[start_index], names[min_index] = names[min_index], names[start_index]


def main():
    """
    Main function to sort a list of names alphabetically.
    """
    names = ["Zita", "Henny", "Benny", "Harold", "Danny", "Penny"]
    print("Unsorted list:")
    print(names)

    for i in range(len(names)):
        min_index = find_next(names, i)
        put_in_order(names, i, min_index)

    print("Sorted list:")
    print(names)


if __name__ == "__main__":
    main()

---

 Problem 2: Managing Music Albums (music.py)

```python
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
```

---

 Explanation for Beginners:

1. **Problem 1: Sorting Names**
   - The program divides the list into a "sorted" and "unsorted" portion.
   - **`find_next`** identifies the smallest name in the unsorted part.
   - **`put_in_order`** swaps the smallest name to the correct position.
   - This is repeated until the entire list is sorted.

2. **Problem 2: Music Management**
   - **`Song` Class** represents a single song, storing its name and duration.
   - **`Album` Class** holds album details and a list of songs. It can add songs and calculate total playtime.
   - The `main` function takes user inputs for album and songs, creates instances of `Song` and `Album`, and calculates the total album length.

Both programs are written with clear comments, making it easier for beginners to understand each step. The `main` functions are designed for direct testing with predefined inputs or user input.