from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

Question_bank = []


for item in question_data:
    question = item['question']
    answer = item['correct_answer']
    QUESTION = Question(question, answer)
    Question_bank.append(QUESTION)


quiz = QuizBrain(Question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz !")
print(f"Your final score is {quiz.score}/{len(Question_bank)}")
