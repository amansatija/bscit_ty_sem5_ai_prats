import itertools, random

# Import necessary libraries:
# - itertools: for creating combinations/products of elements
# - random: for shuffling the deck

# Create a standard deck of 52 playing cards
# - range(1,14): represents card values (1=Ace, 11=Jack, 12=Queen, 13=King)
# - ['spade','heart','diamond','club']: represents the four suits
# - itertools.product() creates all possible combinations (13 values × 4 suits = 52 cards)
# - list() converts the iterator to a list for easier manipulation
print("Creating a standard deck of 52 playing cards...")
deck = list(itertools.product(range(1,14),['spade','heart','diamond','club']))

print(f"Deck created with {len(deck)} cards")
print(f"First card before shuffling: {deck[0][0]} of {deck[0][1]}")
def print_card(card):
    if card[0] == 1:
        card_name = "Ace"
    elif card[0] == 11:
        card_name = "Jack"
    elif card[0] == 12:
        card_name = "Queen"
    elif card[0] == 13:
        card_name = "King"
    else:
        card_name = str(card[0])
    print(f"{card_name} of {card[1]}")

def print_deck(deck):
    for card in deck:
        print_card(card)

print("\nEntire deck before shuffling: printing start")
print_deck(deck)
print("\nEntire deck before shuffling: printing end")

# Shuffle the deck randomly
print("\nShuffling the deck...")
random.shuffle(deck)
print("Deck has been shuffled")
print(f"First card after shuffling: {deck[0][0]} of {deck[0][1]}")
print("\nEntire deck after shuffling: printing start")
print_deck(deck)
print("\nEntire deck after shuffling: printing end")
# Print student information
print("\nAhmed Shaikh 323")

# Deal and display 4 cards from the top of the shuffled deck
print("\nYou got :")
for i in range(4):
    # Each card is a tuple: (value, suit)
    card_value = deck[i][0]
    card_suit = deck[i][1]
    
    # Convert numerical values to face card names for better readability
    if card_value == 1:
        card_name = "Ace"
    elif card_value == 11:
        card_name = "Jack"
    elif card_value == 12:
        card_name = "Queen"
    elif card_value == 13:
        card_name = "King"
    else:
        card_name = str(card_value)
        
    print(f"Card {i+1}: {card_name} of {card_suit}")