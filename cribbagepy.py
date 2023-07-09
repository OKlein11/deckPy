import deckpy
import random
from itertools import combinations

class CribbagePlayer(deckpy.Player):
    def __init__(self, name):
        super().__init__(name)
        self.score = 0

    def putCardIntoCrib(self,card):
        self.crib.add(card)
        self.discard(card)

class Cribbage:
    def __init__(self,players):  ##players is a list of strings
        self.players = []
        for player in players:
            self.players.append(CribbagePlayer(player))
        self.chooseDealer()

    def chooseDealer(self): #of the players, choose one at randome to be the dealer
        self.dealer = self.players[random.randint(0,len(self.players)-1)]

    def nextDealer(self): #move dealer to the next person in the list
        x = self.players.index(self.dealer)
        x = x + 1
        x = x % len(self.players)
        self.dealer = self.players[x]
    
    def cutDeck(self):
        self.cut = self.deck.pop(random.randint(1,len(self.deck)-2))
        self.checkForCutNobs()

    def checkForCutNobs(self):
        if self.cut.value == 11:
            self.dealer.score = self.dealer.score + 2


class CribbageTwoPlayer(Cribbage):
    def __init__(self,players):
        super().__init__(players)

    def newHand(self):
        self.deck = deckpy.Deck()
        self.deck.shuffle()
        for x in range(6):
            for z in range(len(self.players)):
                self.players[(self.players.index(self.dealer)+z+1)%len(self.players)].draw(self.deck)
        self.crib = Crib()
        for player in self.players:
            player.crib = self.crib
    
    



class Crib:
    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def show(self):
        for card in self.cards:
            card.show()


class HandScorer:
    def __init__(self, player, cut=None, isCrib=False):
        self.hand = player.hand
        self.cut = cut
        self.allCards = []
        for x in self.hand:
            self.allCards.append(x)
        self.allCards.append(cut)
        


class Scorer:
    def __init__(self, cards):
        self.cards=cards
        self.total=0

    def flush(self):
        pass

    def nobs(self, cut):
        for x in self.cards:
            if x.suit == cut.suit and x.value == 11:
                self.total = self.total + 1

    def fifteens(self):
        pass

    def runs(self):
        pass #sort all 5 cards, remove every combination of 2 cards, check if it's a run

    def pairs(self):
        pass #create every 2 card combination, check if their value is the same
