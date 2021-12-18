
# Traveling Salesman Problem

This project includes few approaches of solving TSP problem.


## Approaches
BruteForce,
Branch and Bound, Simulated Annealing

## Usage

To use this program just run UserPanel.py script and write name of file with .tsp or.atsp  extenstions. Examples of files you will find in folder 'test_files'.

```python
def menu():
    running = True

    while running:
        print("")
        print("Choose way to solve the TSP: ")
        print("Type 1 for Brute Force approach")
        print("Type 2 for Branch and Bound approach")
        print("Type 3 for Simulated Annealing approach")
        print("Type 4 to end program")
        number = input("Chose number: ")
        print("")

        if number == "1":
            os.system('BruteForce.py')

        elif number == "2":
            os.system('Branch_and_Bound.py')

        elif number == "3":
            os.system('SimulatedAnnealing.py')

        elif number == "4":
            running = False
            print("END")

        else:
            print("You have to chose number from 1 to 4!")


menu()
```