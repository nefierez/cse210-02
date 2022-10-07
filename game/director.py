from game.cards import Cards


class Director:
    """A person who directs the game. 
    The responsibility of a Director is to control the sequence of play.
    """
    def start_game(self):
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
            