   
   
import random
import itertools   

from classes.Card_class import Card
   
    #Deck  
    #   -cards: List of Cards 
    #   draw() -> card
    #   shuffle() (empty all hands)
class Deck:
    def __init__(self, colors, values):
        self.cards = []
        card_list = list(itertools.product(colors,values))
        for c in card_list:
            card = Card(c[0], c[1])
            self.cards.append(card)

        
    def draw(self):
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)

    def get_size(self):
        return len(self.cards)