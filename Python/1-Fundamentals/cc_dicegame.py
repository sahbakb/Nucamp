import random

high_score = 0


def dice_game():
    global high_score
    while True:

        print("Current high score:", high_score)
        print("1) Roll Dice")
        print("2) Leave Game")
        user_choice = input("Enter your choice: ")
        print(" ")
        if user_choice == '1':
            ran_num_1 = random.randint(1, 7)
            ran_num_2 = random.randint(1, 7)
            print("You rolled a...", ran_num_1)
            print("You rolled a...", ran_num_2)
            print('Total of:', ran_num_1+ran_num_2)
            print("")

            if high_score < (ran_num_1+ran_num_2):
                high_score = ran_num_2+ran_num_1
                print("New High Score!!!\n")

        elif user_choice == '2':
            print('Goodbye!\n')

            break
        else:
            print("Wrong choice! Please enter 1 or 2\n")


dice_game()
