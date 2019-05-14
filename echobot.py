# Create your own Echobot
import random, time, datetime, re

data = {"name" : "Echobot 1", "creationdate" : datetime.datetime(2019,5,6,8,15)}
responses = {"hey" :["Hey","Hi","Hello"],"hi" :["Hey","Hi","Hello"],"hello" : ["Hey","Hi","Hello"],"what is your name?":["My name is %s"%data["name"],"People call me %s"%data["name"]],
             "how late is it?":["It is now %s"%datetime.datetime.now().strftime("%H:%M:%S"),"The time is %s"%datetime.datetime.now().strftime("%H:%M:%S")],
             "how old are you?":["I am %s old"%(datetime.datetime.now()-data["creationdate"]),"Do you want to know that?"],"how are you?" : ["I'm fine","I am fine","I am feeling well", "I am not feeling so well"]}

statements = ["Tell me more!", "That sounds interesting", "Wow!", "How long have you felt this way?"]
questions = ["How do you feel?", "What is your name"]
def respond(message):
    factor = random.randint(0,2)
    print(factor)
    if message.lower() in responses:
        return random.choice(responses[message.lower()])
    elif message.endswith("?"):
        return ("I don't know the answer to %s :(" %message)
    elif factor == 0:
        return random.choice(statements)
    elif factor == 1:
        return random.choice(questions)
    elif factor == 2:
        return("I can hear you! you said: %s"%message)

def send_message(message):
    print("You: %s" %message)
    time.sleep(random.uniform(0.5,1.5))
    print("Echobot: %s" %respond(message))

print("I am %s, your virtual buddy. You can speak to me and I will talk back to you"%data["name"])
while True:
    message = input("")
    send_message(message)

