import time

#Encontrar o maior valor na lista - exemplo 1
lista = [17, 3, 11, 5, 1, 9, 7, 15, 18]
maior_numero = lista[0] #recebeu o numero 17

for i in range(1, len(lista)):
    if lista[i] > maior_numero:
        maior_numero = lista[i]
print("O maior numero da lista é:", maior_numero)

#Exemplo 2 
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 18]
maior = my_list[0]
for i in my_list:
    if i > maior:
        maior = i
print("O maior numero do exemplo 2 é:", maior)

#Exemplo 3
ultima_lista = my_list[:]
mel =ultima_lista[1:]
for i in ultima_lista:
        mel = i
print("O maior numero do exemplo 3 é:", mel)


#Encontrar a localização de um determinado elemento dentro de uma lista
frutas = ["abacaxi", "maçã", "pêra", "mamão", "uva", "melancia"]
elemento = "melancia"
achado = False

for i in range(len(frutas)):
    achado = frutas[i] == elemento
    if achado:
        break

if achado:
    print("Elemento encontrado no indice:", i)
else:
    print("NÃO ENCOTRADO")

time.sleep(4)