import random
from QA import responses
from prediction import related



print("ChatBot: What is your name?")
user_input = input().title()   #converted the input to tite case in other to match the responses in the dictionary
print("Hello " + user_input + ', nice to meet you, what do you want to know?')

name = "I.T.K"
weather = "Rainy"
mood = "Happy!"

chatbot_template = name + " : {0}" 
user_template  = user_input + " : {0}"
#{0} is gotten from format function, this substitute the variable given. replaces the placeholders that are passed as parameters  

        
def respond(message):
    if message in responses(): 
        bot_message = random.choice(responses()[message])
    elif len(message) == 0:
        bot_message = random.choice(responses()[" "])       #Added another statement to access the Blank key
    else:
        bot_message = random.choice(responses()["Default"])
    return bot_message
# A function that calls in the random function to select random answers to the same question



def send_message(message): 
    print(user_template.format(message)) 
    response = respond(message) 
    print(chatbot_template.format(response))


while 1: 
    my_input = input() 
    my_input = my_input.lower() 
    related_text = related(my_input) 
    send_message(related_text)
    if my_input == "exit" or my_input == "stop" or my_input == "end" or my_input == "bye": 
        print ("Code ends here")
        break