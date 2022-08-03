import random

class Player:

    def __init__(self, health = 3, coins = 5, gameover = False):
        self.health = health
        self.coins = coins
        self.gameover = gameover

    def __repr__(self):
        tale = f'This Player has {self.health} health points left and {self.coins} coins.'

        return tale 
    
            

class Adventure:
    
    def __init__(self):
        self.title = "TEXTY'S ADVENTURE"
        self.name = input("What is your name? ")
        self.is_good = True

        def health_up(self):
            Player().health += 1
        
        def health_down(self):
            Player().health -= 1
        
        def coins_up(self):
            Player().coins += 5

        def coins_down(self):
            Player().coins -= 5

    def random_events(self):
        rand = random.randint(0, )
        events = [self.health_down, self.health_up, self.coins_down, self.coins_up]
        good_events = 0
        bad_events = 0

        if rand % 2 == 0:
             good_events = events[rand]
             return good_events
        else:
            bad_events = events[rand]
            self.is_good = False
            return bad_events
            


    def __repr__(self):
        left_or_right = input("Do you go left or right? ")
        response = ''
        if 'left' in left_or_right.lower() and self.is_good == True:
            response = 'You decided to go left'
        script = f"""\n*{self.title}* \n \nHello {self.name}, and welcome to Texty's Adventure.
        All adventures start with these stats: \nHealth - {Player().health}
                    \nCoins - {Player().coins}\n\nThroughout this adventure you will be given a choice between going
                    right or left. There will be random encounters that happen at every turn. Good luck.
                    \nYou begin walking down a road when you come to a fork. {left_or_right} """
        return script
        

adventure = Adventure()
print(adventure)

