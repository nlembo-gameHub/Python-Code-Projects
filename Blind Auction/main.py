from replit import clear
from art import logo
#Setting up Values
bids = {};
name = "";
continue_choice = "";
bid = 0;
continue_bidding = True;

#Functionn that will compare  the bids
def compare_bids(bidding_record):
  highest_bid = 0; #Set a place-holder for the current highest bid
  #The for loop look through the individual bidders in the dictonary bids
  #Bidder is the key to access the value of bid, we cycle through each one in the loop
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    #Once we have a bid amount, we compare it to the last known highest bid
    #this continues until we cycle through the dictionary
    if (bid_amount > highest_bid):
      highest_bid = bid_amount;
      winner = bidder;
  #We end the for loop and the final winner and highest bid is determined
  print(f"The winner is {winner} with a bid of ${highest_bid}");

while(continue_bidding):
  print(logo);
  
  name = input("What is your name?: ");
  #Ensure that the user is inputting an Integer
  while True:
    try:
      #Takes in the bet value and converts it to an int
      bid = int(input("what is your bid?: $")); 
      break;
    except ValueError:
      print("Please input integer only...");
      continue;
  #Sets the key 'name' to the inputted name and makes its value pair = the bid
  bids[name] = bid;
  #Prompt user to continue the bidding or not
  continue_choice = input("Are there any other bidders? Type 'yes' or 'no'. ").lower();
  #Check to see if the user wishes to add more bidders
  if(continue_choice == "no"):
    continue_bidding = False; #Set the bool to false to end the while loop
  else:
    clear(); #Clear the inputs made above
#Compare the bids in the function
compare_bids(bids);