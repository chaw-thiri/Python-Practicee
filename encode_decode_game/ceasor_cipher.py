# python 3
# ceasar cipher : encrypting and decoding words.
from replit import clear
import caesar_art as CA

total_alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]
def ceasor(text_input,no_of_moves, direction):
  new_code = ''
  for alphabet in text_input: 
      if alphabet in total_alphabet:
        old_position = total_alphabet.index(alphabet)
        if direction == 'encode':
          new_position = old_position + no_of_moves
        elif direction == 'decode':
          new_position = old_position - no_of_moves
        new_code += total_alphabet[new_position]
      else:
          new_code += alphabet
  return new_code

while True:
  print(CA.logo)
  direction = input("""\n\nType 'encode' to encrypt, 'decode' to decrypt, or 'exit' to end:
  \n""").lower()
  if direction == 'exit':
    break
    
  text = input("Type your message:\n").lower()
  
  shift = int(input("Type the shift number:\n"))
  if shift > 26:
    shift = shift % 26

  if direction == 'encode':
    print(f'The encrypted code is {ceasor(text,shift,direction)}')
  elif direction == 'decode':
    print(f'The original code is {ceasor(text,shift,direction)} ')
  else:
    print("ERROR")
clear()
print('Thank you for using our service. ')
  



  





