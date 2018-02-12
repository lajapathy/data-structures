
from card_deck import cardDeck
class Dealer:

    def __init__(self,player_list):
        #Create a card deck object. Assuming that we are playing with one deck
        self.cd = cardDeck()
        self.player_list=player_list
        self._initial_deal()


    def _initial_deal(self):
        for player in self.player_list:
            self.deal_to_player(player,2)

    def deal_to_player(self,player,count):
        for i in xrange(count):
            player.add_card(self.cd.get_random_card())