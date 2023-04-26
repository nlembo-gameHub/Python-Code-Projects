#Calculator
from replit import clear
from art import logo
#Functions
#Exception handling
def check_user_input(is_number, value_type):
  if(is_number):
    while True:
      try:
       #Takes in the bet value and converts it to an int
       user_input = float(input(f"What's {value_type} number?: "));
       break;
      except ValueError:
       print("Please input integer only...");
       continue;
  else:
    is_correct_operation = False;
    valid_symbols = ["+", "-", "*", "/"];
    while not is_correct_operation:
      user_input = input(f"Pick an {value_type} from the line above: ");
      for x in valid_symbols:
        if(user_input == x):
          is_correct_operation = True;
  
  return user_input;
#Add
def add(n1, n2):
  sum = n1 + n2;
  return sum;

#Subtract
def subtract(n1, n2):
  sum = n1 - n2;
  return sum;

#Multiply
def multiply(n1, n2):
  sum = n1 * n2;
  return sum;

#Divide
def divide(n1, n2):
  sum = n1 / n2;
  return sum;

#Dictionary
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
};
#Calculator Function
def calculator():
  print(logo);
  continue_calculation = True;
  
  num1 = check_user_input(is_number = True, value_type = "first");
  
  while continue_calculation: 
    for symbol in operations:
      print(symbol);
    operation_symbol = check_user_input(is_number = False, value_type = "operation");
    
    num2 = check_user_input(is_number = True, value_type = "second");
    
    calculation_function = operations[operation_symbol];
    answer = calculation_function(num1, num2);
    
    print(f"{num1} {operation_symbol} {num2} = {answer}");
  
    continue_choice = input("Would you like to keep using the calculator? 'y' or 'n': ").lower();
    if(continue_choice == 'n'):
      continue_calculation = False;
      print("Thanks for using the calculator!")
    else:
      clear();
      reuse_choice = input(f"Do you want to keep using previous answer {answer}? 'y' or 'n': ").lower();
    
      if(reuse_choice == "n"):
          calculator();
      else:
        num1 = answer;
        print(f"Your Answer from before: {num1}");


calculator();