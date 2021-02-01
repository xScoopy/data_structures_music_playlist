from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None #'Head' pointer for our linked list


  def add_song(self, title):
    '''Add a song node to the playlist. This will add the song to the END of the linked list'''
    if self.__first_song == None:
      new_song = Song(title)
      new_song.set_next_song(self.__first_song)
      self.__first_song = new_song
    else:
      new_song = Song(title)
      current_song = self.__first_song
      while current_song.get_next_song() is not None:
        current_song = current_song.get_next_song()
      current_song.set_next_song(new_song)

  def find_song(self, title):
    '''Finds a song and prints the song position in the playlist to the user'''
    current_song = self.__first_song
    counter = 0
    if self.length() is None:
      return -1
    else:
      while current_song:
        if current_song.get_title() == title:
          return counter
        else:
          counter += 1
          current_song = current_song.get_next_song()
      return -1


  def remove_song(self, title):
    '''Checks if song exists and removes, prints a message if it could not find the song to remove to allow users to check for typos in their entry'''
    current_song = self.__first_song
    if not current_song:
      return print(f"There are no songs to remove")
    if current_song.get_title() == title:
      self.__first_song = current_song.get_next_song()
      return print(f"{title} has been removed")
    else:
      while current_song.get_next_song():
        if current_song.get_next_song().get_title() == title:
          current_song.set_next_song(current_song.get_next_song().get_next_song())
          return print(f"{title} has been removed")
        else:
          current_song = current_song.get_next_song()
      return print(f"{title} wasn't found to be removed")


  def length(self):
    '''returns length of the playlist'''
    current_song = self.__first_song
    counter = 0
    while current_song:
      current_song = current_song.get_next_song()
      counter += 1
    return counter


  def print_songs(self):
    '''Prints songs in order each with their own numerical counter next to them.'''
    current_song = self.__first_song
    counter = 1
    while current_song:
      print(f"{counter}. {current_song.get_title()}")
      current_song = current_song.get_next_song()
      counter += 1

  