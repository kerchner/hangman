import sys

class Game:

    def __init__(self, phrase):
        """ Create a new point at the origin """
        self.phrase = phrase

    def play(self):
        print("This is where we play the game.  The phrase is ", self.phrase)



if __name__ == "__main__":
    game = Game(sys.argv[1])
    game.play()
