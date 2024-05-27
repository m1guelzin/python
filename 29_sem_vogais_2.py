import time

s_vog = ""
uw = input("Declare uma palavra: ").upper()

for letra in uw:
    if letra in "AEIOU":
        continue
    else:
        s_vog += letra
    time.sleep(1)

print("Palavra sem vogais:", s_vog)

time.sleep(2)