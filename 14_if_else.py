#Como identificar o maior de dois números
import time

#Ler dois números
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

#verificando qual é o maior número
if num1 > num2:
    numMa = num1
    numMe = num2

    print("O número maior é", numMa)
    print("O número menor é", numMe)

elif num2 > num1:
    numMa = num2
    numMe = num1

    print("O número maior é", numMa)
    print("O número menor é", numMe)
else:
    print("Nenhum é maior")

#Outra notação de if else em Python

if num1 > num2:
    
    numMa = num1
    numMe = num2

    print("O número maior é", numMa)
    print("O número menor é", numMe)
else num2 > num1:

    numMa = num2
    numMe = num1

    print("O número maior é", numMa)
    print("O número menor é", numMe)


time.sleep(5)