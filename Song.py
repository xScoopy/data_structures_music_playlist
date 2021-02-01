class Song:

  def __init__(self, title):
      self.__title = str(title).title()
      self.__next_song = None


  def get_title(self):
    '''Getter method for retrieving the title of the song passed in'''
    return self.__title
  
  def set_title(self, title):
      '''Method to set the current song title to what's passed in'''
      self.__title = str(title).title()


  def get_next_song(self):
    '''Method for retrieving the next_song attribute'''
    return self.__next_song


  def set_next_song(self, next_title):
    '''Method for setting the pointer of the current song to what's passed in'''
    self.__next_song = next_title

  def __str__(self):
    return str(self.get_title).title()


  def __repr__(self):
    return f"{self.get_title()} -> {self.get_next_song()}"