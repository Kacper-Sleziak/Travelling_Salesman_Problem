import os


def menu():
    running = True

    while running:
        print("")
        print("Choose way to solve the TSP: ")
        print("Type 1 for Brute Force approach")
        print("Type 2 for Branch and Bound approach")
        print("Type 3 for Simulated Annealing approach")
        print("Type 4 for Genetic Algorithm approach")
        print("Type 5 to end program")
        number = input("Chose number: ")
        print("")

        if number == "1":
            os.system('BruteForce.py')

        elif number == "2":
            os.system('Branch_and_Bound.py')

        elif number == "3":
            os.system('SimulatedAnnealing.py')

        elif number == "4":
            os.system('GeneticAlgorithm.py')

        elif number == "5":
            print("END")

        else:
            print("You have to chose number from 1 to 5!")


menu()
