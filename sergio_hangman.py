import random

stages = ['''
  +---+
  | |
  O |
 /|\|
 / \|
    |
=========
''', '''
  +---+
  | |
  O |
 /|\|
 /  |
    |
=========
''', '''
  +---+
  | |
  O |
 /|\|
    |
    |
=========
''', '''
  +---+
  | |
  O |
 /| |
    |
    |
=========
''', '''
  +---+
  | |
  O |
  | |
    |
    |
=========
''', '''
  +---+
  | |
  O |
    |
    |
    |
=========
''', '''
  +---+
  | |
    |
    |
    |
    |
=========
''']

end_of_game= False
word_list = ["bubbles", "bentley", "spot"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

display = []
for _ in range(word_length):
    display += "_"
    
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives = lives - 1
    print(f"{''.join(display)}")
    
    if "_" not in display:
        end_of_game = True
        print("You win!")
    
    while lives > 0 and guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        print(f"you have {lives} lives remaining")
        if lives == 0:
            print("you lose!")
            end_of_game = True
        break