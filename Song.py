class Song:

  def __init__(self, title):
      self.__title = title
      self.__next_song = None


  # TODO: Create a getter method for the title attribute, called get_title
  def get_title(self):
    '''Getter method for retrieving the title of the song passed in'''
    return self.__title
  
  # TODO: Create a setter method for the title attribute, called set_title. Make sure titles are type cased to strings and are Title Cased.
  def set_title(self, title):
      '''Method to set the current song title to what's passed in'''
      self.__title = str(title).title()



  # TODO: Create a getter method for the next_song attribute, called get_next_song
  def get_next_song(self):
    '''Method for retrieving the next_song attribute'''
    return self.__next_song


  # TODO: Create a setter method for the next_song attribute, called set_next_song
  def set_next_song(self, next_title):
    '''Method for setting the pointer of the current song to what's passed in'''
    self.__next_song = next_title


  # TODO: Using the __str___ dunder method, return a string of the song title.
  def __str__(self):
    return str(self.get_title).title()


  # TODO: Using the __repr__ dunder method, return a string formatted as the following:'Song Title -> Next Song Title'
  def __repr__(self):
    return f"{self.get_title()} -> {self.get_next_song()}"