# Importing Modules and Libraries
import random
from question_model import Question
from data import question_data_videogames, question_data_computers
from quiz_brain import QuizBrain


# This function takes in the inputted data banks from the data.py and returns a list of Question() objects
def fill_question_bank(data_bank):
    # A temporary list variable that we will be using to return the list of Question() objects
    data = []
    # The for loop that will iterate through all the questions of the data bank provided
    for question in data_bank:
        # Create temporary variables to store the text and answers of question_data
        # Grabs the question info using the 'text' dic key
        question_text = question["question"]
        # Grabs the question answer using the 'answer' dic key
        question_answer = question["correct_answer"]
        # Then create a temporary Question object variable that has the temp vars for question_data's info
        new_question = Question(q_text=question_text, q_answer=question_answer)
        # Finally, add this temp object to the question_bank list
        data.append(new_question)
    # Return the list called data so that you can fill in the data banks in the main function
    return data


# Setting up Question data bank list, which will be a list of Question() objects
question_bank = []
question_bank_2 = []
chosen_question_bank = []
# Calling the fill question bank func to provide the data from data.py
question_bank = fill_question_bank(question_data_videogames)
question_bank_2 = fill_question_bank(question_data_computers)

# Prompt Users to choose between a quiz on video games or computers
data_pick = input("Welcome to the QUiz Game! Would you like to take a quiz on video games or computers? "
                  "input 'v' or 'c': ").lower()
if data_pick == "v":
    chosen_question_bank = question_bank
else:
    chosen_question_bank = question_bank_2


random.shuffle(chosen_question_bank)
quiz = QuizBrain(q_list=chosen_question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("Thank you for completing out Quiz!")
print(f"Your final score was {quiz.score}/{quiz.question_num}")
