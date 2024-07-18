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
  
def get_neighbors(self , city):
    n_city = city.lower()
    
    if n_city in self.cities:
      return self.cities[n_city].city_neighbours

    return []

def display_graph(self):
    for key , object in self.cities.items(): 
      neighbors = self.get_neighbors(key)
      neighbor_names = [neighbor.city_name for neighbor in neighbors] 
      
      print(f"{key}:  {', '.join(neighbor_names)}")


#----------------------------------------------------------------------------------------------------------------------------------------


class WeDeliverProcess:
    def __init__(self, predefined_data):
      self.drivers = LinkedList()
      self.graph = Graph()
      self.driver_count = 0
      self.initialize_from_data(predefined_data)

    def initialize_from_data(self, data):
        if "cities" in data:
            for city_name in data["cities"]:
                self.graph.add_city(city_name)
                for neighbor in data["cities"][city_name]:
                    self.graph.add_city(neighbor)
                    self.graph.add_edge(city_name, neighbor)

        if "drivers" in data:
            for driver_info in data["drivers"]:
                self.add_driver(driver_info["driver_name"], driver_info["driver_start_city"], suppress_message=True)


    def generate_id(self):
        self.driver_count += 1

        return f"ID {self.driver_count:03d}"


    def add_driver(self, name, start_city, suppress_message=False):
        if start_city.lower() not in self.graph.cities:
            add_city = input(f"{start_city} is not in the database. Do you want to add it? (y/n): ").lower()
            if add_city == "y":
                self.graph.add_city(start_city)
            else:
                print("Drivers cannot be added to the system without a valid starting city.")
                return

        driver_id = self.generate_id()
        new_driver = Driver(driver_id, name, start_city)
        self.drivers.add_driver(new_driver)

        if not suppress_message:
            print(f"Driver {name} is successfully added to the system.")

