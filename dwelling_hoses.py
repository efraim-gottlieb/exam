from soldier import Soldier

class Room:
  def __init__(self, id, house_id, house_name):
    self.id = id
    self.soldiers:list[Soldier] = []
    self.house_id = house_id
    self.house_name = house_name
  def get_places(self):
    return 8 - len(self.soldiers)
    
class DwellingHose:
  houses_counter = 0
  def __init__(self, name):
    DwellingHose.houses_counter += 1
    self.id = DwellingHose.houses_counter
    self.name = name
    self.rooms = [Room(_+1, self.id, self.name) for _ in range(10)]
  def get_places(self):
    return 80 - sum([len(room.soldiers) for room in self.rooms])