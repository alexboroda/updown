#!/usr/bin/python
from random import randint

suits = ['hearts', 'diamonds', 'spades', 'clubs']
colors = ['red', 'black']
values=['1','2','3','4','5','6','7','8','9','10','jack', 'queen','king','ace']
picked = []

deck = []
your_cards = []

for card in range(0,51):
        for suit in suits:
                 for color in colors:
                        for value in values:
                                deck.append({'color' : '%s' % color, 
                                      'suit' : '%s' % suit,
                                      'value' : '%s' % value})
#pick a random card
your_color = raw_input("Pick a color: ")
your_cards.append(deck[randint(0,52)])
if your_color != your_cards[0]['color']:
        print "drink"
else:
        print "give a drink"

your_value = raw_input("High or low? ")
your_cards.append(deck[randint(0,52)])

print your_cards
# TODO: compare face cards
if (your_cards[1]['value'] > your_cards[0]['value']) and your_value == 'high' :
        print "give a drink"
elif (your_cards[1]['value'] < your_cards[0]['value']) and your_value =='low':
        print "give a drink"
else:
        print "take a drink"
