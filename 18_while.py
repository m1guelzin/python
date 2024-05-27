import time
#Variável de controle do loop while
controle = True
#Contador de vezes que o while vai repetir
contador = 0
#Enquanto o contador for menor que 10, o loop while exibe a mensagem
while controle == True:
    print("Série B!!!!")
    contador += 1
    if contador == 10:
        controle = False

time.sleep(2)