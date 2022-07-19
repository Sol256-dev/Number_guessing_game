import random

max_number = input("Enter the maximum number: ")

if max_number.isdigit():
    max_number = int(max_number)

    if max_number <= 5:
        print("please enter a number greater than 4")
        quit()
else:
    print("please enter an integer")
    quit()

random_number = random.randint(0, max_number)

no_of_guesses = 0

while True:
    user_guess = input("Make a guess: ")

    no_of_guesses += 1

    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("please enter an integer")
        continue

    if user_guess == random_number:
        print("You guessed right!")
        break

    else:
        print("wrong guess!")
        continue

print("you made" ,no_of_guesses, "guess attempts")