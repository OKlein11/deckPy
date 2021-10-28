import random
class Deck:
    def __init__(self) -> None:
        pass    
    def makeDeck():
        deckList = []
        card = {}
        suitNames = ("Hearts", "Diamonds", "Clubs", "Spades")
        for x in range(4):
            for y in range(13):
                if y == 0:
                    card = {"name" : "A " + suitNames[x], "value": 1, "suit": suitNames[x], "face" : "A"}
            
                if y > 0 and y < 10:
                    card = {"name" : str(y+1) + " " + suitNames[x], "value": y+1, "suit": suitNames[x], "face" : y+1}
                if y == 10:
                    card = {"name" : "J " + suitNames[x], "value": 10, "suit": suitNames[x], "face" : "J"}
                if y == 11:
                    card = {"name" : "Q " + suitNames[x], "value": 10, "suit": suitNames[x], "face" : "Q"}
                if y == 12:
                    card = {"name" : "K " + suitNames[x], "value": 10, "suit": suitNames[x], "face" : "K"}
                deckList.append(card)
        return deckList
            
    def makeShuffledDeck():
        shuffledDeck = Deck.makeDeck()
        random.shuffle(shuffledDeck)
        return shuffledDeck