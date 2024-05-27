import time

numero1 = float(input("Digite o número 1: "))
numero2 = float(input("Digite o número 2: "))

print("Adição:", numero1 + numero2)
print("Subtração:", numero1 - numero2)
print("Multiplicação:", numero1 * numero2)
print("Divisão 1/2:", numero1 / numero2)
print("Divisão 2/1:", numero2 / numero1)
print("Divisão inteira 1/2:", numero1 // numero2)
print("Divisão inteira 2/1", numero2 // numero1)
print("Resto da Divisão 1/2:", numero1 % numero2)
print("Resto da Divisão 2/1:", numero2 % numero1)
print("Potência 1/2:", numero1 ** numero2)
print("Potência 2/1:", numero2 ** numero1)

time.sleep(5)