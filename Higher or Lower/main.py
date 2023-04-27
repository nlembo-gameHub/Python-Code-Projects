#Libraries
from game_data import data
from art import logo, vs
import random
from replit import clear

#Functions
#Random Option Generation Function
def get_random_option():
  #Generate a random data object from the game_data script
  return random.choice(data)
#Data Formating Function
def formatted_data(option):
  #Format the data
  name = option["name"]
  description = option["description"]
  country = option["country"]
  #follower_count = option["follower_count"]
  #formatted_data = f"{name}, a/an {description}, from {country}, with {follower_count}"
  formatted_data = f"{name}, a/an {description}, from {country}"
  
  return formatted_data

#Ensures user inputs one of the two correct options
def user_input_check():
  correct_input = False
  while not correct_input:
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if guess == 'a' or guess == 'b':
      correct_input = True
  return guess
  
#Checking the Guess the user made
def check_guess(guess, a_followers, b_followers):
  if a_followers > b_followers: 
    return guess == "a" #if a > b and guess was a return True, else return false
  else:
    return guess == "b" #if b > a and  guess was b return True, else return false

#The Game Logic Function
def game_start():
  #Variable set up
  score = 0
  continue_game = True
  #The random options from the data sheet
  option_a = get_random_option()
  option_b = get_random_option()
  while continue_game:
    #Sets up the first matchup generation
    option_a = option_b
    option_b = get_random_option()
    while option_a == option_b:
      option_b = get_random_option()
    
    #Setting up the Option Display
    print(f"Compare A: {formatted_data(option_a)}")
    print(vs)
    print(f"Compare B: {formatted_data(option_b)}")

    #Prompting the User for their input
    guess = user_input_check()

    #Retrieving the option follower counts
    follower_count_a = option_a["follower_count"]
    follower_count_b = option_b["follower_count"]

    correct_answer = check_guess(guess, follower_count_a, follower_count_b)
    
    clear()
    print(logo)

    if correct_answer:
      score += 1
      print(f"You're right! Current score: {score}")
    else:
      continue_game = False
      print(f"Sorry, that's the wrong answer. Final score: {score}")
    
#Main Function
game_start()