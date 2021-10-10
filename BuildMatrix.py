import numpy as np


def create_matrix(file_name):
    file_path = 'test_files/' + file_name
    matrix = []
    OPT = ""

    with open(file_path, 'r') as f:
        for count, line in enumerate(f):
            pass

        f.seek(0)
        index_of_line = 0
        last_line_index = count

        for line in f:
            if index_of_line == last_line_index:
                for char in line:
                    OPT += char
                OPT = int(OPT)

            elif index_of_line >= 2:
                number = ""
                matrix_row = []

                for char in line:
                    if char != " ":
                        number += char
                    else:
                        if number != "":
                            matrix_element = int(number)
                            number = ""
                            matrix_row.append(matrix_element)

                matrix_row.append(number)
                matrix.append(matrix_row)

            index_of_line += 1
    matrix = np.array(matrix, dtype='int16')
    return matrix, OPT
