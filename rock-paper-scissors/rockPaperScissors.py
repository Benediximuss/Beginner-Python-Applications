# ROCK PAPER SCISSORS #

import random

weapons = ["rock", "paper", "scissors"]

player_point = 0
cpu_point = 0
round = 1
while True:
    print("******************************************************************")
    if player_point == 3:
        print("Player wins!!!")
        break
    elif cpu_point == 3:
        print("CPU wins!!!")
        break
    else:
        print("ROUND", round)
        print(" ")
        cpu = random.choice(weapons)
        while True:
            playerinput = input("Choose a weapon: r / p / s ?  ")
            if playerinput == "r":
                player = "rock"
                break
            elif playerinput == "p":
                player = "paper"
                break
            elif playerinput == "s":
                player = "scissors"
                break
            else:
                print("Please enter a valid input!!!")

        result = [weapons.index(cpu), weapons.index(player)]

        print(player, "vs", cpu)

        k = 0
        if weapons.index(cpu) == weapons.index(player):
            k = 2

        elif result == [0, 1] or result == [1, 0]:
            if result.index(1) == 0:
                k = 0
            elif result.index(1) == 1:
                k = 1

        elif result == [0, 2] or result == [2, 0]:
            if result.index(0) == 0:
                k = 0
            elif result.index(0) == 1:
                k = 1

        elif result == [1, 2] or result == [2, 1]:
            if result.index(2) == 0:
                k = 0
            elif result.index(2) == 1:
                k = 1

        if k == 2:
            print("DRAW")
        elif k == 0:
            print("CPU GOT 1 POINT")
            cpu_point += 1
        elif k == 1:
            print("Player GOT 1 POINT")
            player_point += 1
        round += 1
        print("SCORE: Player =", player_point, "/", "CPU =", cpu_point)
