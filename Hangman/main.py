#Importing the modules and contents within them
import random
from hangman_words import word_list
from hangman_art import logo, stages
#Setting up the chosen word and the getting its word length
chosen_word = random.choice(word_list);
word_length = len(chosen_word);
#Setting up comparison variables used against the user input
letter = "";
guess = "";
#Creating the game-monitoring variables for win-lose conditions
end_of_game = False;
lives = 6;

#Set up the game logo
print(logo);

#print(f'Pssst, the solution is {chosen_word}.')

#Setting up and creating the '_' for the hidden words
hidden_word_list = []
for _ in range(word_length):
    hidden_word_list.append("_");

while not end_of_game:
    guess = input("Guess a letter: ").lower();
    #The If-Statement allows us to check and see if it's a repeat guess by checking the 
    #letter compared to the revealed letters in the hidden_word_list
    if (guess in hidden_word_list):
      print(f"You've already gussed {guess}");
    #Checking the guess compared to the letters of the word
    
    for position in range(word_length): #For loop that goes up to the length of the word
      #Sets the letter variable = to the chosen_word at the current position
        letter = chosen_word[position]; 
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}");
        #Checks to see if the current letter is = to the guess
        if (letter == guess):
          #If so, we set the hidden_word_list of the current position equal to the letter
            hidden_word_list[position] = letter; #This removes the '_' and replaces it with the letter

    #Check if user is wrong.
    if (guess not in chosen_word):
        lives -= 1 #Subtract the lives
        print(f"You guessed {guess}, that's not in the word. You now have {lives} / 6 lives")
        if (lives == 0): #check if lives equal 0 for a game over
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(hidden_word_list)}");

    #Check if user has got all letters.
    if ("_" not in hidden_word_list):
        end_of_game = True;
        print("You win.");

#Use lives as the element index to print the different hangman drawings
    print(stages[lives]); 