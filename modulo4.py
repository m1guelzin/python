import time

# #exemplo de função
# def somar():
#     n1 = int(input("Digite o primeiro numero da adição: "))
#     n2 = int(input("Digite o segundo numero da adição: "))
#     print(n1 + n2)

# somar()

# #segundo exemplo de função
# def soma2(n1, n2):
#     soma = n1 + n2
#     return soma
# print("Soma 2:", soma2(22,20))

# #terceiro exemploi de função
def soma3(n1,n2):
    return n1 + n2

# # numero1 = float(input("Digite um numero: "))
# # numero2 = float(input("Digite outro numero: "))

# # #chamada de função
# # print(soma3(numero1, numero2))

#chamada de função por argumentos
print(soma3(n2 = 12, n1 = 5))

#função com parametros default (padrao)
def soma4(n1 = 0, n2 = 0):
    return n1 + n2

print(soma4(50, 25))
print(soma4())

#função com apenas alguns valores default 
def soma5(n1, n2 = 0):
    return n1 + n2

print(soma5(50, 25)) #75
#print(soma5()) #erro
print(soma5(10)) #10
print(soma5(n2 = 51, n1 = 12))

def soma6(n1, n2):
    if n1 == 1:
        return 1

print(soma6 (1,3)) #True
print(soma6 (13,3)) #None

print(soma6(1, 2) + 10) #Mostra 11
#print(soma6(2, 2) + 10) #Mostra type nao suportado 

time.sleep(3)