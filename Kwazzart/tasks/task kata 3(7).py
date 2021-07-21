def decode(mes):
    letters = "abcdefghijklmnopqrstuvwxyz"
    answ = ""
    for i in mes:
        if i == " ":
            answ += " "
        else:
            for k in range(len(letters)):
                if i == letters[k]:
                    answ += letters[-k-1]
                    break
    return answ

print(decode("q"))
