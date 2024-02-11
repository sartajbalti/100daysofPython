#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open(r"./Input/Names/invited_names.txt", 'r') as file:
    c = file.readlines()
    names = [x.strip('\n') for x in c ]
print(names)

starting_letters = r'./Input/Letters/starting_letter.txt'
ready_to_send = './Output/ReadyToSend/'



for name in names:
    with open(starting_letters, 'r') as template:
        content = template.read()
        newContent = content.replace('[name]', name)
        print(newContent)
        filename = ready_to_send +"letter_for_"+ name + '.txt'
        with open(filename, 'w') as f:
            f.write(newContent)