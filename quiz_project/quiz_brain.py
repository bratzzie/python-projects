class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.user_score = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f"\nQ{self.question_number + 1}: {current_question.text} (True/False)? ")
        self.question_number += 1
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number != len(self.question_list)

    def check_answer(self, actual_answer, correct_answer):
        if actual_answer.lower() == correct_answer.lower():
            self.user_score += 1
            print("You got it right!")
        else:
            print("That's wrong...")
            print(f"The correct answer was: {correct_answer}")

        print(f"Your current score is: {self.user_score}/{self.question_number}")

    def complete_quiz(self):
        print("\nYou've completed the quiz!!!")
        print(f"Your final score is : {self.user_score}/{self.question_number}")
