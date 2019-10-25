# Aly Batch
# 10.23.19
# Craps!

import random


# roll the dice
def rolldice():
    return random.randint(2, 12)


# create bank roll
def create():
    print('How much money ya got?')
    bank = input()


# create bet amount
def bet():
    print('How much ya bettin?')
    bet = input()


# Play the game
def playgame():
    roll = rolldice()
    if roll == 7 or roll == 11:
        print("You Win!")
        print(f"You rolled a {roll}")
    elif roll == 2 or roll == 3 or roll == 12:
        print("YOU LOSE")
        print(f"You rolled a {roll}")
    else:
        print(f"You rolled a {roll}")
        print("Let's roll again!")
        print('How much ya bettin?')
        bet = input()
        new_roll = rolldice()
        while new_roll != roll and new_roll != 7:
            new_roll = rolldice()
        if new_roll == roll:
            print('Win')
            print(f"You rolled a {roll}")
        else:
            print('YOU LOSE!')
            print(f"You rolled a {roll}")


# create total bank roll
create()
# create bet amount for current game
bet()
# rolldice
playgame()
