import BuildMatrix


def menu():
    print("To start program choose testing file: ")
    file_name = input()
    matrix, opt = BuildMatrix.create_matrix(file_name)

    while True:
        print(f"You are using file '{file_name}' ")
        print(" ")
        print(f"Matrix: {matrix}")
        print(f"opt: {opt}")
        break


menu()
