

class Player:

    def __init__(self):
        self.cards=[]
        self.total=0

    def add_card(self,card):
        self.cards.append(card)
        self.total+=card.value

    def get_total(self):
        return self.total