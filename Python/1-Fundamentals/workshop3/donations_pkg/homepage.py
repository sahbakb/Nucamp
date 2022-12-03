def show_homepage():

    print("         ===DonateMe Homepage===     ")
    print('----------------------------------------------')
    print('| 1.    Login      | 2.    Register          |')
    print('----------------------------------------------')
    print('| 3.    Donate     | 4.    Show Donations    |')
    print('----------------------------------------------')
    print('|                5. Exit                     |')
    print('----------------------------------------------')


def donate(username):
    donation_amt = float(input("Enter amount to doante: "))

    print("Thank you! ")
    return donation_amt


def show_donations(donations, username):
    total = 0
    print("\n----All Donations---\n")
    if len(donations) == 0:
        print("Currently, there are no donations.")
    else:
        for i in donations:
            print(username + " donated $"+str(i))
            total = total + i
    print("Total: $" + str(total))
