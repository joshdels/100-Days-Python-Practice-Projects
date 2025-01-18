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

word_list = ["aardvark", "baboon", "camel"]


choosen_word = random.choice(word_list)
letter_list = list(choosen_word)

# debug word selected
print(choosen_word) 

# User Guess section
guess = input("Make a letter guess").lower()

for letter in letter_list:
    if guess == letter:
        print(letter)
        # letter_list.pop(letter)
        break
    else:
        print('no letters found')





# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.
