import datetime

chatsession = """"""
data = {"name" : "Virtual buddy", "creationdate" : datetime.datetime(2019,5,6,8,15), "username":"Unknown person"}
responses = {"hey" :["Hey","Hi","Hello"],"hi" :["Hey","Hi","Hello"],"hello" : ["Hey","Hi","Hello"],"what is your name":["My name is %s"%data["name"],"People call me %s"%data["name"]],
             "how late is it":["It is now %s"%datetime.datetime.now().strftime("%H:%M:%S"),"The time is %s"%datetime.datetime.now().strftime("%H:%M:%S")],
             "how old are you":["I am %s old"%(datetime.datetime.now()-data["creationdate"])],"how are you" : ["I'm fine","I am fine","I am feeling well", "I am not feeling so well"],
             "i am fine":["That's nice to hear","Why are you feeling fine?","Can you describe that?","Keep feeling fine!"],"hi virtual buddy":["Hi %s"%data['username']]
            }

statementsandquestions = ["Tell me more!", "That sounds interesting", "Wow!","How do you feel?",
                          "What is your name"]

statementpatterns = {"my name is (.*)" : ["your name is %s"], "i feel (.*) because (.*)":["You feel %(feeling)s because %(reason)s", "Why is it that %(reason)s makes you feel %(feeling)s?"],
                     "i feel (.*)":["Why do you feel %s?","How long have you felt %s?","You feel %s, why?, Why do you feel %s"],
                    "i am feeling (.*)":["Why do you feel %s?","How long have you felt %s?","You feel %s, why?"]}

questionpatterns = {"why do you feel (.*)":["I feel %s because it's raining", "I feel %s because it's sunny", "I feel %s because it's cloudy", "I feel %s because I am listening"],
                    "why do you feel (happy)":["I feel %s because I am programming","I feel %s because I like what I am doing", "I feel %s because the weather is good",
                                                   "I feel %s because I am helping someone"],
                    "why do you feel (bad)":["I feel %s because what I am doing is boring","I feel %s because life is bad", "I feel %s because I do not like what I am doing",
                                               "I feel %s because the water is bad",],
                    "why are you feeling (well)":["I feel %s because I am programming", "I feel %s because the sun is shining", "I feel %s because I do not feel bad", "I feel %s because life is good"],
                    "why are you feeling (.*)":["I feel %s because it's raining", "I feel %s because it's sunny", "I feel %s because it's cloudy", "I feel %s because I am listening"],
                    "do you remember (.*)": ["How could I forget %s", "Of course I remember %s"]}
