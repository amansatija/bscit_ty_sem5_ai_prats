# Python3 program for shuffling desk of cards
# Function which shuffle and print the array 

import random
def shuffle(card,n) :
    
    # Initialize seed randomly
    for i in range(n):
        
        # Random for remaining positions.
        r = i + (random.randint(0,55) % (52 -i))
        tmp=card[i]
        card[i]=card[r]
        card[r]=tmp
#Driver code
if __name__=='__main__':
    a=[0, 1, 2, 3, 4, 5, 6, 7, 8,
       9, 10, 11, 12, 13, 14, 15,
       16, 17, 18, 19, 20, 21, 22, 
       23, 24, 25, 26, 27, 28, 29,
       30, 31, 32, 33, 34, 35, 36,
       37, 38, 39, 40, 41, 42, 43, 
       44, 45, 46, 47, 48, 49, 50,
       51]
    shuffle(a,52)
    print(a)
       
#this code is contributed by sahilshelangia

# The purpose of this line is to implement the Fisher-Yates shuffle algorithm, which works by:

# Starting from the first card (i=0)
# Selecting a random card from the entire deck
# Swapping the current card with the randomly selected one
# Moving to the next card and repeating, but only selecting from the remaining unshuffled cards

# Fisher-Yates Shuffle Implementation
# This line is implementing a key part of the Fisher-Yates (or Knuth) shuffle algorithm, which is a method for generating a random permutation of a finite sequence.

# Breaking Down the Formula
# Current Position (i):
# As we iterate through the deck, i represents the current position we're working on
# Cards at positions 0 to i-1 are already shuffled
# We need to pick a random card from positions i through 51 to swap with
# Random Number Generation (random.randint(0,55)):
# Generates a random integer between 0 and 55
# The choice of 55 is arbitrary and could be any number ≥ 51
# A more standard implementation would use random.randint(i, 51) directly
# Modulo Operation (% (52 - i)):
# Takes the random number and constrains it to the range 0 to (51-i)
# This represents the offset from position i
# As i increases, the range of possible offsets decreases
# Final Position Calculation (i + ...):
# Adds the current position i to the random offset
# This gives us a position between i and 51 inclusive
# This ensures we only swap with unshuffled cards
# Example Walkthrough
# Let's trace through a few iterations:

# First iteration (i=0):
# We need a random position between 0 and 51
# random.randint(0,55) gives a number, say 37
# 37 % (52-0) = 37 % 52 = 37
# r = 0 + 37 = 37
# We swap cards at positions 0 and 37
# Middle iteration (i=25):
# We need a random position between 25 and 51
# random.randint(0,55) gives a number, say 42
# 42 % (52-25) = 42 % 27 = 15
# r = 25 + 15 = 40
# We swap cards at positions 25 and 40
# Last iteration (i=51):
# We need a random position of 51 only
# random.randint(0,55) gives a number, say 17
# 17 % (52-51) = 17 % 1 = 0
# r = 51 + 0 = 51
# We "swap" the card with itself (no change)
# Mathematical Properties
# The distribution of r is uniform across the range [i, 51] because:

# The modulo operation converts any uniform distribution into a uniform distribution over the range [0, modulus-1]
# Adding i shifts this uniform distribution to the range [i, i+modulus-1]
# Since modulus = 52-i, the range becomes [i, 51]
# This ensures that each card has an equal probability of ending up in any position, which is the key property of a proper shuffle algorithm.


# Why Modulo and (52-i) are Used
# Why Modulo (%)
# The modulo operation serves a critical purpose in the shuffle algorithm:

# Range Constraint:
# We need to select a random position between i and 51
# Using modulo converts any random number into a value within a specific range
# Uniform Distribution:
# Modulo preserves the uniformity of the random distribution
# If we have a uniform random number generator and take modulo N, we get a uniform distribution from 0 to N-1
# Efficiency:
# Instead of generating a random number in the exact range needed, we can generate a random number in any range and use modulo to constrain it
# This is a common technique in programming when you need random numbers in a specific range
# Why (52-i)
# The expression (52-i) is crucial because:

# Remaining Cards:
# 52 is the total number of cards in the deck
# i is the current position in the iteration
# 52-i represents the number of cards that haven't been shuffled yet
# Decreasing Range:
# As i increases, 52-i decreases
# This ensures we only select from the remaining unshuffled cards
# For example:
# When i=0: We select from 52 cards (positions 0-51)
# When i=30: We select from 22 cards (positions 30-51)
# When i=51: We select from 1 card (position 51 only)
# Avoiding Redundant Shuffling:
# Cards at positions 0 to i-1 are already properly shuffled
# Re-shuffling them would waste computation and potentially introduce bias
# Using (52-i) ensures we only consider positions i through 51
# The combination of modulo and (52-i) creates an elegant way to select a random position from the remaining unshuffled portion of the deck, which is exactly what the Fisher-Yates algorithm requires for correctness.

# Feedback submitted

# 26m ago
# 12m ago
# 3m ago
# Press enter again to interrupt and send a new message