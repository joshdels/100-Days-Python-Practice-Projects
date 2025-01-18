import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

game_is_on = True
lives = 6

word_list = ["aardvark", "baboon", "camel"]


hidden_word = random.choice(word_list)
letter_list = list(hidden_word)
display_word = ["_"] *len(hidden_word)

while game_is_on and lives >= 0:
    print(" ".join(display_word))
    

    guess = input("Make a letter guess: ").lower()

    if guess in letter_list:
      # removing of elements
      for letter in letter_list:
          if guess == letter:
              letter_list.remove(letter)
              display_word[letter] = guess # need to debug this part
    else:
      print("Wrong!")
      lives -= 1

      #print status
      print(stages.pop())

    if len(letter_list) <= 0:
      game_is_on = False
      print("No more letters left")
      print("You survived")

print("Game Over!")





