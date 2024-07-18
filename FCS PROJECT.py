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

#----------------------------------------------------------------------------------------------------------------------------------------


class Node:
  def __init__(self,driver):
    self.driver = driver
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def add_driver(self , driver):
    n = Node(driver)

    if self.head is None:
      self.head = n
      self.tail = n
      self.size = 1
    else:
      n.next = self.head
      self.head = n
      self.size += 1

  def append(self , driver):
    n= Node(driver)
    
    if not self.tail:
      self.head = self.tail = n
      self.size = 1
    else:
      self.tail.next = n
      self.tail = n
      self.size += 1

  def display(self):
    cur = self.head

    while cur is not None:
      print(f"{cur.driver.driver_id}, {cur.driver.driver_name}, {cur.driver.driver_start_city}")


      cur = cur.next

  def search_for_drivers_by_city(self , city):
    city = city.lower()
    
    cur = self.head
    drivers_in_city = []

    while cur is not None:
      if city.lower() == cur.driver.driver_start_city.lower():
        drivers_in_city.append(cur.driver)

      cur = cur.next

    return drivers_in_city
  

#----------------------------------------------------------------------------------------------------------------------------------------


class Graph:
  def __init__(self):
    self.cities = {}

  def add_city(self , city_name):
    n_name = city_name.lower()
    
    if n_name not in self.cities:
      self.cities[n_name] = City(n_name)

def add_edge(self, city1, city2):
    n_city1 = city1.lower()
    n_city2 = city2.lower()

    if n_city1 in self.cities and n_city2 in self.cities:
      self.cities[n_city1].add_neighbour(self.cities[n_city2])
      self.cities[n_city2].add_neighbour(self.cities[n_city1])
  