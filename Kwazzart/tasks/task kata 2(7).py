def square_digits(num):
    answ = ""
    str_num = str(num)
    for i in range(len(str_num)):
        answ += str(int(str_num[i])**2)
    return int(answ)

print(square_digits(29))
