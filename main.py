from checkCribbageScore import CheckHandScoreCribbage
from createDeck import Deck
from createHands import Hands
from findBestCribbageHand import findBestCribbageHand
def main():
    owenhands = Hands()
    hand = owenhands.deal(1,6)
    for x in hand[0]:
        print(x["name"])

    bestHand = findBestCribbageHand(hand[0]).findhand()
    print(bestHand[0])
    for x in bestHand[1]:
        print(x["name"])




if __name__=="__main__":
    main()
