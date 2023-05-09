class QuizBrain:
    # Initializing the question list and question num
    def __init__(self, q_list):
        self.question_num = 0
        self.score = 0
        self.question_list = q_list

    # Method that is called upon to provide a 'true' or 'false' regarding if there are more questions
    def still_has_questions(self):
        total_questions = len(self.question_list)
        return self.question_num < total_questions

    # Method to call upon the next question in the list of Question objects provided
    def next_question(self):
        current_question = self.question_list[self.question_num]
        # Increasing the question num prior to input so the text is correct (e.g. Q.1, not Q.0)
        self.question_num += 1
        # Prompting the user to answer the provided question
        user_guess = input(f"Q.{self.question_num} {current_question.text} (True or False?): ").lower()
        self.check_answer(guess=user_guess, answer=current_question.answer)

    # Method that is called upon to check the answers made by the user
    def check_answer(self, guess, answer):
        if guess == answer.lower():
            print("Correct! You got it right!")
            self.score += 1
        else:
            print("Sorry, that is wrong...")

        print(f"The answer for the question was: {answer}.")
        print(f"Your current score is {self.score}/{self.question_num}")
        print("\n")

