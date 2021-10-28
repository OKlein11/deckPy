from checkCribbageScore import CheckHandScoreCribbage
from createDeck import Deck
from itertools import combinations
class findBestCribbageHand:
    def __init__(self, hand6):
        self.sixCardHand = hand6
        if len(self.sixCardHand) != 6:
            print("ERROR: Hand does not have 6 cards")
            exit()
        print("HAND: " + str(self.sixCardHand))
    def findhand(self):
        all4Hands = combinations(self.sixCardHand, 4)
        cardsInCut = Deck.makeDeck()
        
        for x in self.sixCardHand:
            cardsInCut.remove(x)
        averageHandScores = list()
        all4Hands = list(all4Hands)
        for x in all4Hands:
            averageCutScores=list()
            for y in cardsInCut:
                fiveCardHand = list(x)
                fiveCardHand.append(y)
                score = CheckHandScoreCribbage(fiveCardHand).checkScore()
                averageCutScores.append(int(score))
            average = sum(averageCutScores)/len(averageCutScores)
            averageHandScores.append(average)
        highestScore = max(averageHandScores)
        
        highestScorePosition = averageHandScores.index(highestScore)
        return([highestScore,all4Hands[highestScorePosition]])
    def findWhichCardsToRemove(self):
        all4Hands = combinations(self.sixCardHand, 4)
        cardsInCut = Deck.makeDeck()
        
        for x in self.sixCardHand:
            cardsInCut.remove(x)
        averageHandScores = list()
        all4Hands = list(all4Hands)
        for x in all4Hands:
            averageCutScores=list()
            for y in cardsInCut:
                fiveCardHand = list(x)
                fiveCardHand.append(y)
                score = CheckHandScoreCribbage(fiveCardHand).checkScore()
                averageCutScores.append(int(score))
            average = sum(averageCutScores)/len(averageCutScores)
            averageHandScores.append(average)
        highestScore = max(averageHandScores)
        
        highestScorePosition = averageHandScores.index(highestScore)
        bestHand = all4Hands[highestScorePosition]
        cardsToRemove = list(self.sixCardHand)
        for x in bestHand:
            cardsToRemove.remove(x)
        return(cardsToRemove)
        
