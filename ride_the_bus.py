from card_game import *

# Possible answers
not_valid = "That's not a valid answer, drink one either way"
win = "You were right, choose somebody to drink"
lose = "You were wrong, take one sip"

# Ask for the number of players joining the game
n_players = int(input("How many players will join? "))

# Ask for each player's name
players_list = []
for p in range(n_players):
    name = input(f"What is the name of player {p + 1}? ")
    players_list.append(name)

# Create a Player instance for each name   
for p in range(n_players):
   players_list[p] = Player(players_list[p])
   
# Round 1: Red or Black?
for p in range(n_players):
    print(f"\n\n{players_list[p].name}, it is your turn now")
    prediction = input("Guess: Is the card red or black? ").lower()
    players_list[p].draw(deck)
    if prediction in ['black', 'red']:
        print("You drew \n")
        players_list[p].showHand()
        print(win if prediction == players_list[p].hand[0].color else lose)
    else:
        print(not_valid)
        
# Round 2: Higher or Lower
for p in range(n_players):
    print(f"\n\n{players_list[p].name}, it is your turn now")
    print('Your last card was ')
    players_list[p].showHand()
    pred = input("Guess: Is the next card higher or lower? ").lower()
    players_list[p].draw(deck)
    players_list[p].showHand()
    
    if pred in ['higher', 'lower']:
        if pred == 'higher':
            print(win if players_list[p].hand[1].value >  players_list[p].hand[0].value else lose)
        else:
            print(win if players_list[p].hand[1].value < players_list[p].hand[0].value else lose)
    else:
        print(not_valid)
