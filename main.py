import numpy as np

matrix = np.matrix

file_name = 'a280.tsp'
file_path = 'test_files/' + file_name

with open(file_path, 'r') as f:

    for count, line in enumerate(f):
        pass

    f.seek(0)
    index_of_line = 0
    last_line_index = count
    OPT = 0

    for line in f:
        if index_of_line == last_line_index:
            OPT = int(line)

        if index_of_line >= 2:
            print(line)

        index_of_line += 1








