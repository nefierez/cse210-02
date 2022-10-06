#Start with def main
def main():
    points = 300
#Interact with the player to see if they want to keep playing
#Also keeps track if the game is won or lost
    def keep_playing():
        if points == 0:
            print('Sorry, you have lost the game.')
        else:
            answer = print(input('Would you like to continue? Y/N'))
            if answer == 'Y'.upper:
                print('Higher or lower?') 
            else:              
                print('Thank you for playing.')

#Code a call to main
if __name__ == "__main__":
    main()

