import time

ano = int(input("Digite um ano: "))
if (ano < 1582):
    print("Não está dentro do periodo do calendario gregoriano")
if (ano % 4 != 0):
    print("É um ano comum!")
elif (ano % 100 != 0):
    print("É um ano bissexto!")
elif (ano % 400 != 0):
    print("É um ano comum!!")
else:
    print("É um ano bissexto!!")

time.sleep(3)