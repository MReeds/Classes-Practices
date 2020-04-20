from city import City
from building import Building

# Create a new city instance and add your building
# instances to it. Once all buildings are in the city,
# iterate the city's building collection and output the
# information about each building in the city.

# megalopolis = City()

# for building in megalopolis.buildings:
#    print(building)

new_york = City("New York", "Dan Jones", "1885")

Adrians_building = Building("800 Parkway Drive", 25)
Adrians_building.purchase("Adrian Reeds")
Adrians_building.construct()
new_york.add_building(Adrians_building)

Kristens_building = Building("1200 Seaway Pass", 58)
Kristens_building.purchase("Kristen Reeds")
Kristens_building.construct()
new_york.add_building(Kristens_building)

Savannahs_building = Building("P Sherman 42 Wallaby Way Sydney", 45)
Savannahs_building.purchase("Savannah Reeds")
Savannahs_building.construct()
new_york.add_building(Savannahs_building)

Matts_building = Building("23 Westwood Avenue", 25)
Matts_building.purchase("Matt Reeds")
Matts_building.construct()
new_york.add_building(Matts_building)

for building in new_york.all_buildings:
    print(building)