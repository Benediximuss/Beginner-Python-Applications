import random

letters = "a-b-c-d-e-f-g-h-j-k-l-m-n-o-p-r-s-t-u-v-y-z-q-x"
let = letters.split("-")
cap = ["up", "low"]
allwords = []

k = 0
while k != 1000:  # how many words
    wordlen = random.choice(range(5, 15))
    tempword = ""
    l = 0
    while l != wordlen:
        if random.choice(cap) == "up":
            tempword += random.choice(let).upper()
        else:
            tempword += random.choice(let).lower()

        l += 1
    k += 1
    allwords.append(tempword)

lineslist = []

line = 0
while line != 10**3:  ## how many lines ?
    # print("Line:", line, "\n--------")

    line_adet = random.choice(range(15, 50))
    linelist = []

    q = 0
    while q != line_adet:
        urun = random.choice(allwords)
        adet = random.choice(range(0, 30))
        entry = urun + "_" + str(adet)
        linelist.append(entry)

        q += 1

    lineslist.append("-".join(linelist))

    line += 1

final = "\n".join(lineslist)

nf = open("output.txt", "w")
nf.write(final)
nf.close()

print("DONE")
