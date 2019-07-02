import random, time, datetime, re

data = {"name" : "Virtual buddy", "creationdate" : datetime.datetime(2019,5,6,8,15), "username":"Unknown person"}
responses = {"hey" :["Hey","Hi","Hello"],"hi" :["Hey","Hi","Hello"],"hello" : ["Hey","Hi","Hello"],"what is your name":["My name is %s"%data["name"],"People call me %s"%data["name"]],
             "how late is it":["It is now %s"%datetime.datetime.now().strftime("%H:%M:%S"),"The time is %s"%datetime.datetime.now().strftime("%H:%M:%S")],
             "how old are you":["I am %s old"%(datetime.datetime.now()-data["creationdate"])],"how are you" : ["I'm fine","I am fine","I am feeling well", "I am not feeling so well"],
             "i am fine":["That's nice to hear","Why are you feeling fine?","Can you describe that?","Keep feeling fine!"],"hi virtual buddy":["Hi %s"%data['username']]
            }

statementsandquestions = ["Tell me more!", "That sounds interesting", "Wow!","How do you feel?",
                          "What is your name"]

statementpatterns = {"my name is (.*)" : ["your name is %s"], "i feel (.*) because (.*)":["You feel %(feeling)s because %(reason)s", "Why is it that %(reason)s makes you %(feeling)s?"],
                     "i feel (.*)":["Why do you feel %s?","How long have you felt %s?","You feel %s, why?, Why do you feel %s"],
                    "i am feeling (.*)":["Why do you feel %s?","How long have you felt %s?","You feel %s, why?"]}

questionpatterns = {"why do you feel (.*)\?":["I feel %s because it's raining", "I feel %s because it's sunny", "I feel %s because it's cloudy", "I feel %s because I am listening"],
                    "why do you feel (happy)\?":["I feel %s because I am programming","I feel %s because I like what I am doing", "I feel %s because the weather is good",
                                                   "I feel %s because I am helping someone"],
                    "why do you feel (bad)\?":["I feel %s because what I am doing is boring","I feel %s because life is bad", "I feel %s because I do not like what I am doing",
                                               "I feel %s because the water is bad",],
                    "do you remember (.*)\?": ["How could I forget %s", "Of course I remember %s"]}

def swap_pronouns(phrase):
    phrase = " " + phrase + " "

    if " i " in phrase or "you ":
        phrase = re.sub(" i ", " you ", phrase)
    if " my" in phrase:
        phrase = re.sub(" my ", " your ", phrase)
    if " am" in phrase:
        phrase = re.sub(" am ", " are ", phrase)
    if " me " in phrase:
        phrase = re.sub(" me ", " you ", phrase)
    return phrase

def respond(message):
    if message.endswith("."):
        message = message[:-1]
    if message.lower() in responses:
        return random.choice(responses[message.lower()])
    if re.search("my name is (.*)", message.lower()):
        data["username"] = re.search("my name is (.*)", message.lower()).group(1).capitalize()
        responses["hi virtual buddy"] = ["Hi %s" % data['username']]
        return ("Your name is %s" %data["username"])
    if message.lower() == "what is my name" or message.lower()=="what is my name?":
        if data["username"] != "Unknown person":
            return(random.choice(["Your name is %s"%data["username"]]))
        else:
            return random.choice(["I don't know your name, can you tell me it?", "Can you tell me your name?"])
    if message.endswith("?"):
        for pattern in questionpatterns:
            phrase = re.search(pattern, message.lower())
            if phrase:
                return (random.choice(questionpatterns[pattern])% swap_pronouns(phrase.group(1).lower()))
        if message[:-1].lower() in responses:
            return random.choice(responses[message[:-1].lower()])
        return ("I don't know the answer to %s :(" %message)
    else:
        for pattern in statementpatterns:
            phrase = re.search(pattern, message.lower())
            if phrase:
                try:
                    if phrase.group(2):
                        return random.choice(statementpatterns[pattern]) %{'feeling':swap_pronouns(phrase.group(1).lower()), 'reason':swap_pronouns(phrase.group(2).lower())}

                except:
                    try:
                        return (random.choice(statementpatterns[pattern]) % swap_pronouns(phrase.group(1)))
                    except:
                        pass

        if swap_pronouns(message.lower()) == message.lower():
            return random.choice(statementsandquestions)
        else:
            return swap_pronouns(message.lower()).capitalize()
def update():
    # updating time values in responses dictionary
    responses["how late is it"] = ["It is now %s" % datetime.datetime.now().strftime("%H:%M:%S"),"The time is %s" % datetime.datetime.now().strftime("%H:%M:%S")]
    responses["how old are you"] = ["I am %s old"%(datetime.datetime.now()-data["creationdate"])]

def send_message(message):
    print("You: %s" %message)
    time.sleep(random.uniform(0.5,1.5))
    update()
    respondmessage = respond(message)
    print("Echobot: %s" %respondmessage)

print("I am %s, your virtual buddy. You can speak to me and I will talk back to you"%data["name"])

while True:
    message = input("")
    send_message(message)