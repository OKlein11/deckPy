import cribbagepy
from deckpy import Card

def startHand():
    players = ["Owen","Ralph"]
    game = cribbagepy.CribbageTwoPlayer(players)
    print(f"Initial Dealer: {game.dealer.name}")
    game.newHand()
    print("Owen's Hand:")
    game.players[0].showHand()
    print("Ralph's Hand:")
    game.players[1].showHand()
    
def testNobs(): #Test the Scorer nobs function
    print("First Case: 6,J,Q,K of Diamonds in hand, 4 of diamonds cut\nShould come up nobs")

    cards = []
    for x in [6,11,12,13]:
        cards.append(Card("Diamonds", x))
    cut = Card("Diamonds", 4)
    scorer = cribbagepy.Scorer(cards)
    print(f"Initial Total: {scorer.total}")
    scorer.nobs(cut)
    print(f"Total after function: {scorer.total}")
    
    print("Second Case: 6,10,Q,K of Diamonds in hand, 4 of diamonds cut\nShould come up no nobs")

    cards = []
    for x in [6,10,12,13]:
        cards.append(Card("Diamonds", x))
    cut = Card("Diamonds", 4)
    scorer = cribbagepy.Scorer(cards)   
    print(f"Initial Total: {scorer.total}")
    scorer.nobs(cut)
    print(f"Total after function: {scorer.total}")
