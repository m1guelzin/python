#Acionando a variavel time
import time

#Acionando a função de sistema OS
import os

os.system('cls') or None # Limpa a tela

print("Iniciando o sistema...")
time.sleep(3)

os.system('cls') or None # Limpa a tela

var = 1
print(var)
var = var + 10
print(var)
var = "amor"
print(var)
var = (var + "\n") * 10
print(var)
#imprimir 10 vezes a palavra amor quebrando a linha
var = "AMOR"
var = (var + "\n") * 10
print(var)
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
#exercício teorema de pitágoras
a = 3.0
b = 4.0

c = (a ** 2 + b ** 2) ** 0.5
print(c)

os.system('cls') or None

x = 2
y = 3

x = x * 2 #número * 2
print(x) #4

y = y + 1 #número + 1
print(y) #4

#Forma abreviada (atalho)
x *= 2
print(x)

y += 1
print(y)

y -= 1
print(y)


print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
os.system('cls')

#Arredondando um valor
_decimal = 54.6
print(round(_decimal))

print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
os.system('cls')

# #testando o input
# anything = float(input("Digite um número: "))
# something = anything ** 2.0
# print(anything, "elevado a 2 é", something)

print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
os.system('cls')

#comando str
valor = 100
print("Valor:", valor)
print("Tipo da variável:", type(valor))

#convertendo valor para string
print("Tipo novo da variavel:", type(str(valor)))

valor = str(valor)

print("Novo valor:", valor)
print("Número vezes 2:", valor * 2)








#espera 5 segundos
time.sleep(5)