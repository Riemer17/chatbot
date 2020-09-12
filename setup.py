# Zorg ervoor dat er een database genaamd chatbot is en een user in xampp met de volgende credentials:
# username: chatb
# password: Cartesius2

import dbscripts as ds
ds.dbcreatetableuser()
ds.dbcreatetablechatsession()
print("Databases aangemaakt!")