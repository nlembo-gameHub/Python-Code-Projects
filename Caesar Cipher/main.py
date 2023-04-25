#Module Imports
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];

#Cypher and Decypher Function
def caesar(start_text, shift_amount, cipher_direction):
  #End result of the coded or decoded message
  end_text = "";
  alphabet_length = len(alphabet);
  #Checks if the user chose Decode
  if cipher_direction == "decode":
    #We'll multiple the shift amount by -1 to go in reverse for a decoded message
    shift_amount *= -1; 
  #A For loop that cycles through the entire word
  for char in start_text:
    #Checks to make sure the character is a letter in the alphabet
    if char in alphabet:
      #We'll get a starting position for the character
      position = alphabet.index(char);
      #once we do that we'll set a new position using a modulus of 26
      #this way if the user uses a shift amount higher than 26, it'l cycle through
      #the list so as to not get an out-of-bounds error
      new_position = (position + shift_amount) % alphabet_length;
      #finally, we will add the individual characters from the alphabet
      #to the text using the element position we calculated
      end_text += alphabet[new_position];
    else:
      #If it's a number or symbol, then we'll not cycle it through our list
      end_text += char;
  #We then print the final message whether it was encrypted or decrypted
  print(f"Here's the {cipher_direction}d result: {end_text}");

#Printing the Caesar Decypher Logo
print(logo);
#Set the end-condition bool/flag
should_continue = True;
#While loop will allow repetition for encryption/decryption program
while should_continue:
  #Direction in which the program should follow
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n");
  #The message in which the user wishes to alter
  text = input("Type your message:\n").lower();
  #Amout of letters in the alphabet to shift and move the individual letters
  shift = int(input("Type the shift number:\n"));
  #Calling the encoding and decoding function
  caesar(start_text = text, shift_amount = shift, cipher_direction = direction);
  #Set up the user choice to continue or end the program
  user_choice = input("Type 'yes' if you want to go again. Otherwise, type 'no'\n").lower();
  
  if (user_choice == "no"):
    should_continue = False;
    print("Thanks for playing! Goodbye and join again when you want!")