import re
from itertools import permutations

class City:
    def __init__(self, name):
        self.name = name
        self.distances = {}

    def addDistances(self, cityName, distance):
        self.distances[cityName] = distance

def createCityIfNotExist(cities, city):
    if city not in cities:
        cities[city] = City(city)

def completeCity(cities, cityStart, cityDestination, distance):
    createCityIfNotExist(cities, cityStart)
    cities[cityStart].addDistances(cityDestination, distance)

def resolve(allRoutes, cities, startValue, fct):
    distance = startValue
    for route in allRoutes:
        distanceTmp = 0
        for cityStart, cityDestination in zip(route[:-1], route[1:]):
            distanceTmp += cities[cityStart].distances[cityDestination]
        distance = fct(distance, distanceTmp)
    return distance

with open("input.txt", "r") as file:
    lines = file.read().split("\n")

cities = {}

for line in lines:
    pattern = re.search("(.+) to (.+) = (\d+)", line)
    cityName1 = pattern.group(1).lower()
    cityName2 = pattern.group(2).lower()
    citiesDistance = int(pattern.group(3))
    completeCity(cities, cityName1, cityName2, citiesDistance)
    completeCity(cities, cityName2, cityName1, citiesDistance)

allRoutes = list(permutations(cities, len(cities)))

print("Puzzle 1 : " + str(resolve(allRoutes, cities, float("Inf"), min)))
print("Puzzle 2 : " + str(resolve(allRoutes, cities, -float("Inf"), max)))