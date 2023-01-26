from replit import clear
import art

Bidding_game={}
next = True

def bid(name, price):
  Bidding_game[name] = price
  
while next:
  print(art.logo)
  Name = input("What is the bidder name? : ")
  bid_amt = int(input('How much are you going to bid? : '))
  bid(Name,bid_amt)
  next_player= input('Is there anyone world would like to bid? Yes or No. : ').lower()
  if next_player == 'no':
    next = False
  elif next_player == "yes":
    clear()
# finding the highest bid   
total_bids= Bidding_game.values()    # type = dict_values
winning_bid = max(total_bids)        # type = int
# finding the highest bidder 
for i in Bidding_game:
  if Bidding_game[i] == winning_bid:
    winner = i
print(f'\nCongratulations!!!\n{winner} wins the bid with ${winning_bid}')