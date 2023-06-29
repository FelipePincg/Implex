import numpy as np

def tsp(cities):
    num_cities = len(cities)
    all_cities = set(range(num_cities))
    start_city = 0
    unvisited_cities = all_cities - {start_city}
    current_city = start_city
    tour = [start_city]

    while unvisited_cities:
        next_city = min(unvisited_cities, key=lambda city: cities[current_city][city])
        unvisited_cities.remove(next_city)
        tour.append(next_city)
        current_city = next_city

    tour.append(start_city)
    return tour

# Exemplo de uso
cities = np.array([
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
])

tour = tsp(cities)
print("Melhor caminho:", tour)
