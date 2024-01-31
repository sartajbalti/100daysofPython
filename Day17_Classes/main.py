# Creating Classes
# Class is a blueprint to create and object
# Custom classes

# class Users:
# # Constructor what should happend if the obejct is created
# # __init__ function.
#     def __init__(self,user_id,username):
#         self.user_id = user_id
#         self.username = username
#         # default value 
#         self.followers = 0
#         self.following = 0
#         print(f"new user created")

#     # Adding methods 
#     def follow(self,user):
#         user.followers +=1
#         self.following +=1
# user_1 = Users("001","Balti")
# user_2 = Users("002","Raja")
# user_1.follow(user_2)
# # user_1.user_id = "001"
# # user_1.username = "Balti"
# print(user_1.following)
# print(user_2.followers)

# Quiz Game 
from data import question_data1
from question_model import Question
from quiz_brain import Quiz
question_bank =[]
for data in question_data1:
    new_question = Question(data['question'],data['correct_answer'])
    question_bank.append(new_question)
# print(question_bank[0].text)
quiz= Quiz(question_bank)
# print(quiz.question_list[0].text)
while quiz.still_has_question(): 
    # print(quiz.still_has_question())
    quiz.next_question()

print("You've Completed the quiz")
print(f"Your Final Score was: {quiz.score}/{quiz.question_no}")






