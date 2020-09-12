import botscripts as bs
import botdata as bd
userverified = False

while not userverified:
    bd.data['username'] = bs.login()
    if bd.data['username']:
        userverified = True

print("I am %s, your virtual buddy. You can speak to me and I will talk back to you"%bd.data["name"])
while userverified:
    message = input("%s:"% bd.data['username'])
    bs.send_message(message)
