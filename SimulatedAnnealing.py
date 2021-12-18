import math
import random
import sys
from copy import copy
from BuildMatrix import create_matrix

# Starting Parameters of SP
T0 = 1000                           # Beginning Temperature
T = T0                              # Actual Temperature
END_TEMPERATURE = 10 ** -5          # Ending Temperature
A = 0.999                           # Cooling Factor
AGES = 50                           # Number of Ages
K = 0                               # Number of temperature decrease
path_local = []                     # Path of researching point
path_len_local = 0                  # Path length of researching point

# Asking for file
print("To start program choose testing file: ")
file_name = input()
print(f"You are using file '{file_name}' ")
print(" ")
matrix, OPT, number_of_cities = create_matrix(file_name)


# Get first path as a set of next cities
def first_route():
    cities = [0]

    for i in range(number_of_cities):
        cities.append(i)

    cities.append(0)
    cities_len = value(cities)

    return cities, cities_len


# Function copied from Branch_and_Bound.py
def find_very_first_best_path():
    first_best_len = 0
    first_best_path = [0]

    minimum = sys.maxsize
    next_city = 0

    # find shortest way from city with 0 index
    for i in range(matrix[0].size):
        if i != 0:
            if matrix[0][i] < minimum:
                minimum = matrix[0][i]
                next_city = i

    first_best_len += minimum
    first_best_path.append(next_city)

    # when first best_path == numbers_of_cities we have whole route
    while len(first_best_path) != number_of_cities:
        city_to_research = next_city
        minimum = sys.maxsize

        for i in range(matrix[city_to_research].size):
            if i not in first_best_path and i != 0:
                if matrix[city_to_research][i] < minimum:
                    minimum = matrix[city_to_research][i]
                    next_city = i

        first_best_len += minimum
        first_best_path.append(next_city)

    last_city = next_city
    first_best_path.append(0)
    first_best_len += matrix[last_city][0]

    return first_best_path, first_best_len


# Function copied from Branch_and_Bound.py
def value(route):
    value = 0

    for i in range(len(route)):
        v = i
        u = i + 1

        if u < len(route):
            city_1 = route[v]
            city_2 = route[u]
            value += matrix[city_1][city_2]

    return value


# Geometric Cooling
def Cooling():
    global A
    global T
    global T0

    T = A ** K * T0


# Getting first best path
best_path, best_len = find_very_first_best_path()
PRD = (100 * (best_len - OPT)) / OPT
print(f"{best_len} {PRD:.2f}%")

# Setting starting point
path_local = best_path
path_len_local = best_len
ages_left = AGES

# Simulated Annealing Algorithm
while T > END_TEMPERATURE:
    while ages_left > 0:

        # Getting 2 random cities to swap to get neighbour of actual point
        swap_city_index1 = random.randint(1, number_of_cities - 1)
        swap_city_index2 = random.randint(1, number_of_cities - 1)

        # Create random neighbour of actual point
        neighbour = copy(path_local)
        swap_helper = path_local[swap_city_index1]
        neighbour[swap_city_index1] = path_local[swap_city_index2]
        neighbour[swap_city_index2] = swap_helper

        neighbour_len = value(neighbour)

        # Counting probability of moving from actual point to neighbour
        if neighbour_len > path_len_local:
            probability = math.exp((path_len_local - neighbour_len) / T)
        else:
            probability = 1

        random_probability = random.uniform(0, 1)

        # Moving to neighbour
        if probability >= random_probability:
            path_len_local = neighbour_len
            path_local = neighbour

            # Found New Better path
            if path_len_local < best_len:
                best_len = path_len_local
                best_path = path_local

                # Printing new best solution
                PRD = (100 * (best_len - OPT)) / OPT
                print(f"{best_len} {PRD:.2f}%")

        ages_left -= 1

    # Reset ages_left and start cooling
    ages_left = AGES
    Cooling()
    K += 1

# Printing final solution
PRD = (100 * (best_len - OPT)) / OPT
print("")
print("Best Result: ")
print(f"{best_len} {PRD:.2f}%")
print(best_path)
