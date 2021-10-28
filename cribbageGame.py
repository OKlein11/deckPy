import tkinter as tk

from pyglet import text
from createDeck import Deck
from createHands import Hands
from checkCribbageScore import CheckHandScoreCribbage
from findBestCribbageHand import findBestCribbageHand
window = tk.Tk()
deck = Hands()
hands = deck.deal(2,6)
handLabel =tk.Label(text=hands[0])
handLabel.pack()
window.mainloop()