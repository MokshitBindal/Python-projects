from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for data in question_data:
    text = data["question"]
    answer = data['correct_answer']
    new_question = Question(text, answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_list=question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You have completed the quiz with score of {quiz.score}/{quiz.question_number}.")
