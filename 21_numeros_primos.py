import time

c = 1
sucesso = 0

num = int(input("Digite um número natural: "))

while (num - 1) > c :
    if num % (num - c) == 0:
        print("Seu número não é primo!!")
        c = num - 1
    else:
        sucesso += 1
        c += 1

if (num - 2) == sucesso:
    print("Parabéns, seu número é primo!!!")

if num <= 1:
    print(f"{num} não é primo.")

time.sleep(2)