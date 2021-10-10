import numpy as np

matrix = np.matrix

file_name = 'a280.tsp'
file_path = 'test_files/' + file_name
matrix = np.matrix([])

with open(file_path, 'r') as f:
    for count, line in enumerate(f):
        pass

    f.seek(0)
    index_of_line = 0
    last_line_index = count
    OPT = ""

    for line in f:

        number = ""
        matrix_row = np.array([])
        print(f"Line index {index_of_line}")

        if index_of_line == last_line_index:
            for char in line:
                OPT += char
            OPT = int(OPT)
            print(OPT)

        elif index_of_line >= 2:
            for char in line:
                if char != " ":
                    number += char

                else:
                    if number != "":
                        matrix_element = int(number)     #numer do dodania do rzedu macierzy
                        np.append(matrix_row, matrix_element)
                        number = ""

            matrix_element = int(number)
            np.append(matrix_row, matrix_element)

        np.append(matrix, matrix_row)
        index_of_line += 1

print(matrix)
