# Create your own Echobot
import random, time, datetime, sqlite3


creationdate = datetime.datetime(2019,5,6,8,15)

name = "Echobot 1"
responses = {"hey":["Hey","Hi","Hello"],"hi":["Hey","Hi","Hello"],"what is your name?":["My name is %s"%name,"People call me %s"%name],
             "how late is it?":["It is now %s"%datetime.datetime.now().strftime("%H:%M:%S"),"The time is %s"%datetime.datetime.now().strftime("%H:%M:%S")],
             "how old are you?":["I am %s old"%(datetime.datetime.now()-creationdate),"Do you want to know that?"]}
def respond(message):
    message = message.lower()
    if message in responses:
        return random.choice(responses[message])
    else:
        return("I can hear you! you said: %s"%message)

def send_message(message):
    print("You: %s" %message)
    waitingtime = random.uniform(0.5,1.5)
    print(waitingtime)
    time.sleep(waitingtime)
    print("Echobot: %s" %respond(message))

print("I am %s, your virtual buddy. You can speak to me and I will talk back to you"%name)
while True:
    message = input("")
    send_message(message)