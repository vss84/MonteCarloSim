import random as random

coin = [] #create coin
for i in range(0,2): #add imaginary heads and tails
    coin.append(i)

coinOdds = len(coin) - 1 #bet odds

def coin_flip(): #flip a coin using a pseudorandom generator, returns result of the flip
    outcome = random.choice(coin)
    return outcome

def betting(amount): #bet amount and your coin side will be chosen randomly
    side = random.choice(coin)
    if str(side) == str(coin_flip()):
        return amount*coinOdds #if you bet and win you get +1, losing is -1 thus making a fair EV game
    else: return -amount

def play_coin_flip(numToss, bet, toPrint):
    totEarnings = 0
    for i in range(numToss):
        coin_flip()
        totEarnings += betting(bet)
    if toPrint:
        print(numToss, 'Coin tosses')
        print('Expected return betting', "random side", '=',
               str(100*totEarnings/numToss) + '%\n')
    return (totEarnings/numToss)

for numToss in (100, 1000, 10000, 1000000):
    for i in range(3):
        play_coin_flip(numToss, 1, True)

