import sys
from copy import copy

from BuildMatrix import create_matrix

matrix, OPT, number_of_cities = create_matrix("m6.atsp")


def find_very_first_best_path():
    first_best_len = 0
    first_best_path = [0]

    minimum = sys.maxsize
    next_city = 0
    for i in range(matrix[0].size):
        if i != 0:
            if matrix[0][i] < minimum:
                minimum = matrix[0][i]
                next_city = i

    first_best_len += minimum
    first_best_path.append(next_city)

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


def bound(vertex):
    bound = 0

    # Count actual length of path
    for i in range(len(vertex)):
        v = i
        u = i + 1

        if u < len(vertex):
            city_1 = vertex[v]
            city_2 = vertex[u]
            edge = matrix[city_1][city_2]

            bound += edge

    cities_still_to_search = []

    # finding cities that we are still not in path
    for i in range(number_of_cities):
        if i not in vertex:
            cities_still_to_search.append(i)

    # adding city from vertex that dont have path to next city
    cities_still_to_search.append(vertex[-1])

    # finding minimal cost of traveling to every city that we have to travel to
    for city in cities_still_to_search:
        minimum = sys.maxsize
        for i in range(matrix[city].size):
            if i not in vertex or i == 0:
                if matrix[city][i] < minimum and i != city:
                    minimum = matrix[city][i]
        bound += minimum

    return bound



