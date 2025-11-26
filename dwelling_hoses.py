from soldier import Soldier

class Room:
  def __init__(self, id):
    self.id = id
    self.soldiers:list[Soldier] = []
  def get_places(self):
    return 8 - len(self.soldiers)
    
class DwellingHose:
  def __init__(self, name):
    self.name = name
    self.rooms = [Room(_+1) for _ in range(10)]
  def get_places(self):
    return 80 - sum([len(room.soldiers) for room in self.rooms])