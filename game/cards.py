import random

class Card:
    """A deck that holds 13 cards. The responsibility of Cards is to assign the card number drawn by the dealer to the
    self.value variable.

    Attributes:
        value (int): Will hold the card number drawn by the dealer."""
    def __init__(self):
        self.value = 0
        self.points = 300

    def shuffle(self):
        self.value = random.randint(1, 13)
        self.points = self.points + 100 if self.value == True else self.points - 75