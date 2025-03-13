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
#this will create an empty list na naay length
display_word = ['_' for _ in hidden_word]

while game_is_on and lives > 0:
  
  print(f"Word: {' '.join(display_word)}")
  print(f"Lives left: {lives}")
  
  guess = input("Make a letter guess: ").lower()

  if guess in letter_list:
    # removing of elements
    for index, letter in enumerate(hidden_word):
        if guess == letter:
          display_word[index] = letter
          letter_list.remove(letter)
  else:
    print("Wrong!")
    lives -= 1
    if stages:
      #print status
      print(stages.pop())
      
  if "_" not in display_word:
    game_is_on = False
    print("No more letters left")
    print(f"You survived, hidden work: {hidden_word}")

if lives <= 0:
  print("Game Over!")
  print(f'Right word: {hidden_word}')




