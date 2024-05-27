import time

blocos = int(input("Insira o número de blocos: "))  
inic = blocos
altura = 0
camadas = 0

#Enquanto o número de blocos for maior ou igual ao número de blocos por camada + 1
while blocos >= camadas + 1:
    #aumenta o número de blocos da camada
    camadas += 1
    #tira os blocos do montante igual à nova camada
    blocos -= camadas
    #contabiliza a camada formada
    altura += 1

#Diz a altura final após os cálculos
print("Altura da pirâmide:", altura)
print("Número de blocos utilizados:", inic - blocos)

time.sleep(2)