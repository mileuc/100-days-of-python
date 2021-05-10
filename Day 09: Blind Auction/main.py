from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

#print logo
print(logo)

#empty dictionary of bidders and their bid amounts
bids = {}
#boolean that indicates if there are more bidders
more_bidders = True
#variable to store the highest bid and bidder
winner = ""
winning_bid = 0


while more_bidders:
  #get name of bidder and their bid amount
  name = input("What is your name?: ")
  bid = float(input("What is your bid?: $"))

  #adding name and bid amount to dictionary
  bids[name] = bid

  #loop through current bids and find the highest bidder
  for bidder in bids:
    current_bid = bids[bidder]
    #print(type(current_bid))
    if current_bid > winning_bid:
      winning_bid = current_bid
      winner = bidder

  #ask if there are any other bidders
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

  #if there are no other bidders
  if other_bidders == 'no':
    more_bidders = False
    clear()
    winning_bid = "{:.2f}".format(winning_bid)
    print(f"The winner is {winner} with a bid of ${winning_bid}.")
  else:
    clear()
  
