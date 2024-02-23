# List Comprehension 

# case where we create a new list from previous lists 
list = [1,2,3]
new_list = [i+1 for i in list]
# print(new_list)
name = "Sartaj"
new = [i for i in name]
# print(new)

x = [i*2 for i in range(1,5)]
# print(x)

# Conditional list comprehension

n = [i*2 for i in range(1,20) if i%2 == 0]
# print(n)

nam = ["Sartaj", "Zakir","Nam"]

new_name = [i.upper() for i in nam if len(i)>=5]
# print(new_name)

with open('./Day26_List_comprehension/file1.txt') as f1:
  data = f1.readlines()
  dat = [int(i) for i in data]
# print(dat)

# Dictionary comprehension
import random 
students_scores = {i:random.randint(1,100) for i in  nam}
print(students_scores)
pass_students= {i:n for (i,n) in students_scores.items()if n>=60}
print("Passed Students are : ", pass_students)
# sentence = input()
# 🚨 Don't change code above 👆
# Write your code below 👇
# new_sentence = sentence.split(' ')
# print(new_sentence)

#  iterates over pandas dataframe 
import pandas as pd 
student_dict={"student":["Sartaj", "Zakir","Nam"],"score":[89,74,92]}
df = pd.DataFrame(student_dict)
# loop trough each row of pandas dataframe
# for (index,row) in df.iterrows():
#     print(row.score)

a = {index:row for (index,row) in df.iterrows()}
print(a)


# Nato alphabate project 


# Initialize an empty dictionary to store the NATO phonetic alphabet
nato_dict = {}

# Open the CSV file and read its contents
data = pd.read_csv("./Day26_List_comprehension/nato_phonetic_alphabet.csv")

p_data = {row.letter:row.code for (index,row) in data.iterrows()}
print(p_data)

namee = input("Enter a word:").upper()
# li_name = [namee for namee in namee]
li_name = [p_data[key] for key in namee]
print(li_name)


# Print the resulting dictionary

