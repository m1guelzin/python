import time

#Variáveis de controle dos números
numImpar = 0
numPar = 0

#Solicitar o 1o número ao usuário
num = int(input("Digite um número inteiro ou digite ou digite 0 para encerrar o programa: "))

#Enquanto o usuário não digitar zero, o while não termina.
while num != 0:
    #Verificar se é ímpar
    if num % 2 == 1:
        #Adciona 1 à variável numImpar
        numImpar += 1
    #Se não é ímpar, é par
    else:
        #Adciona 1 à variável numPar
        numPar += 1
    #Pede o próximo número ao usuário
    num = int(input("Digite um número inteiro ou digite ou digite 0 para encerrar o programa: "))

#Mostrar as quantidades dos números
print("Números Pares:", numPar)
print("Números Ímpares:", numImpar)

time.sleep(2)