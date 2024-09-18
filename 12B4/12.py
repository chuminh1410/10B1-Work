import random

"""
This program will produce an simulation of a coin flip.
"""
chance = 0
def CoinFlip(chance):
    prob = random.randint(0,100)
    if prob > 50:
        print("Heads")
    else:
        print("Tails")
    
CoinFlip(chance)