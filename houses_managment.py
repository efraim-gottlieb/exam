from dwelling_hoses import DwellingHose, Room

class HouseManager:
  def __init__(self):
    self.houses = [DwellingHose('Dorm A'), DwellingHose('Dorm B')]
  def soldier_deployment(self, soldiers):
        soldiers.sort(key=lambda x: x.distance_from_base, reverse=True)
        cur = 0 
        deployed_soldiers = 0
        for house in self.houses:
            if not house.get_places():
                continue
            for room in house.rooms:
                while len(room.soldiers) < 8:
                        soldiers[cur].PlacementStatus = 'assigned'
                        soldiers[cur].house = house.name
                        soldiers[cur].room = room.id
                        room.soldiers.append(soldiers[cur])
                        cur += 1
                        deployed_soldiers += 1
                        if cur >= len(soldiers):
                            break
        not_deployed_soldiers = len([so for so in soldiers if so.PlacementStatus != 'assigned'])
        return {'deployed soldiers':deployed_soldiers,
                'not_deployed_soldiers' : not_deployed_soldiers,
                'soldiers' : soldiers
                }
  def get_houses_info(self):
      houses = {}

      for house in self.houses:
        full_rooms = 0
        empty_rooms = 0
        partially_filled_rooms = 0
        for room in house.rooms:
          if room.get_places() >= 8:
            full_rooms +=1
          elif room.get_places() == 0:
            empty_rooms += 1
          else:
            partially_filled_rooms += 1
          houses[house.id] = {  'house': house.name,
                                'full_rooms':full_rooms,
                                 'partially_filled_rooms':partially_filled_rooms,
                                 'empty_rooms':empty_rooms
                                 }
      return houses