import time 

numeros = [111,7,2,1]
print(len(numeros))

numeros.append(52)
print(len(numeros))

print(numeros)

numeros.insert(0, 222)
print(len(numeros))
print(numeros)

numeros.insert(-1, 12)
print(numeros)

numeros.insert(1, 18)
print(numeros)

numeros.insert(-2, 99)
print(numeros)

time.sleep(5)