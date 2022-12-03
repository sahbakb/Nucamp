def login(database, username, password):
    if username in database:
        if database[username] == password:
            print("Welcome!!!!")
            return username
        else:
            print("Invalid Password")
            return ""
    else:
        print("Username does not exist. Please register")
        return ""


def register(database, username):
    if username in database:
        print("Username already registered")
        return ""
    else:
        print(username + " has been registered!")
        return username
