from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register

database = {'admin': '123'}
donations = []
authorized_user = ''

while True:

    show_homepage()

    if authorized_user == '':
        print('You must be logged in to donate.')
    else:
        print("Logged in as: "+authorized_user)

    option = input("\nChoose an option: ")

    if option == '1':
        username = input("Please enter username: ")
        password = input("Please enter your password: ")
        authorized_user = login(database, username, password)

    elif option == '2':
        username = input("Please enter username: ")
        password = input("Please enter your password: ")
        authorized_user = register(database, username)
        if authorized_user != "":
            database[authorized_user] = password

    elif option == '3':
        if authorized_user == '':
            print("You are not logged in!")
        else:
            donation_amt = donate(authorized_user)
            print(authorized_user + " donated $" + str(donation_amt))
            donations.append(donation_amt)

    elif option == '4':
        if authorized_user == '':
            print("You are not logged in!")
        else:
            show_donations(donations, authorized_user)
    elif option == '5':
        print('\n Leaving donateMe....')
        break
