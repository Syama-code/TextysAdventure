import random

class Player:

    def __init__(self, name = input("What is your name? "), coins = 5):
        self.name = name
        self.coins= coins

    def __repr__(self):
        tale = f'{self.name} has {self.coins} coins.'

        return tale 

class Adventure:


    def __init__(self):
        pass

player1 = Player()
print(player1)

