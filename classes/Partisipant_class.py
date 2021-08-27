    #partisipant
    #   -hand cards:List
    #   -stand 
    #   -hit

class Partisipant:
        '''Partispipant in the game of blackjack'''
         
        def __init__(self, name):
            self.name = name
            self.hand = []

        def show_hand(self):
            print(f'{self.hand} with count: {self.__get_hand_count()}')
                    
        def hit(self, deck):
            self.hand.append(deck.draw())  

        def __get_hand_count(self):
            count = 0
            for c in self.hand:
                if c.get_value() in  ('jack', 'queen', 'king'):
                    count += 10
                elif c.get_value() is 'ace':
                    ace_choice = input('Count  as 11 (yes)? Otherwise 1.')
                    if ace_choice is 'yes': count += 11 
                    else: count += 1
                else: count += int(c.get_value())
            return count

        def reset(self):
            self.hand = []