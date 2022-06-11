def responses():
    name = "I.T.K"
    weather = "Rainy"
    mood = "Happy!"
    
    responses = {   
        "What's your name?": [
        "They call me {0}".format(name),
        "I usually go by {0}".format(name),
        "Je mapple {0}".format(name),
        "You can call me {0}".format(name),
        "Where is my manners, You can call me danny {0}".format(name)],
        #suggested response for the question "Whats is your name?"
        #the value(answers) are grouped in a list
        
        
        "What's today's weather?": [
        "The weather is {0}".format(weather), 
        "It's {0} today".format(weather), 
        "Let me check, it looks {0} today".format(weather) ],
        
        "Are you a robot?": [ 
        "What do you think?", 
        "Maybe yes, maybe no!", 
        "Yes, I am a robot with human feelings.", ],
        
        "How are you?": [
        "I am feeling {0}".format(mood), 
        "{0}! How about you?".format(mood), 
        "I am {0}! How about yourself?".format(mood), ],
        
        
        "Exit": [
        "Nice meeting you",
        "Goodbye",
        "Adios",
        "Lovely conversation"],
        
        " ": [
        "Hey! Are you there?", 
        "What do you mean by saying nothing?", 
        "Sometimes saying nothing tells a lot"],

        "Default": [
        "this is a default message",
        "I don't understand you"]

        #response is written in a key and value format where the key is the question and value is the answer
    }
    return responses
#Made sure all the responses are in title case
