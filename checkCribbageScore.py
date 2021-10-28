from itertools import combinations


class CheckHandScoreCribbage:
    def __init__(self, hand):
        from itertools import combinations
        self.hand = hand
        self.score = 0
        self.cardValues = list()
        if len(self.hand) != 5:
            print("ERROR: Hand does not have 5 cards")
            exit()
        for x in self.hand:
            self.cardValues.append(x["value"])


    def checkScore(self):
        self.checkForFifteens()
        self.checkForRuns()
        self.checkForPairs()
        self.checkForNobs()
        self.checkForFlush()
        return(self.score)


    def checkForFifteens(self):
        for z in [2,3,4,5]:
            combs = combinations(self.cardValues, z)
            for x in combs:
                cardSum = 0
                for y in x:
                    cardSum = cardSum + y
                if cardSum == 15:
                    self.score = self.score + 2


    def checkForRuns(self):
        runsArr = list()
        listOfRuns = list()
        validRuns = list()
        for x in self.hand:
            if x["face"] == "J":
                runsArr.append(11)
            elif x["face"] == "Q":
                runsArr.append(12)
            elif x["face"] == "K":
                runsArr.append(13)
            else:
                runsArr.append(x["value"])
        for z in [3,4,5]:
            combs = combinations(runsArr, z)
            for x in combs:
                y=list()
                for j in x:
                    y.append(j)
                y.sort()
                a= y[z-1] - y[0]
                b = z-1
                if a == b:
                    if len(y)  == len(set(y)):
                        listOfRuns.append(y)
        listOfRuns.reverse()
        for x in range(len(listOfRuns)):
            if len(listOfRuns[x]) == 5:
                validRuns.append(listOfRuns[x])
                break   
            elif len(listOfRuns[x]) == 4:
                validRuns.append(listOfRuns[x])
                validRuns.append(listOfRuns[x+1])
                break
            else:
                validRuns.append(listOfRuns[x])
        for x in validRuns:
            self.score = self.score + len(x)


    def checkForPairs(self):
        cardFaces = list()
        for x in self.hand:
            cardFaces.append(x["face"])
        for x in cardFaces:
            currentCard = x
            cardFaces.remove(currentCard)
            for y in cardFaces:
                if x == y:
                    self.score = self.score + 2


    def checkForNobs(self):
        cutSuit = self.hand[4]["suit"]
        for x in range(4):
            y = self.hand[x]["suit"]
            z = self.hand[x]["face"]
            if y == cutSuit:
                if z == "J":
                    self.score = self.score + 2
                    

    def checkForFlush(self):
        suit = self.hand[0]["suit"]
        flush = False
        for x in range(1, 4):
            if suit == self.hand[x]["suit"]:
                flush = True
            else: 
                flush = False
                break
        if flush == True:
            if self.hand[4]["suit"] == suit:
                self.score = self.score + 5
            else:
                self.score = self.score + 4
