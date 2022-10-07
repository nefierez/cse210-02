import random

class Deck:
    """A deck that holds 13 cards. The responsibility of Cards is to assign the card number drawn by the dealer to the
    self.value variable.

    Attributes:
        value (int): Will hold the card number drawn by the dealer."""
    def __init__(self):
        self.cards = [*range(1,14,1)]
        random.shuffle(self.cards)
    
    def draw_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        return None