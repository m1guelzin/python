import time

#Número maior inicial
M = -9999999999

#Contador
c = 0

#Enquanto o número for diferente de -1, repete
while True:
    
    #Solicita o próximo número
    N = int(input('Digite um número inteiro ou "-1" para sair: '))
    
    if N == -1:
        break
    
    c += 1
    #O número é maior que o maior número atual?
    if N > M:
        #Caso verdadeiro, maior número recebe numero.
        M = N
if c != 0:
    #Fala o maior número gravado
    print("O maior número digitado foi", M)
else:
    print("Você não digitou nenhum número!!!")

time.sleep(2)