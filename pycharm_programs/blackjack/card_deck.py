
import random
from card import Card

class cardDeck:

    def __init__(self):
        self.suits=['heart','spade','club','diamond']
        self.values=[{'A':1},{2:2},{3:3},{4:4},{5:5},{6:6},{7:7},{8:8},{9:9},{10:10},{'J':10},{'Q':10},{'K':10}]
        self.cards=[]
        self._generate_deck()


    def _generate_deck(self):
        for suit in self.suits:
            for value in self.values:
                self.cards.append(Card(suit,value[0]))

    def get_random_card(self):
        x= random.choice(self.cards)
        self.cards.remove(x)
        return x
