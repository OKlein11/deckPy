from createDeck import Deck
from createHands import Hands
from checkCribbageScore import CheckHandScoreCribbage
from findBestCribbageHand import findBestCribbageHand
def main():
    score = [0,0]
    dealAndShowCards(score)

def dealAndShowCards(score):
    deck = Deck.makeShuffledDeck()
    hands = Hands.dealFromCreatedDeck(deck, 2, 6)
    print("PLAYER HAND:")
    i = 1
    printOutGroupOfCards(hands[0])
    cardsToBeCribbed= str(input("Type Which Cards To Place in Crib:"))
    crib = list()
    for x in cardsToBeCribbed:
        crib.append(hands[0][int(x)-i])
        hands[0].pop(int(x)-i)
        i+= 1
    printOutGroupOfCards(hands[0])
    aiPutsCardsInCrib(hands, crib, score)
def aiPutsCardsInCrib(hands, crib, score):
    cardsToPutInCrib = findBestCribbageHand(hands[1]).findWhichCardsToRemove()
    printOutGroupOfCards(hands[1])
    print("\n")
    printOutGroupOfCards(cardsToPutInCrib)
    for x in cardsToPutInCrib:
        crib.append(x)
        hands[1].remove(x)
    print("\n")
    printOutGroupOfCards(hands[1])



def printOutGroupOfCards(cards):
    i=1
    for x in cards:
        tempSuit = str()
        if x["suit"] == "Hearts":
            tempSuit = "\u2665"
        if x["suit"] == "Diamonds":
            tempSuit = "\u2666"
        if x["suit"] == "Spades":
            tempSuit = "\u2660"
        if x["suit"] == "Clubs":
            tempSuit = "\u2663"
        print(f"{i}.     {tempSuit} {x['face']}")
        i+= 1
if __name__=="__main__":
    main()