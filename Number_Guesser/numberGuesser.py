import random

random_number = random.randint(1, 100)

first_guess = input("Guess the number I'm thinking of between 1 to 100: ")
if first_guess != random_number:
    print("incorrect! were off by"), print(int(first_guess) - int(random_number))