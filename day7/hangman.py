import random
from hangman_art import logo , stages
from hangman_words import word_list


chosen_word = random.choice(word_list)
display = []
word_length = len(chosen_word)
lives = 6
end_of_game = False

print(logo)

print(chosen_word)

for word in chosen_word:
    display+='_'



while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
       print(f"You've already guessed: {guess}")


    for position in range(0, word_length):
      letter = chosen_word[position]
      # print(f"Current position:{position}\n Current letter: {letter}\n Guessed letter: {guess}")
      if letter == guess:
        display[position] = letter

 

    if guess not in chosen_word:
       print(f"You guessed {guess} word that is not in the word. You lose a life Ooops!")
       lives-=1
       if lives == 0:
          end_of_game = True
          print("Game Over!")

    print(f"{' '.join(display)}")


    if '_' not in display:
       end_of_game = True
       print("You win!")

    print(stages[lives])