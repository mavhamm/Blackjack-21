# blackjack/21 attempt

import random

# 1. Create deck of 52 cards = ........................... create_deck()
# 2. Set the start-game -- study game rules
# 3. Get decision from player to draw or not
# 4. Method to pick a random card = ...................... card_draw()
# 5. Checks if it went over 21
# ?
# TODO: card names are dogshit, try Unicode symbols later


def create_deck():
    ''' Creates a 52-card deck. How:
    Creates a list of strings with 52 items, with cards named
    1_hearts, 2_clubs, K_diamonds, 10_spades, etc.
    It combines a list with every suit with another list of
    every card (i.e.: 1, 2, ... , J, Q, K)
    '''
    # strings to be made into lists with the split method
    all_numbers_letters = '1 2 3 4 5 6 7 8 9 10 J Q K'
    all_suits = 'hearts clubs spades diamonds'

    # making lists out of those strings
    suits_list = all_suits.split(' ')
    numbers_list = all_numbers_letters.split(' ')

    # concat each suit with each card
    all_cards = []
    suit_counter = 0
    for i in range(len(suits_list)):
        for i in numbers_list:
            all_cards.append(i + f"_{suits_list[suit_counter]}")
        suit_counter += 1
        if suit_counter > 3:
            break
    return all_cards


def card_draw():
    ''' Draws a card from the deck. How:
    Picks a random list item and find its index in the list
    Then using that index, pops that item from that list to card_draw'''
    card_index = deck.index(random.choice(deck))
    card_draw = deck.pop(card_index)
    return card_draw


deck = create_deck()
