import time

#criando uma lista dentro de uma outra lista usando o for
lista = [[x for x in range(4)] for i in range(5)]

print(lista)

lista2 = [12,17,22,45,32]

print(lista2)

lista2.sort()

print(lista2)

print(lista2[3])

lista2.reverse()

print(lista2)


list_1 = [1, 2]
list_2 = list_1
list_1 [0] = 2
list_1 [1] = 3
print(list_2)
print(len(list_2))

time.sleep(3)