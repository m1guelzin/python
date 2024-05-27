import time

uw = input("Declare uma palavra: ").upper()

for letra in uw:
    if letra in "AEIOU":
        continue
    else:
        print(letra)
    time.sleep(1)



time.sleep(2)