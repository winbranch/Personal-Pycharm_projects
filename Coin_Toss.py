import random
guess = ""
list = ['heads','tails']
while guess not in ('heads','tails'):
    print ('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.choice(list)# 0 is tails, 1 is heads
if toss == guess:
    print ('You got it!')
else :
    print ('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print ('You got it!')
    else:
        print ('Nope. You are really bad at this game.')