import time

numero = float(input("Digite um número:"))
while(numero < 0):
    numero = float(input("Erro!! Digite um número inteiro positivo:", ))
resultado = numero % 2
if resultado == 1:
    print("Tente outra vez!")
if resultado == 0:
    print('""P-A-R!!!""')   
print("Reinicie o Código")
time.sleep(4)