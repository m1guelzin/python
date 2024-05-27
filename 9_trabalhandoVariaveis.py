#acionando a função time
import time

#acionando a função de sistema "OS"
import os

print("Iniciando o Sistema!")
time.sleep(3)
os.system("cls") #Limpa a tela

var = 1
print (var)
var = var + 10
print (var)

#torna a variavel var para a variavel "Amor"
var = "Amor"
print (var)
#imprime a variavel 10 vezes quebrando a linha por conta do "\n"
var = (var + "\n") * 10
print (var)

#linha de separação
print()
#exercicio teorema de pitagoras
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5 
print(c)

os.system("cls")

#Expressões completas
x = 2
y = 3

x = x * 2 #Número * 2
print(x) #4

y = y + 1 #número + 1 (incremento)
print(y) #4

#Forma abreviada (atalho)
x *= 2 
print(x) #8

#Forma abreviada (atalho do incremeto)
y += 1
print(y) #5

y -= 1
print(y) #4

print("---------------------------------")
os.system("cls")

#Arredondando um valor
_decimal = 54.6 
print(round(_decimal))

print("---------------------------------")

#Testando o INPUT
# anything = float(input("Digite um número: "))
# something = anything ** 2
# print(anything, "Elevado a 2 é", something)

os.system("cls")

#comando "STR" -----------------------------------------------------
valor = 100
print("valor:", valor)

#qual o TIPO de valor?
print("Tipo da variavel:",type(valor))

#convertendo valor para string
print("Tipo novo da variavel:",type(str(valor)))
print("Novo valor:",valor)
print("valor vezes 2:",valor * 2)

valor = str(valor)
print(type(valor))
print("Valor vezes 2(???):", valor * 2)

#qual o tipo de x
x = int(input("Digite um número: "))
print(x * "5")
y = input("Digite um número: ")
print(type(y))

#espera de 5 segundos para execução do código
time.sleep(5)
