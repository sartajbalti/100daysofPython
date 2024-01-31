class Quiz:
    def __init__(self,question_list):
        self.question_no = 0
        self.score = 0
        self.question_list = question_list
    def still_has_question(self):
        return self.question_no<len(self.question_list)

    def next_question(self):
        
        current_question= self.question_list[self.question_no]
        correct_answer = current_question.answer
        self.question_no+=1
        user_answer = input(f"Q.{self.question_no}: {current_question.text}.(True/False)?: ")
        self.check_answer(user_answer,correct_answer)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower()==correct_answer.lower():
            self.score+=1
            print("You got it right!")
        else:
            print("That is wrong.")
        print(f"The correct answer was: {correct_answer}\nYour Current score is : {self.score}/{self.question_no}")
        print()
    
        