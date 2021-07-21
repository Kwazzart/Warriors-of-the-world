import random

list = ("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM1234567890")

while True:
    lenth = input("Введите длину пароля: ")
    num = input("Введите колличество паролей: ")
    if lenth.isdigit() and num.isdigit():
        for i in range(int(num)):
            psw = ""
            for char in range(int(lenth)):
                psw += random.choice(list)
            print(psw)
    else: print("Вы ввели некорректные данные.")
