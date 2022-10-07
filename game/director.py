from game.cards import Cards


class Director:
    """A person who directs the game. 
    The responsibility of a Director is to control the sequence of play.
    """


    def do_updates(self):
        #updates the playe's score.

        #Args:
        #self(Director): An instance of Director.

        if not self.is_playing:
            return

        for i in range(len(self.card)):
            cards =self.card[i]
            cards.display()
            self.score += cards.points
            self.total_score += self.score

            
