import time
nm = "Os maiores números são iguais!!"

#Entrada de 5 números
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o quarto número: "))
n5 = int(input("Digite o quinto número: "))
#Comparação curtinha
nm = max(n1, n2, n3, n4, n5)
print("O número maior usando max é:", nm)
time.sleep(1)