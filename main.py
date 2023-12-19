from question_model import Question
from data import quiz_data, categories
from quiz_brain import QuizBrain

print("Choose a Category from the following.")
for key in categories:
    print(key)
usr_category = input("> ").title()
print("How many questions do you want?")
usr_amt = input("> ")
print("Choose a difficulty Easy, Medium, Hard")
usr_difficulty = input("> ").lower()
question_data = quiz_data(usr_category, usr_amt, usr_difficulty)

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the Quiz")
print(f"The final score is {quiz.score}/{quiz.question_number}")
