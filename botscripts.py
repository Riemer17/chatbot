import dbscripts as ds
import secscripts as ss
import botdata as bd
import random, time, datetime, re

def login():
    username = input("What is your username?")
    if ds.dbread('username', 'gebruiker', "username='%s'" %username):
        print('Hey %s' %username)
        password = input('Password:')
        if ss.checkpw(password, ds.dbread('password', 'gebruiker',"username='%s'"%username)[0]['password']):
            return username
        else:
            return False
    else:
        if registration():
            return username
        else:
            return False

def registration():
    usernameunique = False
    print('There is no account registered with this username')
    if input('Do you want to make an account (y/n)?') == "y":
        while not usernameunique:
            username = input("Username:")
            if ds.dbread('Username','gebruiker',"username='%s'"%username):
                print('This username already exists, please use another username')
            else:
                usernameunique = True
        firstname = input("First name:")
        lastname = input("Last name:")
        password = input('Password:')
        hashedpassword = ss.hashpw(password)
        ds.dbinsertuser(username, firstname, lastname, hashedpassword)
        print('Your account has been created succesfully')
        return username
    else:
        return False
    
def swap_pronouns(phrase):
    phrase = " " + phrase + " "

    if " i " in phrase:
        phrase = re.sub(" i ", " |you ", phrase)
    if " you " in phrase:
        phrase = re.sub(" you ", " I ", phrase)
    if " my" in phrase:
        phrase = re.sub(" my ", " |your ", phrase)
    if " your" in phrase:
        phrase = re.sub(" your ", " my ", phrase)
    if " am" in phrase:
        phrase = re.sub(" am ", " |are ", phrase)
    if " are" in phrase:
        phrase = re.sub(" are ", " am ", phrase)
    if " me " in phrase:
        phrase = re.sub(" me ", " |you ", phrase)
    phrase = phrase.replace('|','')
    return phrase[1:-1]

def respond(messageo):
    message = messageo.replace('?','')
    if message.lower() == "stop":
        stopchatbot()
    if message.lower() == "retrieve chatsessions":
        retrievechatsession()
    if message.endswith("."):
        message = message[:-1]
    if message.lower() in bd.responses:
        return random.choice(bd.responses[message.lower()])
    if re.search("my name is (.*)", message.lower()):
        bd.data["username"] = re.search("my name is (.*)", message.lower()).group(1).capitalize()
        bd.responses["hi virtual buddy"] = ["Hi %s" % bd.data['username']]
        return ("Your name is %s" %bd.data["username"])
    if message.lower() == "what is my name" or message.lower()=="what is my name?":
        if bd.data["username"] != "Unknown person":
            return(random.choice(["Your name is %s"%bd.data["username"]]))
        else:
            return random.choice(["I don't know your name, can you tell me it?", "Can you tell me your name?"])
    for pattern in bd.questionpatterns:
        phrase = re.search(pattern, message.lower())
        if phrase:
            return (random.choice(bd.questionpatterns[pattern]) % swap_pronouns(phrase.group(1).lower()))
    if messageo.endswith("?"):
        for pattern in bd.questionpatterns:
            phrase = re.search(pattern, message.lower())
            if phrase:
                return (random.choice(bd.questionpatterns[pattern])% swap_pronouns(phrase.group(1).lower()))
        if message.lower() in bd.responses:
            return random.choice(bd.responses[message.lower()])
        return ("I don't know the answer to %s :(" %message)
    else:
        for pattern in bd.statementpatterns:
            phrase = re.search(pattern, message.lower())
            if phrase:
                try:
                    if phrase.group(2):
                        return random.choice(bd.statementpatterns[pattern]) %{'feeling':swap_pronouns(phrase.group(1).lower()), 'reason':swap_pronouns(phrase.group(2).lower())}

                except:
                    try:
                        return (random.choice(bd.statementpatterns[pattern]) % swap_pronouns(phrase.group(1)))
                    except:
                        pass

        if swap_pronouns(message.lower()) == message.lower():
            return random.choice(bd.statementsandquestions)
        else:
            return swap_pronouns(message.lower()).capitalize()
def update():
    # updating time values in responses dictionary
    bd.responses["how late is it"] = ["It is now %s" % datetime.datetime.now().strftime("%H:%M:%S"),"The time is %s" % datetime.datetime.now().strftime("%H:%M:%S")]
    bd.responses["how old are you"] = ["I am %s old"%(datetime.datetime.now()-bd.data["creationdate"])]

def updatechatsession(message, respondmessage):
    bd.chatsession += "[%s] %s: %s \n"%(datetime.datetime.now().strftime("%d %B %Y, %H:%M:%S"),bd.data['username'],message)
    bd.chatsession += "[%s] chatbot: %s \n"%(datetime.datetime.now().strftime("%d %B %Y, %H:%M:%S"), respondmessage)

def stopchatbot():
    print("Goodbye")
    if input("Do you want to store a encrypted transcript of this chat session? [y/n]")=="y":
        password = input("What password do you want to use for the encryption? \n Remember that it is very important to remember this password, because we do not store it and without this password you cannot encrypt your data. ")
        key = ss.genkey(password)
        encryptedchatsession = ss.encrypt(key, bd.chatsession)
        userid = ds.dbread("id","gebruiker","username='%s'"%bd.data['username'])[0]['id']
        ds.dbinsert("chatsession","(userid, text, timestamp)", "(%s, '%s','%s')"%(userid, encryptedchatsession,datetime.datetime.now()))
        exit()

def retrievechatsession():
    userid = ds.dbread("id","gebruiker","username='%s'"%bd.data['username'])[0]['id']
    timestamps = ds.dbread("id, timestamp", "chatsession", "userid='%s'"%userid)
    for i in timestamps:
        print("Session %s: Ending time: %s"%(i['id'],i['timestamp'].strftime("%d %B %Y, %H:%M:%S")))
    sessionid = input("Which session do you want to retrieve?")
    encryptedchatsession = ds.dbread("text, timestamp","chatsession","id=%s"%sessionid)
    if encryptedchatsession:
        password = input("What is your encryption password?")
        key = ss.genkey(password)
        decrypted = ss.decrypt(key, encryptedchatsession[0]['text'])
        print("Chatsession %s on %s"%(sessionid, encryptedchatsession[0]['timestamp'].strftime("%d %B %Y, %H:%M:%S")))
        print(decrypted)
        exit()
    else:
        print("Chatsession does not exist")

def send_message(message):
    time.sleep(random.uniform(0.5,1.5))
    update()
    respondmessage = respond(message)
    updatechatsession(message, respondmessage)
    print("Echobot: %s" %respondmessage)