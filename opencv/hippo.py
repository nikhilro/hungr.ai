class Hippo(object):
    def __init__(self, n):
        self.color = n
        self.counter = 0
        self.move = False

    def update(self, p):
        """ Takes new location of the ball as a vector """
        self.move = False

    def chomp(self, bool):
        """ Determines the predicted location to make a decision to move"""
        self.move = bool

    def counter(self):
        self.counter = self.counter + 1
