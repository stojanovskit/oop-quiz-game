from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for dat in question_data:
    question_text = dat["text"]
    question_answer = dat["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
brain = QuizBrain(question_bank)

while brain.still_got_questions():
    brain.new_question()
print("You've completed the quiz")
print(f"your final score was {brain.score()}")
