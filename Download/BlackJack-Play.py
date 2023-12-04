your_hand = []
your_hand_com = 0
dealers_hand = []
dealers_hand_com = 0
def get_yours_hand():
    hand = int(input("Your first Card: "))
    your_hand.append(hand)
    hand = int(input("Your Second Card: "))
    your_hand.append(hand)
    return your_hand
def get_dealers_hand():
    hand = int(input("Dealers first Card: "))
    dealers_hand.append(hand)
    return dealers_hand
def compare_cards():
    dealers_hand = get_dealers_hand()
    your_hand = get_yours_hand()
    if (your_hand[0]) == (your_hand[1]):
        if (your_hand[0] in [1, 11]):
            print("Split")
        elif (your_hand[0] == 10):
            print("Stand")
        elif (your_hand[0] == 9) and (dealers_hand[0] in [2, 3, 4, 5, 6, 8, 9]):
            print("Split")
        elif (your_hand[0] == 9) and (dealers_hand[0] in [7, 10, 11, 1]):
            print("Stand")
        elif (your_hand[0] == 8):
            print("Split")
        elif (your_hand[0] == 7) and (dealers_hand[0] in [2, 3, 4, 5, 6, 7]):
            print("Split")
        elif (your_hand[0] == 7) and (dealers_hand[0] in [8, 9, 10, 1, 11]):
            print("Split")
        elif (your_hand[0] == 6) and (dealers_hand[0] in [2, 3, 4, 5, 6]):
            print("Split")
        elif (your_hand[0] == 6) and (dealers_hand[0] in [7, 8, 9, 10, 11, 1]):
            if (dealers_hand[0] in [2, 3, 7, 8, 9, 10, 11, 1]):
                print("Hit")
            else:
                print("Stand")
        

compare_cards()