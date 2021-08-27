
from classes.Partisipant_class import Partisipant

class Dealer(Partisipant):
    '''Partisipant in the role of a dealer, whose actions are determined by the rules'''

    def __init__(self, name):
        super().__init__(name)
        self.hidden = True
        
    def show_hand(self):
        print('Dealers hand:')
        if self.hidden:
            print(f'With one hidden card: {self.hand[0]} and count of {self.hand[0].get_value}')
        else:
            super().show_hand()

    def hit(self, deck):
        super().hit(deck)
        print(f'Dealer {self.name} hits.' )
    
    def __get_hand_count(self):
        count = 0
        for c in self.hand:
            if c.get_value() in  ('jack', 'queen', 'king'):
                count += 10
            elif c.get_value() is 'ace':
                if count + 11 > 21: count+= 1
                else: count += 11
            else: count += int(c.get_value())

    def reset(self):
        super().reset()
        self.hidden = True

