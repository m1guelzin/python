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



#Conferidor de aposta em loteria
sorteado = [5,11,9,42,3,49]
apostados = [3,7,11,42,34,49]
acertos = 0

for numero in sorteado:
    if numero in apostados:
        acertos += 1

print("Acertou", acertos, "numeros sorteados")

#remoção de numeros repetidos em uma lista
lista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
print("Lista original: ", lista)

#lista de paoio
vistos = []

#Iterar pela lista original de tras para frente
for i in range(len(lista) - 1, -1, -1):
    #se o numero ja esta na lista "vistos", removê-lo da lista original
    if lista[i] in vistos:
        del lista[i]
    else:
        #caso contrario, adicionar a lista "vistos"
        vistos.append(lista[i])
print("Lista modificada: ",vistos)
    


#LISTAS AVANÇADAS
#2D - Listas aninhandas bidimensionais
tabela = [[":(", ":)", ":|", ";-;"],
          [";-;", ":|", ":)", ":("],
          [":|", ":)", ";-;", ":("]]
print(tabela[0][3])
print(tabela)

#3D - Matriz Tridimensional
cubo = [[[":(", "y", "z"],
         [":)", "y", "z"],
         [":|", "y", "z"]],
        [["amor", "ódio", "caridade"],
         ["paz", "esperança", "ferias"],
         ["tina", "prior", "pp"]],
        [["restinga", "patrocinio", "rifaina"],
         ["amazonence", "fluminense", "santos"],
         ["pizza", "lasanha", "pastel"]]]
print(cubo)
print(cubo[1])
print(cubo[1][0])
print(cubo[1][0][2])
time.sleep(3)