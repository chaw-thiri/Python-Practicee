# python 
# rockpaperscissor game
import random
rock= '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper= '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors= '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


gameset=[rock,paper,scissors]
computer=random.choice(gameset)
user=input('Choose either rock(1) or  paper(2) or scissors(3): ')
if user=='1':
  user=rock
elif user=='2':
  user=paper
elif user=='3':
  user=scissors

if user==computer:
  print('user:',user)
  print("computer:",computer)
  print('DEAL')
elif user==rock and computer==paper:
  print('user:',user)
  print("computer:",computer)
  print('You lose')
elif user==rock and computer==scissors:
  print('user:',user)
  print("computer:",computer)
  print('You win')
elif user==scissors and computer==paper:
  print('user:',user)
  print("computer:",computer)
  print('You win')
elif user==scissors and computer==rock:
  print('user:',user)
  print("computer:",computer)
  print('You lose')
elif user==paper and computer==rock:
  print('user:',user)
  print("computer:",computer)
  print('You win')
elif user==paper and computer==scissors:
  print('user:',user)
  print("computer:",computer)
  print('You lose')
elif user!=rock or user!=paper or user!=scissors:
  print(user)
  print(computer)
  print('GAME OVER')
  
  
