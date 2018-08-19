class Folder:
  def __init__(self, home_path, name, dir, atime, ctime, size, ext):
    self.home_path = home_path
    self.name = name
    self.dir = dir
    self.atime = atime
    self.ctime = ctime
    self.size = size
    self.ext = ext

class Movie(Folder):
    def __init__(self, Folder, id, url, title, year, plot, director_box, actor_box):
        super().__init__(Folder.home_path, Folder.name, Folder.dir, Folder.atime, Folder.ctime, Folder.size, Folder.ext)
        self.id = id
        self.url = url
        self.title = title
        self.year = year
        self.plot = plot
        self.director_box = director_box
        self.actor_box = actor_box

class Actor():
    def __init__(self, name, id):
        self.name = name
        self.id = id


class Director():
    def __init__(self, name, id):
        self.name = name
        self.id = id