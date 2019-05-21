# Create your own Echobot
import random, time, datetime, re

data = {"name" : "Echobot 1", "creationdate" : datetime.datetime(2019,5,6,8,15)}
responses = {"hey" :["Hey","Hi","Hello"],"hi" :["Hey","Hi","Hello"],"hello" : ["Hey","Hi","Hello"],"what is your name?":["My name is %s"%data["name"],"People call me %s"%data["name"]],
             "how late is it?":["It is now %s"%datetime.datetime.now().strftime("%H:%M:%S"),"The time is %s"%datetime.datetime.now().strftime("%H:%M:%S")],
             "how old are you?":["I am %s old"%(datetime.datetime.now()-data["creationdate"]),"Do you want to know that?"],"how are you?" : ["I'm fine","I am fine","I am feeling well", "I am not feeling so well"],
             "i am fine":["That's nice to hear","Why are you feeling fine?","Can you describe that?","Keep feeling fine!"]}

statementsandquestions = ["Tell me more!", "That sounds interesting", "Wow!", "How long have you felt this way?","How do you feel?",
                          "What is your name"]


patterns = {"do you remember (.*)" : "How could I forget %s","my name is (.*)" : "your name is %s", "i feel (.*)":"Why do you feel %s?"}
def swap_pronouns(phrase):
    if "i" in phrase:
        phrase = re.sub("i ","you ", phrase)
    if " my" in phrase:
        phrase = re.sub("my ","your ", phrase)
    if " am" in phrase:
        phrase = re.sub("am ","are ", phrase)
    if " me " in phrase:
        phrase = re.sub("me ","you ", phrase)

    return phrase

def respond(message):

    if message.lower() in responses:
        return random.choice(responses[message.lower()])

    for pattern in patterns:
        phrase = re.search(pattern, message.lower())
        if phrase:
            return (patterns[pattern] % swap_pronouns(phrase.group(1)))

    if message.endswith("?"):
        return ("I don't know the answer to %s :(" %message)
    else:
        if swap_pronouns(message.lower()) == message.lower():
            return random.choice(statementsandquestions)
        else:
            return swap_pronouns(message.lower()).capitalize()

def send_message(message):
    print("You: %s" %message)
    time.sleep(random.uniform(0.5,1.5))
    print("Echobot: %s" %respond(message))

print("I am %s, your virtual buddy. You can speak to me and I will talk back to you"%data["name"])
while True:
    message = input("")
    send_message(message)

