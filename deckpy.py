import random
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print(f"{self.value} of {self.suit}")


class Deck:
    def __init__(self):
        self.cards = []
        self.create()

    def create(self): ##build the deck.  For every suit, for every value, create a card and add it to the deck
        for suit in ["Diamonds", "Hearts", "Clubs", "Spades"]:
            for value in range(1,14):
                self.cards.append(Card(suit,value))
    
    def show(self): 
        for card in self.cards:
            card.show()

    def shuffle(self): ##Fischer-Yates shuffle
        for i in range(len(self.cards) -1,0,-1):
            r = random.randint(0,i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()

class Player:
    def __init__(self,name):
        self.name = name
        self.hand = []

    def draw(self,deck):
        self.hand.append(deck.drawCard())

    def discard(self,card):
        self.hand.remove(card)

    def showHand(self):
        for card in self.hand:
            card.show()

