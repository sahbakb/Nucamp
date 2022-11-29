import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}


dealer_total = 0
player_total = 0


def randomCardGenerator():
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append((rank,suit))
    deck = deck + deck +deck

    card = random.choice(deck)
    card = (card[0],card[1], values[card[0]])
    return card

def showHands(dealer,player):
    global dealer_total
    global player_total
    print()
    print("Dealer Hand:")
    for i in dealer:
        print(i[0] + " of "+ i[1])
        dealer_total = dealer_total + i[2]
    print("Total:",dealer_total)     
    print()
    print("Your Hand:")
    for i in player:
        print(i[0]+ " of "+ i[1])    
        player_total = player_total + i[2]
    print("Total:",player_total)   


