class Driver:
  def __init__(self , driver_id , driver_name , driver_start_city):
    self.driver_id = driver_id
    self.driver_name = driver_name
    self.driver_start_city = driver_start_city


class City:
  def __init__(self , city_name):
    self.city_name = city_name
    self.city_neighbours = []
  
  def add_neighbour(self , neighbour):
    if neighbour not in self.city_neighbours:
      self.city_neighbours.append(neighbour)