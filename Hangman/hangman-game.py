# python 
# hangman game
import random
import hangman_art
import hangman_word
from replit import clear

chosen_word =random.choice(hangman_word.word_list)
display_list=[]
used_guess = []
lives = 6
status = True

def win():
  if '_' not in display_list:
    print("Congratulations")
    global status 
    status = False

def lose():
  if lives == 0:
    print(hangman_art.stages[lives])
    print('You lose')
    print(f'The correct answer is {chosen_word}')
    global status 
    status = False

def check():
  global used_guess
  if guess in used_guess:
    print(f'You have already guessed {guess}. Please try another alphabet.')
  else:
    used_guess += guess
  for i in range(len(chosen_word)):
    if chosen_word[i] == guess:
      display_list[i] = guess
      
  if guess not in chosen_word:
    global lives 
    print(hangman_art.stages[lives])
    lives -= 1
    print(f"{guess} is not in the chosen word.")
    print(f"You have {lives} lives remained.")
  print(''.join(display_list))
  win()
  lose()

print(hangman_art.logo)
# displaying _ for number of alphabets
for i in range(len(chosen_word)):
  display_list.append('_')
print(''.join(display_list))

# asking alphabet from the user 
while status:
  guess = input("\nGuess the letter: ").lower()
  clear()
  check()
  print('..................................................')
  
    


