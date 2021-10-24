class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question = question_list
        self.points = 0

    def still_got_questions(self):
        if self.question_number < len(self.question) - 1:
            return True

    def new_question(self):
        current_question = self.question[self.question_number]
        ans = input(f"Q.{self.question_number}: {current_question.text} (True or False)").title()
        self.question_number += 1
        self.chk_answer(ans)

    def chk_answer(self, answer):
        current_question = self.question[self.question_number]
        if answer == current_question.answer:
            self.points += 1
            print(f"Correct Answer, You Have {self.points} Points")
        else:
            print(f"Wrong Answer, You Have {self.points} Points")
            # print(current_question.answer)

    def score(self):
        return self.points
