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
