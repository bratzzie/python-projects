from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from art import logo


def run_quiz():
    question_bank = []
    for q_data in question_data:
        question_bank.append(Question(q_data.get("text"), q_data.get("answer")))

    quiz = QuizBrain(question_bank)

    print("\nWelcome to our...")
    print(logo)
    print("Let's start!")
    while quiz.still_has_questions():
        quiz.next_question()
    quiz.complete_quiz()

    exit()


run_quiz()
