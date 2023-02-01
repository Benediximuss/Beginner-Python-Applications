import random

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', # len.lowers : 26
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', # len.uppers : 26
'!', '=', ':', '.', ',', '/', '*', '+', '-', '?', '(', ')', '&', '#', '@', '_', ' ', '\n', # len.symbols : 17
'1','2','3','4','5','6','7','8','9','0'] # len.numbers : 10   

 # len.total : 79

def shuffle(x_original): # appends all elements of x to y in random order and returns the list y
    x = [i for i in x_original]
    y = []
    l = len(x)
    k = 0
    while k != l :
        tempidx = x.index(random.choice(x))
        y.append(x[tempidx])
        x.pop(tempidx)
        k += 1
    return y

def encrypt(txt,database):
    aidx = shuffle(list(range(len(database))))  ## shufles the original code i.e : 0123 .. -- >  3120 ...
    code = ""

    for i in aidx :  # adjust the code i.e : 0123 --> 00010203
        if i < 10 :
            code += "0" + str(i)
        elif i >= 10 :
            code += str(i)

    newdic = { }
    for i in range(len(database)) : # creates new dictionary ( keys and values are reversed for encryption )
        newdic[database[aidx[i]]] = database[i]

    etxt = "" # creating the new word in new language
    for i in txt :
        etxt += newdic[i]

    return (etxt,code) # tuple containing crypted text and cryption code


def decrypt(crypted,code,database):
    code_list = []
    k = 0  # decode the code
    while k != len(code) :
        code_list.append(int(code[k:k+2]))
        k += 2

    xx = {} # create the dictionary of the given code
    for i in range(len(database)) :
        ch = database[i]
        xx[ch] = database[code_list[i]]

    decrypted = "" # decode the word
    for i in crypted :
        decrypted += xx[i]

    return decrypted # decrypted text

while True :
    print("Encrypt the file [1] \nDecrypt the file [2] \nTerminate code [3]")
    dec = input()
    print()
    if dec == "1" :
        while True:
            fname = input("Please enter a file name to encrypt: ")
            try:
                txtfile = open(fname,"r")
                raw_txt = txtfile.read()
                txtfile.close()

                encryption_tuple = encrypt(raw_txt,characters)
                new_txt = encryption_tuple[1] + "\n" + encryption_tuple[0]

                txtfile = open(fname,"w")
                txtfile.write(new_txt)
                txtfile.close()
                print("Encryption completed!")
                break
            except:
                print("There is no such file named", "'"+fname+"'")
                print("Please enter a file name again!\n")

    elif dec == "2" :

        while True:
            fname = input("Please enter a file name to decrypt: ")
            try:
                txtfile = open(fname,"r")
                enc_txt = txtfile.read()
                txtfile.close()

                n = enc_txt.index("\n")
                en_code = enc_txt[:n]
                en_str = enc_txt[n+1:]

                decrypted_str = decrypt(en_str,en_code,characters)

                txtfile = open(fname,"w")
                txtfile.write(decrypted_str)
                txtfile.close()

                print("Decryption completed!")
                break
            except:
                print("There is no such file named", "'"+fname+"'")
                print("Please enter a file name again!\n")
    elif dec == "3" :
        print("Terminating..")
        break
    else:
        print("Invalid, try again!\n")
        pass
