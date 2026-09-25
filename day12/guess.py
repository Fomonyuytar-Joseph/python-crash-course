import random

print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100.")

random_number = random.randint(1,100)
print(random_number)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard: ")

if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5

game_ended = False

while not game_ended:
    print(f"You have {attempts} attempts to guess the number.")
    guess = int(input("Make a guess: "))

    if guess > random_number:
        print("Too high")
        attempts -= 1
    elif guess < random_number:
        print("Too Low")
        attempts -= 1
    else:
        print("You win🎉")
        game_ended = True

    # attempts-=1

    if attempts < 1:
        print("Sorry you have ran out of luck!😥")
        game_ended = True
         

