import random

diamonds = 'AD 2D 3D 4D 5D 6D 7D 8D 9D 10D JD QD KD'.split(' ')
hand = []

while diamonds:
    user_input = input("Press enter to pick a card or press Q to exit: ")
    if user_input.upper() == 'Q':
        break
    else:

        choice = random.choice(diamonds)
        diamonds.remove(choice)
        hand.append(choice)
        print("Remaining Cards: ", diamonds)
        print()
        print("Your Hand: ", hand)
print("No more cards to pick!")
