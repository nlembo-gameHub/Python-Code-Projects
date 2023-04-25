#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = "";
#Get letters into password
for char in range(1, nr_letters + 1):
  #1 to number of letters
  password += random.choice(letters);
#Get symbols into password
for symbol in range(1, nr_symbols + 1):
  #1 to number of symbols
  password += random.choice(symbols);
#Get numbers into password
for symbol in range(1, nr_numbers + 1):
  #1 to number of numbers
  password += random.choice(numbers);

print(f"Your password is: {password}");
# You could use the following instead of random.choice(): 
# random_element = random.randint(0, len(letters) - 1)
# generated_password += letters[random_element];

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#Make password_list a list
password_list = [];
password_shuffled = "";
#Get letters into password
for char in range(1, nr_letters + 1):
  #1 to number of letters
  password_list.append(random.choice(letters));
#Get symbols into password
for symbol in range(1, nr_symbols + 1):
  #1 to number of symbols
  password_list.append(random.choice(symbols));
#Get numbers into password
for symbol in range(1, nr_numbers + 1):
  #1 to number of numbers
  password_list.append(random.choice(numbers));

#Instead of using random.shuffle(password_list) I used the Fisher–Yates shuffle Algorithm 
# Start from the last element and swap one by one. We don't
# need to run for the first element that's why i > 0
password_length = len(password_list);
for i in range(password_length - 1, 0, -1):
  # Pick a random index from 0 to i
  j = random.randint(0, i + 1);
  
  # Swap arr[i] with the element at random index
  password_list[i], password_list[j] = password_list[j], password_list[i]

for char in password_list:
  password_shuffled += char;
print(f"Your shuffled password is: {password_shuffled}");