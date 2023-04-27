#Libraries
from art import logo
from replit import clear
import random

#Variables
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10];

#Functions
def deal_card(deck):
  random_card = random.choice(cards);
  return random_card;

#Revealing hand
def reveal_hand(p_hand, c_hand, p_score, c_score, final_reveal):
  if not final_reveal:
    print(f"\n  Your current hand: {p_hand}, current score: {p_score}");
    print(f"  Computer's current hand: {c_hand[0]}");
  else:
    print(f"\n  Your final hand: {p_hand}, final score: {p_score}");
    print(f"  Computer's final hand: {c_hand}, final score: {c_score}");

#Calculating the Score
def calculate_score(cards):
  hand_size = len(cards);
  score = sum(cards);
  
  if (score == 21 and hand_size == 2):
    print("Blackjack!");
    score = 0;

  if (11 in cards and score > 21):
    cards.remove(11);
    cards.append(1);
    score = sum(cards);

  return score;
#Comparing the Scores
def compare_scores(player, computer):
  if (player == computer):
    return "Both Player and Computer have equal scores! Computer wins.";
  elif (computer == 0 or computer == 21):
    return "You Lose, opponent has Blackjack.";
  elif (player == 0 or player == 21):
    return "You Win with a Blackjack!";
  elif player > 21:
    return "You went over 21. You Lose."
  elif computer > 21:
    return "Computer went over. You Win!";
  elif player > computer:
    return "Your score is higher, you win!";
  else:
    return "You Lose.";

def play_game():
  #Lists
  player_cards = [];
  computer_cards = [];
  #Ints
  beginning_deal = 2;
  player_score = 0;
  computer_score = 0;
  #Bools
  player_turn_over = False;
  #Main Program/Initial Dealing
  for x in range(beginning_deal):
    player_cards.append(deal_card(deck = cards));
    computer_cards.append(deal_card(deck = cards));
  
  #Player Turn Loop
  while not player_turn_over:
    #Calculate the scores of the player and the computer
    player_score = calculate_score(player_cards);
    computer_score = calculate_score(computer_cards);
    
    reveal_hand(player_cards, computer_cards, player_score, computer_score, False);
    
    if (player_score == 0 or computer_score == 0 or player_score > 21):
      print("Game Over!");
      player_turn_over = True;
    else:
      user_should_deal = input("\nType 'y' to get another card, type 'n' to pass: ").lower();
      if (user_should_deal == "y"):
        player_cards.append(deal_card(deck = cards));
      else:
        player_turn_over = True;
  
  #Computer Turn Loop
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card(deck = cards));
    computer_score = calculate_score(computer_cards);
  
  reveal_hand(player_cards, computer_cards, player_score, computer_score, True);
  
  print(compare_scores(player_score, computer_score));

#Replay Game
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
  clear();
  print(logo);
  play_game();