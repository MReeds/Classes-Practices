#You define the properties and methods.
# Name of the city.
# The mayor of the city.
# Year the city was established.
# A collection of all of the buildings in the city.
# A method to add a building to the city.

class City:
    def __init__(self, name, mayor, year):
        self.city_name = name
        self.mayor_name = mayor
        self.year_established = year
        self.all_buildings = list()

    def add_building(self, item):
            self.all_buildings.append(item)
            