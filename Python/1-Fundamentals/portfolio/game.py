from cards import randomCardGenerator, showHands

dealer_hand = []
player_hand = []

exit = False
busted = False
lost = False

while exit == False:

    dealer_hand.append(randomCardGenerator())
    player_hand.append(randomCardGenerator())
    player_hand.append(randomCardGenerator())

    showHands(dealer_hand, player_hand)

    while lost == False:
        player_choice = input("\nHit or Stand(H/S): ")
        if player_choice.lower() == "h" or player_choice.lower() == 'hit':
            player_hand.append(randomCardGenerator())
            showHands(dealer_hand,player_hand)
        else:
            lost =True    
            exit = True
