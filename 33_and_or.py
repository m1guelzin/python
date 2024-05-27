import time

var = 0

# print(var > 0) #False
# print(not(var <= 0)) #not True = False

# print()

# print(var != 0) #False
# print(not(var == 0)) #not True = False

# print()

# p = 1
# q = 0
# analise1 = not(p and q) == (not p) or (not q)
# print(analise1)

# print()

# analise2 = not(p or q) == (not p) and (not q)
# print(analise2)

# i = 15
# j = 22

# print(bin(i))
# print(bin(j))

# print()

# print(i & j) # 6 = 0110

# print()

# print(bin(i & j))

# print()

# print(bin(~i))

# print()

# print(bin(~j))

# print()

# print(i | j)

# print()

# print(i ^ j)

# print()

#Testes com deslocamento de casas

# var = 17

# var_direita = var >> 1
# var_esquerda = var << 1

# print(var, var_direita, var_esquerda)

#Teste com listas:

numeros = [10, 5, 7, 2, 1]

print("Conteúdos originais da lista:", numeros)

print(numeros[4])

numeros[0] = 111
numeros[1] = numeros[4]

print("Conteúdos atualisados da lista:", numeros)

print("Tamanho da lista", len(numeros))

print("Atualização")
del numeros[1]
print(numeros)
print(numeros[-1])

time.sleep(2)