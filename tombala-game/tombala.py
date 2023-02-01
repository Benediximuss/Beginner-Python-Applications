# TOMBALA GAME #

print("Welcome to the New Year's night fun(!)")
in_her = input("Please enter the Tombala card for Grandma: ")
in_your = input("Please enter the Tombala card for You: ")
in_drawn = input("Please enter the numbers drawn in the order: ")

print("----")

her = in_her.split("-")
your = in_your.split("-")
drawn = in_drawn.split("-")

k = 0
i = drawn[k]

while len(her) != 0 and len(your) != 0:
    if your.count(i) == 1 and her.count(i) == 1:
        print("Number", i, "is drawn. Grandma has it. You have it.")
        her.remove(i)
        your.remove(i)
        k = k + 1

    elif your.count(i) == 1:
        print("Number", i, "is drawn. You have it.")

        your.remove(i)
        k = k + 1

    elif her.count(i) == 1:
        print("Number", i, "is drawn. Grandma has it.")
        her.remove(i)
        k = k + 1

    elif your.count(i) == 0 and her.count(i) == 0:
        print("Number", i, "is drawn.")
        k = k + 1

    if k < len(drawn):
        i = drawn[k]

print("----")

if len(your) < len(her):
    print("You win.")
    print("Remaining numbers of Grandma:", "-".join(her))

elif len(your) > len(her):
    print("Grandma win.")
    print("Remaining numbers of you:", "-".join(your))

elif len(your) == len(her):
    print("Grandma and You finish at the same round. It's a tie!")
