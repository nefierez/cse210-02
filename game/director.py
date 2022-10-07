from game.cards import Cards


class Director:
    """A person who directs the game. 
    The responsibility of a Director is to control the sequence of play.
    """
    """ Attributes:

        dice (list): Number of the card dranw by the dealer.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The player wins 100 points if their guess is correct, they lose 75 points if not.
        total_score (int): The score for the entire game."""


    def __int__(self):
        #cosntructor a new director.
        #Args:
        #self (Director): An instance of Director-

        self.card = ()
        self.is_playing = True
        self.score = 300
       
    def start_game(self):
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs():
        
        if points == 0:
            print('Sorry, you have lost the game.')
        else:
            answer = print(input('Would you like to continue? Y/N'))
            if answer == 'Y'.upper:
                print('Higher or lower?') 
            else:              
                print('Thank you for playing.')

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
        
    def do_output(self):
    
        """Display the players score based on if they guessed right.
        Args: 
            Self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
    
        if ((self.guess == "h" and self.current_card > self.previous_card) or
        (self.guess == "l" and self.current_card < self.previous_card)):
            self.points += 100
    
        elif ((self.guess == "l" and self.current_card > self.previous_card) or
        (self.guess == "h" and self.current_card < self.previous_card)):
            self.points -= 75
    
        print(f'Your score is: {self.points}')
        
        if self.points <= 0:
            self.is_playing = False
            print('')
            print('Game over. You ran out of points.')