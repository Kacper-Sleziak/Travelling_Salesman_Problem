from copy import copy
from BuildMatrix import create_matrix

print("To start program choose testing file: ")
file_name = input()
print(f"You are using file '{file_name}' ")
print(" ")
matrix, OPT, number_of_cities = create_matrix(file_name)


def next_permutation(a):
    """Generate the lexicographically next permutation inplace.
    Return false if there is no next permutation.
    """
    # Find the largest index i such that a[i] < a[i + 1]. If no such
    # index exists, the permutation is the last permutation
    for i in reversed(range(len(a) - 1)):
        if a[i] < a[i + 1]:
            break  # found
    else:  # no break: not found
        return False  # no next permutation

    # Find the largest index j greater than i such that a[i] < a[j]
    j = next(j for j in reversed(range(i + 1, len(a))) if a[i] < a[j])

    # Swap the value of a[i] with that of a[j]
    a[i], a[j] = a[j], a[i]

    # Reverse sequence from a[i + 1] up to and including the final element a[n]
    a[i + 1:] = reversed(a[i + 1:])
    return True


def brute_force():
    permutation = []
    new_len = 0
    last_visited_city = 0

    for i in range(1, number_of_cities):
        permutation.append(i)

    for city in permutation:
        new_len += matrix[last_visited_city][city]
        last_visited_city = city

    new_len += matrix[last_visited_city][0]
    best_len = new_len
    best_route = copy(permutation)
    PRD = (100 * (new_len - OPT)) / OPT
    print(f"{new_len} {PRD:.2f}%")
    new_len = 0
    last_visited_city = 0

    while next_permutation(permutation):
        for city in permutation:
            new_len += matrix[last_visited_city][city]
            last_visited_city = city

        new_len += matrix[last_visited_city][0]

        if best_len > new_len:
            best_len = new_len
            best_route = copy(permutation)
            print("Found better route")

        PRD = (100 * (new_len - OPT)) / OPT
        print(f"{new_len}   {PRD:.2f}%")
        new_len = 0
        last_visited_city = 0

    final_route = [0]
    final_route.extend(best_route)
    final_route.append(0)

    print("")
    print(f"Koszt najlepszej sciezki {best_len}")
    print(f"Najlepsza sciezka{final_route}")


brute_force()
