import time

n = int(input("Digite um número inteiro positivo: "))
cont = 0
while n != 1:
    if n % 2 != 0:
        n = n * 3 + 1
    else:
        n //= 2
    cont += 1
    print(n)
    time.sleep(1)


print("Número de repetições: ", cont)

time.sleep(2)