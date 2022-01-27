import random
import sys

from BuildMatrix import create_matrix

# Starting Parameters
POPULATION = []                     # All permutations of cities with their values of routes
POPULATION_SIZE = 1000              # Number of permutation in population
CROSSOVER_NUMBER = 150              # Number of crossovers in single iteration
ACTUAL_GENERATION = 0               # Actual iteration of main algorithm
FINAL_NUMBER_OF_GENERATION = 2000   # Number of main algorithm iterations
MUTATION_NUMBER = 30                # Number of mutations in iteration
MUTATION_POWER = 1                  # Number of changes in single mutation
NUMBER_OF_DUELS = 3                 # Number of battles for every single entity in population during selection
BEST_ENTITY_LEN = sys.maxsize       # Length of best route
BEST_ENTITY_ROUTE = []              # Best found route in all generations

# Asking for file
print("To start program choose testing file: ")
file_name = input()
print(f"You are using file '{file_name}' ")
print(" ")



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


# Function create new population
def create_new_population():
    # Creating rest entities by random adding indexes of city
    for i in range(POPULATION_SIZE):

        new_random_permutation = [0]
        while True:
            city_index = random.randint(1, number_of_cities - 1)

            if not city_index in new_random_permutation:
                new_random_permutation.append(city_index)

            if len(new_random_permutation) == number_of_cities:
                new_random_permutation.append(0)
                element_of_population_list = [value(new_random_permutation), new_random_permutation]
                POPULATION.append(element_of_population_list)
                break


def crossover():
    for i in range(CROSSOVER_NUMBER):
        k = random.randint(0, POPULATION_SIZE - 1)
        l = random.randint(0, POPULATION_SIZE - 1)

        first_entity_permutation_to_cross = POPULATION[k][1]
        second_entity_permutation_to_cross = POPULATION[l][1]

        new_entity_permutation = []

        # Copy half of first permutation to new entity
        for i in range(int(len(first_entity_permutation_to_cross) / 2)):
            new_entity_permutation.append(first_entity_permutation_to_cross[i])

        # Copy missing city to new entity from second permutation
        for i in range(len(second_entity_permutation_to_cross)):
            if not second_entity_permutation_to_cross[i] in new_entity_permutation:
                new_entity_permutation.append(second_entity_permutation_to_cross[i])

        new_entity_permutation.append(0)

        new_entity = [value(new_entity_permutation), new_entity_permutation]
        POPULATION.append(new_entity)


def mutation():
    k = random.randint(0, POPULATION_SIZE - 1)
    entity_to_mute = POPULATION[k]

    for i in range(MUTATION_NUMBER - 1):
        first_gen_to_swap = random.randint(1, number_of_cities - 1)
        second_gen_to_swap = random.randint(1, number_of_cities - 1)

        helper = entity_to_mute[1][first_gen_to_swap]

        entity_to_mute[1][first_gen_to_swap] = entity_to_mute[1][second_gen_to_swap]
        entity_to_mute[1][second_gen_to_swap] = helper


def selection():
    global POPULATION
    new_generation = []

    # Find best entity
    best_entity_index = 0
    best_entity_len = POPULATION[0][0]

    # Find best entity in population
    for i in range(len(POPULATION)):
        if POPULATION[i][0] < best_entity_len:
            best_entity_index = i
            best_entity_len = POPULATION[i][0]

    global BEST_ENTITY_LEN
    global BEST_ENTITY_ROUTE

    # Check if new entity is better than saved one
    if best_entity_len < BEST_ENTITY_LEN:
        BEST_ENTITY_LEN = best_entity_len
        BEST_ENTITY_ROUTE = POPULATION[best_entity_index][1]

        PRD = (100 * (BEST_ENTITY_LEN - OPT)) / OPT
        print(f"{BEST_ENTITY_LEN} {PRD:.2f}%")

    # Appending best entity to new generation
    new_generation.append(POPULATION[best_entity_index])
    POPULATION.pop(best_entity_index)

    numbers_of_entities_in_tournament = POPULATION_SIZE + CROSSOVER_NUMBER - 1

    while len(new_generation) != POPULATION_SIZE:

        # Find 2 entities random
        entity_index_1 = random.randint(0, numbers_of_entities_in_tournament - 1)
        entity_index_2 = random.randint(0, numbers_of_entities_in_tournament - 1)

        entity_1 = POPULATION[entity_index_1]
        entity_2 = POPULATION[entity_index_2]

        if entity_1[0] < entity_2[0]:
            new_generation.append(entity_1)
            POPULATION.pop(entity_index_1)

        else:
            new_generation.append(entity_2)
            POPULATION.pop(entity_index_2)

        numbers_of_entities_in_tournament -= 1

    POPULATION = new_generation


def selection_new():
    global POPULATION
    new_generation = []
    punctation = []
    best_entity_len = sys.maxsize
    best_entity_index = 0

    # Find best entity in population
    for i in range(len(POPULATION)):
        if POPULATION[i][0] < best_entity_len:
            best_entity_index = i
            best_entity_len = POPULATION[i][0]

    global BEST_ENTITY_LEN
    global BEST_ENTITY_ROUTE

    # Check if new entity is better than saved one
    if best_entity_len < BEST_ENTITY_LEN:
        BEST_ENTITY_LEN = best_entity_len
        BEST_ENTITY_ROUTE = POPULATION[best_entity_index][1]

        PRD = (100 * (BEST_ENTITY_LEN - OPT)) / OPT
        print(f"{BEST_ENTITY_LEN} {PRD:.2f}%")

    # For every entity in population
    for i in range(len(POPULATION)):

        # create punctation for entity with i index
        punctation.append([0, i])

        # find opponents and start duels
        for k in range(NUMBER_OF_DUELS):
            opponent_index = random.randint(0, len(POPULATION) - 1)

            while i == opponent_index:
                opponent_index = random.randint(0, len(POPULATION) - 1)

            entity = POPULATION[i]
            opponent = POPULATION[opponent_index]

            if entity[0] < opponent[0]:
                punctation[i][0] += 1

    # Sort entities from best -> worst
    punctation.sort(reverse=True)

    # Append best entities to new generation
    for i in range(POPULATION_SIZE):
        entity_index = punctation[i][1]
        entity_to_add = POPULATION[entity_index]

        new_generation.append(entity_to_add)

    POPULATION = new_generation


# Main Loop
create_new_population()

while ACTUAL_GENERATION < FINAL_NUMBER_OF_GENERATION:
    for i in range(MUTATION_NUMBER):
        mutation()
    crossover()
    selection_new()

    ACTUAL_GENERATION += 1

print('---')
PRD = (100 * (BEST_ENTITY_LEN - OPT)) / OPT
print(f"{BEST_ENTITY_LEN} {PRD:.2f}%")
print(f"Best Route: {BEST_ENTITY_ROUTE}")
print('---')
