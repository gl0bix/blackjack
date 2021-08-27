"""
    Blackjack as a Python programm

    Rules:

    Blackjack is played with a 52-card deck without jokers.
    The cards 2 through 10 have their face value, J, Q, and K 
    are worth 10 points each, and the Ace is worth 
    either 1 or 11 points (player's choice).

    Each hand will result in one of the following events for the player:

    Lose - the player's bet is taken by the dealer.
    Win - the player wins as much as he bet. If you bet $10, you win $10 from the dealer (plus you keep your original bet, of course.)
    Blackjack (natural) - the player wins 1.5 times the bet. With a bet of $10, you keep your $10 and win a further $15 from the dealer.
    Push - the hand is a draw. The player keeps his bet, neither winning nor losing money.

    It is essentially a 1v1 game between Dealer and Player.
    There will always be a minimum bet and a maximum bet for the table. 
    The maximum bet is normally ten to twenty times the minimum bet.    

    At the start of a blackjack game, the players and the dealer receive 
    two cards each. The players' cards are normally dealt face up, 
    while the dealer has one face down (called the hole card) and one face up.

    The best possible blackjack hand is an opening deal of an ace with any ten-point card. 
    This is called a "blackjack", or a natural 21, and the player holding this automatically 
    wins unless the dealer also has a blackjack. If a player and the dealer each have a blackjack, 
    the result is a push for that player. If the dealer has a blackjack, all players not holding a blackjack lose.

    After the cards have been dealt, the game goes on with each player taking action - in clockwise order starting to dealer's left. 
    First, the player must declare if he wants to take advantage of the side rules (explained below). 
    You can only use the side rules once, when it's your turn to act after the deal.

    Then the player can keep his hand as it is (stand) or take more cards from the deck (hit), 
    one at a time, until either the player judges that the hand is strong enough to go up against 
    the dealer's hand and stands, or until it goes over 21, in which case the player immediately loses (busts).

    When all players have finished their actions, either decided to stand or busted, the dealer turns over his hidden hole card. 
    If the dealer has a natural 21 (blackjack) with his two cards, he won't take any more cards.

    If the dealer doesn't have a natural, he hits (takes more cards) or stands depending on the value of the hand. 
    Contrary to the player, though, the dealer's action is completely dictated by the rules. 
    The dealer must hit if the value of the hand is lower than 17, otherwise the dealer will stand.

    Whether or not the dealer must hit on a soft 17 (a hand of 17 containing an ace being counted as 11) differs.

    If the dealer goes bust, all players who are left in the game win. Otherwise players with higher point totals than the dealer win, 
    while players with lower totals than the dealer lose. For those with the same total as the dealer the result is a push

    To be implemented later: side rules
"""
#imports

import itertools 
import random

from classes.Deck_class import Deck
from classes.Card_class import Card
from classes.Dealer_class import Dealer
from classes.Player_class import Player

#consts

COLORS = frozenset(('Hearts', 'Spades', 'Diamonds', 'Clubs'))
VALUES = frozenset(('2','3','4','5','6','7','8','9','jack','queen','king','ace'))
    
#gameloop

#main
def game():
    
    #init partisipants

    #start round
    #cash out 
    #reset 
    #start next round


    deck = Deck(COLORS, VALUES)
    deck.shuffle()
    
    for card in deck.cards:
        print(card.get_value() + " " + card.get_color())

    dealer_1 = Dealer("Alice")
    player_1 = Player("Bob", 1000)

    print(deck.get_size())

    dealer_1.hit(deck)
    player_1.hit(deck)

    print(deck.get_size())

if __name__ == "__main__":
    game()