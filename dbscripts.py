import pymysql

#connect to database and make cursor
# db = pymysql.connect("192.168.64.2","chatb","Cartesius2","chatbot" )
db = pymysql.connect("localhost","chatb","Cartesius2","chatbot" )
cursor = db.cursor(pymysql.cursors.DictCursor)

def dbcreatetableuser():
    try:
        cursor.execute("""CREATE TABLE gebruiker(
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            username VARCHAR(256),
                            first_name VARCHAR(256),
                            last_name VARCHAR (256),
                            password VARCHAR (60))""")
        db.commit()
    except:
        db.rollback()

def dbcreatetablechatsession():
    try:
        cursor.execute("""CREATE TABLE chatsession(
        id INT AUTO_INCREMENT PRIMARY KEY,
        userid INT,
        text LONGTEXT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (userid) REFERENCES gebruiker(id))
        """)
        db.commit()
    except:
        db.rollback()

def dbread(rows, table, where=None):
    #Function that reads the database on the specified rows and tables, the where parameter is not required
    #if it is not given all the results form the table are shown.
    try:
        if where:
            execute = cursor.execute("SELECT %s FROM %s WHERE %s"%(rows, table, where))
        else:
            execute = cursor.execute("SELECT %s FROM %s"%(rows, table))

        if execute>0:
            #Chechk if any result is given
            result = cursor.fetchall()
            return result
        else:
            #If no result is given return none
            return None
    except:
        #rollback if any error ocurred
        db.rollback()
        return "An error occured"

def dbinsert(table, rows, values):
    cursor.execute("""INSERT INTO %s %s VALUES %s""" % (table, rows, values))
    db.commit()
    # try:
    #     cursor.execute("""INSERT INTO %s %s VALUES %s"""%(table, rows, values))
    #     db.commit()
    # except:
    #     db.rollback()
    #     return "An error occured"
    # db.commit()

def dbdelete(table, where):
    try:
        cursor.execute("DELETE FROM %s WHERE %s)"%(table,where))
    except:
        db.rollback()
        return  "An error occured"
    db.commit()

def dbinsertuser(username, firstname, lastname, hashedpassword):
    try:
        cursor.execute("""INSERT INTO gebruiker (username, first_name, last_name, password) VALUES('%s', '%s', '%s', '%s')"""%(username, firstname, lastname, hashedpassword))
        db.commit()
    except:
        db.rollback()