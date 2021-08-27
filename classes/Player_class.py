from classes.Partisipant_class import Partisipant

#player:partisipant
#   -hand
#   -purse
#   -bet
#   surrender()
class Player(Partisipant):
    '''Partisipant in the role of a player, able to bet or surrender (and later use side rules)'''

    def __init__(self, name, purse):
        super().__init__(name)
        self.purse = purse 
        self.bet = 0
        self.stands = False
        print(f'Player {self.name} initalized')

    def hit(self, deck):
        super().hit(deck)
        print(f'Player {self.name} hits.' )

    def stand(self):
        self.stands = True
        print(f"The player {self.name} stands")

    def reset(self):
        super().reset()
        self.bet = 0
        self.stands = False