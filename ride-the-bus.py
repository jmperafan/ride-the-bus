from card_game import *
from setup import *

# Ask for the number of players joining the game
n_players = int(input("How many players will join? "))

# Run the function and save it as players_list
players_list = ask_names(n_players)

# Create a player instances
for p in range(n_players):
    players_list[p] = Player(players_list[p])
   
# Round 1: Red or Black?
print(round1)

for p in range(n_players):
    print(f"\n\n{players_list[p].name}, it is your turn now")
    prediction = input("Guess: Is the card red or black? ").lower()
    
    players_list[p].draw(deck)
    print("You drew \n")
    players_list[p].showHand()
        
    # Checks if the card is either black or red
    if prediction in ['black', 'red']:
        print(win if prediction == players_list[p].hand[0].color else lose)
        # If the answer is neither black or red... You have to drink
    else:
        print(not_valid)

# Round 2: Higher or Lower
print(round2)

for p in range(n_players):
    print(f"\n\n{players_list[p].name}, it is your turn now")
    
    print('Your last card was ')
    players_list[p].showLastCard()

    prediction = input("Guess: Is the next card higher or lower? ").lower()
    
    players_list[p].draw(deck)
    print("You drew \n")
    players_list[p].showHand()

    if prediction in ['higher', 'lower']:
        if prediction == 'higher':
            print(win if players_list[p].hand[1].value >  \
                players_list[p].hand[0].value else lose)
        else:
            print(win if players_list[p].hand[1].value < \
                players_list[p].hand[0].value else lose)
    else:
        print(not_valid)

# Round 3: Inside or outside?
print(round3)

for p in range(n_players):
    print(f"\n\n{players_list[p].name}, it is your turn now")
    
    print('Your cards are ')
    players_list[p].showHand()

    prediction = input("Guess: Is the next card inside or outside? ").lower()
    
    players_list[p].draw(deck)
    print("You drew \n")
    players_list[p].showHand()

    if prediction in ['inside', 'outside']:
        if inside == True and prediction == "inside"\
        or outside == True and prediction == "outside":
            print(win)
        else:
            print(lose)
    else:
        print(not_valid)

# Round 4: Do you already have the suit
print(round4)

for p in range(n_players):
    print(f"\n\n{players_list[p].name}, it is your turn now")
    
    print('Your cards are ')
    players_list[p].showHand()

    prediction = input("Guess: Do you have suit already (yes or no) ").lower()
    
    players_list[p].draw(deck)
    print("You drew \n")
    players_list[p].showHand()

    if prediction in ['yes', 'no']:
        if have_it_already == True and prediction == "yes"\
        or have_it_already == False and prediction == "no":
            print(win)
        else:
            print(lose)
    else:
        print(not_valid)