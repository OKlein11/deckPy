from createDeck import Deck
class Hands:
    def __init__(self):
        pass
        
    def deal(self, people, number):
        self.deck = Deck.makeShuffledDeck()
        numberCards = number
        numPeople = people
        hands= list()
        for y in range(numPeople):
            hands.append(list())
        for x in range(numberCards):
            for y in range(numPeople):
                hands[y].append(self.deck[0])
                self.deck.pop(0)
        return hands
    def dealFromCreatedDeck(deck, people, number):
        numberCards = int(number)
        numPeople = int(people)
        deckCards= deck
        cardHands= list()
        for y in range(numPeople):
            cardHands.append(list())
        for x in range(numberCards):
            for y in cardHands:
                y.append(deckCards[0])
                deckCards.pop(0)
        return  cardHands