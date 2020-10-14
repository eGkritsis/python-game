def create_deck():
    # Creating a shuffled deck
    from random import shuffle
    temp = []
    deck = []
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    points = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    suite = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    for i in range(4):
        for j in range(13):
            temp.append(values[j])
            temp.append(suite[i])
            temp.append(points[j])
            deck.append(temp)
            temp = []
    shuffle(deck)
    return deck

def create_hands(player_num, deck, hands):
    # Dealing 7 cards to each player
    templist = []
    for _ in range(int(player_num)):
        for _ in range(7):
            temp = deck.pop(0)
            templist.append(temp)
        hands.append(templist)
        templist = []
    return hands, deck
            
def show_hand(player_name, hands, z):
    # Prints the hand of the player
    # z -- index
    print(player_name[z] + "'s", 'deck')
    x = 1
    for i in hands[z]:
        print("(",x,")",i)
        x+=1
    print('...')
                   
def create_first_card(deck, first_card):
    # Creating the first open card
    first_card.append(deck.pop(0))
    return first_card
    
def choose_card(hands,position,z):
    # position -- position of wanted card in player's hand
    return hands[z][int(position)-1]
    
def new_deck(first_card, deck):
    # Creating a new shuffled deck from the opened deck when there are no cards left in the closed pile
    from random import shuffle
    deck = first_card[1:]
    temp_first_card = []
    temp_first_card.append(first_card[0])
    shuffle(deck)
    return deck, temp_first_card
    

def create_points_list(player_num, points):
    # Returning a list of all the player's points
    # All players start with 0 points
    for _ in range(int(player_num)):
        points.append(0)
    return points

def count_points(hands, points):
    # Adding the points of the cards left in hand at the end of every round to each
    for i in range(len(hands)):
        for j in range(len(hands[i])):
            points[i] = points[i] + hands[i][j][2]
    
def check_points(points):
    # Checks if a player has surpassed 50 points
    # If a player has more than 50 points it returns False, the game ends and this player is the winner
    # If more than one players have the same amount of points it returns True and the game continues
    min = 999
    game_flag = True
    for i in range(len(points)):
        if points[i] > 49:
                for j in range(len(points)):
                    if points[j] < min:
                        min = points[j]
                        min_player_pos = j
                        game_flag = False
                for z in range(len(points)):
                    if points[z] == min and z != j:
                        game_flag = True
    return game_flag, min_player_pos
                        
                    
                
            
                
    
        
                   
    
