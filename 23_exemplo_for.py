import time
print("FOR 1: ")
for i in range (10):
    print("O valor atual do i é:", i)

    time.sleep(1)

print("FOR 2: ")
for i in range (2, 8):
    print("O valor atual do i é:", i)

    time.sleep(1)

print("FOR 3: ")
for i in range (2, 8, 3):
    print("O valor atual do i é:", i)
    time.sleep(1)

print()

#Exemplo de potência
print("Potência de 2: ")

potencia = 1
for expoente in range(16):
    print("2 à potência de", expoente, "é", potencia)
    potencia *= 2

time.sleep(5)