# HANGMAN #

import random

words = [
    "hangman",
    "chairs",
    "backpack",
    "bodywash",
    "clothing",
    "computer",
    "python",
    "program",
    "glasses",
    "sweatshirt",
    "sweatpants",
    "mattress",
    "friends",
    "clocks",
    "biology",
    "algebra",
    "suitcase",
    "knives",
    "ninjas",
    "shampoo",
]


def sketch(i):
    if i == 5:
        print("___")
    if i == 4:
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print("/ \\")

    if i == 3:
        print("  ___")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print("/ \\")

    if i == 2:
        print("  ___")
        print(" |   |")
        print(" |")
        print(" |")
        print(" |")
        print("/ \\")

    if i == 1:
        print("  ___")
        print(" |   |")
        print(" |   O")
        print(" |")
        print(" |")
        print("/ \\")

    if i == 0:
        print("  ___")
        print(" |   |")
        print(" |   O")
        print(" |  /|\\")
        print(" |  / \\")
        print("/ \\")


a = random.choice(words)

bos = []
for i in range(len(a)):
    bos.append("_")

print(" ".join(bos))

life = 5
while True:
    print("********************************************************")
    if bos.count("_") != 0:
        if life > 0:
            letter = input("Choose a letter: ")
            print("*")
            if len(letter) != 1:
                print("You need to enter a letter!!!")
            else:
                if a.count(letter) == 0:
                    life -= 1
                    sketch(life)
                    print(life, "lifes remanining.")
                else:
                    for i in range(0, len(a)):
                        if a[i] == letter:
                            bos[i] = letter
                print(" ".join(bos))
        else:
            print("You lost!")
            print("Words is:", a)
            break
    else:
        print("You won!!")
        break
