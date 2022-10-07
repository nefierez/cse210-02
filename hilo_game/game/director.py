from game.deck import Deck
from game.style import style


class Director:
    """A person who directs the game. 
    The responsibility of a Director is to control the sequence of play.
    """
    """ Attributes:

        dice (list): Number of the card dranw by the dealer.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The player wins 100 points if their guess is correct, they lose 75 points if not.
        total_score (int): The score for the entire game."""


    def __init__(self):
        #cosntructor a new director.
        #Args:
        #self (Director): An instance of Director.
        self.deck = Deck()
        self.is_playing = True
        self.score = 300
        self.previus_card = None
        self.current_card = None
        self.guess = None
       
    def start_game(self):
        """Start the game by running the main game loop.
        Args: 
            Self (Director): An instance of Director.
        """
        self.current_card = self.deck.draw_card()
        while self.should_continue():
            self.show_card()
            self.do_updates()
        self.game_over()

    def is_good_guess(self):
        """Difine the conditions to win the points.
        Args: 
            Self (Director): An instance of Director.
        """
        return (self.current_card > self.previus_card and self.guess == 'h') or (self.current_card < self.previus_card and self.guess == 'l')
            
    def show_card(self):
        """Define the previus and current card.
        Args: 
            Self (Director): An instance of Director.
        """
        print('')
        print(style.GREEN + 'The card is: ' + style.ENDC ,self.current_card)
        self.previus_card = self.current_card
        self.current_card = self.deck.draw_card()
        

    def do_updates(self):
       #updates the playe's score.
       #Args:
       #self(Director): An instance of Director.
        if self.current_card is None:
            print(style.MAGENTA + 'That was the last card' + style.ENDC)
            self.is_playing = False
        else:
            self.input_and_validation()
            print('Next card was: ', self.current_card)
              
            if self.is_good_guess():
                self.score += 100
            else:
                self.score -= 75
            
            print(style.CYAN + 'Your score is: ' + style.ENDC, self.score)
            if self.score > 0:
                play_again = input('Would you like to continue? [y/n]: ').lower()
                self.is_playing = play_again == 'y'

    def should_continue(self):
        """Make the rules to continue the hilo game
        Args: 
            Self (Director): An instance of Director.
        """
        return self.is_playing and self.current_card is not None and self.score > 0

    def game_over(self):
    
        """Display the game over message and the final score
        Args: 
            Self (Director): An instance of Director.
        """
        print('')
        print(style.RED + 'GAME OVER' + style.ENDC)
        print(style.CYAN + style.BOLD + 'Final Score: ' + style.ENDC , self.score)

    def input_and_validation(self):
        """Display the input and make the input validation
        Args: 
            Self (Director): An instance of Director.
        """
        while True:
            self.guess = input(style.BLUE + 'The next card will be higher or lower? '+ style.ENDC + '[' + style.BOLD + 'h' + style.ENDC + style.BLUE + '/' + style.ENDC + style.BOLD + 'l' + style.ENDC + ']: ' ).lower()
            if self.guess != 'h' and self.guess != 'l':
                print(style.RED + 'Invalid Answer. Try again' + style.ENDC)
                continue
            else:
                break