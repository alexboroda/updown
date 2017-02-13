#!/usr/bin/python

suits = ['hearts', 'diamonds', 'spades', 'clubs']
colors = ['red', 'black']
values=['1','2','3','4's]
values.append(range(1-10))
values.append(['jack', 'queen','king','ace'])

deck = []

for card in range(0,52):
        for suit in suits:
                for color in colors:
                        for value in values:
                                deck.append({'color' : '%s' % color, 
                                      'suit' : '%s' % suit,
                                      'value' : '%s' % value})
# print deck
print values