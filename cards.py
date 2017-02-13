#!/usr/bin/python
from random import randint

suits = ['hearts', 'diamonds', 'spades', 'clubs']
colors = ['red', 'black']
values=['1','2','3','4','5','6','7','8','9','10','jack', 'queen','king','ace']

deck = []

for card in range(0,51):
        for suit in suits:
                for color in colors:
                        for value in values:
                                deck.append({'color' : '%s' % color, 
                                      'suit' : '%s' % suit,
                                      'value' : '%s' % value})
#print deck

#pick a random card
print deck[randint(0,52)]