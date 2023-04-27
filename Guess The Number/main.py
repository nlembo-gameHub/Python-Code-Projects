import random;
from art import logo;
from replit import clear

#Global Constants
EASY_DIFF_TURNS = 10;
HARD_DIFF_TURNS = 5;

#Functions

#Set Difficulty Function
def set_difficulty():
  difficulty_type = input("Choose a difficult. Type 'easy' or 'hard': ").lower();
  
  if(difficulty_type == "easy"):
    turns = EASY_DIFF_TURNS;
  else:
    turns = HARD_DIFF_TURNS;

  return turns;

#Random Number Function
def random_num_generator(min, max):
  rnd_num = random.randint(min, max);
  return rnd_num;

#Input Handling
def input_handling():
  while True:
    try:
      num = int(input("Make a guess: "));
      break;
    except ValueError:
      print("Please input integer only...");
      continue;
  return num;

#Comparison Function
def compare(input, number):
  if(input == number):
    print(f"\nCorrected, the answer was {number}. You win!\n")
    return True;
  elif(input < number):
    print(f"\nToo low, Guess Again!");
    return False;
  elif(input > number):
    print(f"\nToo high, Guess Again!");
    return False;

def guessing_game():
  #Main Function
  print(logo);
  #Variables
  game_over = False;
  guess_min = 1;
  guess_max = 100;
  #Intro Text
  print("Welcome to the Number Guessing Game!");
  print(f"I'm thinking of a nnumber between {guess_min} and {guess_max}");
  #Ask for Difficult selection
  attempts = set_difficulty();
  
  #Number is generator
  answer = random_num_generator(guess_min, guess_max);

  #Guessing Loop
  while not (game_over):

    #Player Picks Number
    print(f"You have {attempts} attempts remaining to guess the number.");
    player_guess = input_handling();
  
    game_over = compare(player_guess, answer);
    
    if attempts == 0:
      game_over = True;
    elif not game_over:
      attempts -= 1;

  if attempts <= 0:
    print("You ran out of lives, better luck next time!");

while input("Wanna Guess Numbers? Type 'y' or 'n': ").lower() == "y":
  clear();
  guessing_game();
  