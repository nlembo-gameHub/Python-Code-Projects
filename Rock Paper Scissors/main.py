#Imported Modules
import random;

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Setting up Game List
game_images = [rock, paper, scissors];
#Player Choice Setup
player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n");
player_choice = int(player_choice);
#Making sure the player does not choose something beyond the list's scope
if (player_choice >= 3 or player_choice < 0):
  print("You typed an invalid number, you lose!");
else:
  print("You chose:");
  print(game_images[player_choice]);
  
  #Computer Choice Setup
  computer_choice = random.randint(0, 2);
  
  print("Computer chose:");
  print(game_images[computer_choice])
  
  #Comparing Choices
  if (player_choice == 0 and computer_choice == 2):
    print("You Win!");
  elif (computer_choice == 0 and player_choice == 2):
    print("You Lose.");
  elif (computer_choice > player_choice):
    print("You Lose.");
  elif (player_choice > computer_choice):
    print("You win!");
  elif (computer_choice == player_choice):
    print("You both draw.");
