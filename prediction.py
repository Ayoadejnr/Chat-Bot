from QA import responses

def related(x_text):
    name = "I.T.K"
    weather = "Rainy"
    mood = "Happy!"
    if "name" in x_text:
        y_text = "What's your name?"
    elif "weather" in x_text:
        y_text = "What's today's weather?"
    elif "robot" in x_text:
        y_text = "Are you a robot?"             #Converted all to title case
    elif "how are" in x_text:
        y_text = "How are you?"
    elif "stop" in x_text:
        y_text = "Exit"
    elif "end" in x_text:
        y_text = "Exit"
    elif "bye" in x_text:
        y_text = "Exit"
    elif "exit" in x_text:
        y_text = "Exit"
    elif len(x_text) == 0:              #Added another statement to access the blank key
        y_text = " "
    else:
        y_text = "Default"
    return y_text
# A function helps to match words that can be related to the question
