# Possible answers
not_valid = "That's not a valid answer, drink one either way"
win = "You were right, choose somebody to drink"
lose = "You were wrong, take one sip"

# Instructions
round1 = """In round 1 you guess if the color of the card is black or
red. Simple, right? If you make a typo or answer something else
you drink!"""

round2 = """In round 2 you guess if the number of the card is higher
or lower than the card you drew in the last hand"""

round3 = """In round 3 you guess if the number of the next card is inside,
outside, or the two cards you drew. For example, if you have a
2 and a 7, inside would be any number between 3 and 6. 

If you draw one of the numbers you already have...You drink."""

round4 = """In round 3 you guess if you already have a card with
the same suit as the card that you will draw next. For example,
if you have 3 spades and you answer "I don't have it", you win
unless the suit of the card drawn is also spades."""

# Ask for each player's name
def ask_names(n_players):
    
    __players_list__ = []
    
    for p in range(n_players):
        # p + 1: Otherwise it would say player 0 instead of player 1
        name = input(f"What is the name of player {p + 1}? ")
        __players_list__.append(name)

    return __players_list__

# Check if the card if the card is inside, or outside
def inside():
    players_list[p].hand[2].value < players_list[p].hand[1].value \
    and players_list[p].hand[2].value < players_list[p].hand[0].value
    
def outside():
    players_list[p].hand[2].value > players_list[p].hand[1].value \
    and players_list[p].hand[2].value > players_list[p].hand[0].value

# Check if you have the suit already
def have_it_already():
    players_list[p].hand[3].suit in [
        players_list[p].hand[2].suit
        , players_list[p].hand[1].suit
        , players_list[p].hand[0].suit
    ]