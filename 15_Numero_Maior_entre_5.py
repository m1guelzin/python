import time

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
num4 = float(input("Digite o quarto número: "))
num5 = float(input("Digite o quinto número: "))

#Assumir que o numero 1 é o maior
numeroMaior = num1

#verificar se o segundo numero é maior q o primeiro
if(num2 > numeroMaior):
    numeroMaior = num2
    #caso positivo, atualiza a variavel
if(num3 > numeroMaior):
    numeroMaior = num3
    #caso positivo, atualiza a variavel
if(num4 > numeroMaior):
    numeroMaior = num4
    #caso positivo, atualiza a variavel
if(num5 > numeroMaior):
    numeroMaior = num5 
    #caso positivo, atualiza a variavel

print("O número maior é:", numeroMaior)

time.sleep(2)

#Outra forma com a função inteira do python chamada MAX
numeroMaior2 = max(num1, num2, num3, num4, num5)
print("O maior valor com MAX é:", numeroMaior2)


time.sleep(2)
