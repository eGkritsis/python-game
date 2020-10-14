# ----------------- AGWNIA ----------------------

from Functions import *
 

player_num = input("Write number of player's 2-7: ")
while int(player_num) < 1 or int(player_num) > 7:
    player_num = input("Write number of player's 2-7: ")

player_names = []

for i in range(int(player_num)):
    player_names.append(input("Write player's name: "))
player_names.sort()    

# Creating a shuffled deck
deck = create_deck()
closed_deck = deck

# At the start, all the players have 0 points
points = []
create_points_list(player_num, points)

hands = []
create_hands(player_num, deck, hands)

first_card = []
create_first_card(deck, first_card)


# ---------------------- GAME STARTS ---------------------------

game_flag = True
while game_flag:

    z = 0
    flag = False
    while flag == False:
        
        tempfirst = first_card[0]
        print('The first card is:', tempfirst)
        show_hand(player_names, hands, z)
        choice = input('play or fold?: ')
        if len(deck) == 0:
            deck, first_card = new_deck(first_card, deck)
        if choice == 'play': 
            position = input('Write the position of the cart you want to use starting from 1: ')
            while len(hands[z]) < int(position):
                position = input('Write the position of the cart you want to use starting from 1: ')
                
            chosen_card = choose_card(hands, position, z)
            # A player can't finish the round with an '8'
            if chosen_card[0] == '8' and len(hands[z]) == 1:
                choice = input('You cant end the round with 8 choose again play or fold: ')
            elif chosen_card[0] == tempfirst[0] or chosen_card[1] == tempfirst[1] or chosen_card[0] == 'A':
                first_card.insert(0,hands[z].pop(int(position)-1))
                show_hand(player_names, hands, z)
                z+=1
                # When someone plays a '7', the next player must draw 2 cards from the closed pile
                if chosen_card[0] == '7':
                    hands[z].append(deck.pop(0))
                    if len(player_names) == z:
                        temp = 0
                    else:
                        temp = z
                    print(player_names[temp] + "'s", "cards will increase by 2")
                    if len(deck) == 0:
                        deck, first_card = new_deck(first_card, deck)
                    hands[z].append(deck.pop(0))
                # When someone plays a '9', the next player loses his turn
                elif chosen_card[0] == '9':
                    temp = z
                    if temp == len(player_names):
                        temp = 0
                    if z == len(player_names):
                        z = 1
                    else:
                        z += 1
                    print(player_names[temp], 'will lose his turn')
                # When someone plays an 'A' he gets to choose the Suite of the next cards
                elif chosen_card[0] == 'A':
                    suite = input('Give the suite you want to use: ')
                    while suite != 'Diamonds' and suite != 'Clubs' and suite != 'Spades' and suite != 'Hearts':
                        suite = input('Give the suite you want to use (Diamonds, Clubs, Spades, Hearts): ')    
                    first_card[0].pop(1)
                    first_card[0].insert(1,suite)
                    print("first's card suite will change to", suite)
                # When someone plays an '8' he gets to play again 
                elif chosen_card[0] == '8':
                    temp = z - 1
                    if z == 0:
                        temp = 0
                    z = temp
                    print(player_names[z], "will play again")
            else:
                choice = input('The card you choose does not fit choose again play or fold: ')
            # If someone folds, he must pick a card from closed pile
        elif choice == 'fold':
            hands[z].append(deck.pop(0))
            z+=1
        if z > int(player_num)-1:
            z = 0
        if len(deck) == 0:
            deck, first_card = new_deck(first_card, deck)
        if len(hands[z]) == 0:
            temp_points = [0,0,0]
            hands[z].append(temp_points)
            print('player',player_names[z],'won the round!!!')
            flag = True
            break
    # Calculating the points at the end of each round  
    count_points(hands, points)   
    
    game_flag, player_position = check_points(points)
    # If game_flag == False the game ends and the winner is announced
    if game_flag == False:
        print('The Winner of the game is',player_names[player_position],'with',points[player_position],'points')
    # else if flag == True the deck is being shuffled again and another round is going to be played
    if flag == True:
        deck = create_deck()
        closed_deck = deck
        hands = []
        create_hands(player_num, deck, hands)
        first_card = []
        create_first_card(deck, first_card)
    
    
# ---------- END ------------------