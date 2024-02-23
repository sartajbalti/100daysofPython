# # Working with Pandas 
# # USA states names 
# #  Reading CSV Data 
# # import pandas as pd 
# # data = pd.read_csv('weather_data.csv')
# # with open('weather_data.csv') as f:
# #     da = f.readlines()
# #     # split the data
    
# # print(da)
# # import csv 
# # with open('weather_data.csv') as data_file:
# #     data = csv.reader(data_file)
# # # store the temperature
# #     temp =[]
# #     for row in data:
# #         if row[1]!='temp':
# #             temp.append(int(row[1]))
# # print(temp[:])

# # now work with pandas 
# import pandas as pd 
# data = pd.read_csv('weather_data.csv')
# # print(data['temp'])
# # print(type(data))
# data_dict = data.to_dict()
# # print(data_dict)

# data_list = data['temp'].to_list()
# # print(data_list)
# # sum = 0
# # for i in range(len(data_list)):
# #     sum += data_list[i]
# sum = sum(data_list)  
# average = sum / len(data_list)
# # print(average)

# # print(data['temp'].mean())
# # print(data['temp'].median())
# # print(data['temp'].max())

# # Get hold of data in column 

# # print(data.condition)
# # print(data[data.day=='Monday'])
# max = data.temp.max()
# # print(data[data.temp == max])

# monday = data[data.day=='Monday']
# # monday_temp = monday.temp 
# fah = monday.temp *1.8+32 
# print(fah)

# # Create Dataframe from strach 
# data_dict = {"student":['amy','james'],"score":[95,76]}
# df = pd.DataFrame(data=data_dict)
# # df.to_csv("new_data.csv", index = False)

import pandas as pd
# sq = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# # print(sq.head(5))
# # print(sq['Primary Fur Color'])
# count = sq[sq['Primary Fur Color']=='Gray'].count()
# gray_count = count['Primary Fur Color']
# count2 = sq[sq['Primary Fur Color']=='Cinnamon'].count()
# cinnamon_count = count2['Primary Fur Color']
# count3 = sq[sq['Primary Fur Color']=='Black'].count()
# black_count = count3['Primary Fur Color']
# da_dic = {'Fur Color':['gray','red','black'], 'Count': [gray_count,cinnamon_count,black_count]}
# df = pd.DataFrame(data = da_dic)

# df.to_csv('squiral_count.csv',index=False)

#  US States quiz 
import turtle

screen = turtle.Screen()
screen.title('US States Game')
# image on screen 
image = './Day25_US_states_name/blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
guess_states = []
state = pd.read_csv('./Day25_US_states_name/50_states.csv')

while len(guess_states)<50:
    answer_state = screen.textinput(f'{len(guess_states)}/50 Correct Guessed States',"What's another state name?").title()
    # print(state)
    if answer_state == "Exit":
        not_in_list = [sta for sta in state if sta not in guess_states ]
        df2 = pd.DataFrame(not_in_list)
        df2.to_csv("./Day25_US_states_name/StatesLeft.csv", index=False)
        print(df2)
        break
    for st in state.state:
        if st == answer_state:
            # print(state)
            
            s = state[state.state == answer_state]
            guess_states.append(s.state.item())
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.setposition(int(s.x),int(s.y))
            t.write(s.state.item())
      
        # print the answer in the screen x, y coordinates
# states that are not in the list of guessed states and save into new csv file 


    
    # else:
    #     print('Wrong!')
        
# def get_mouse_click_cor(x,y):
#     print(x,y)
    
# turtle.onscreenclick(get_mouse_click_cor)
# turtle.mainloop()
screen.exitonclick()
