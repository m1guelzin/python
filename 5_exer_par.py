while True:
    num = int(input("Digite um número par: "))
    if (num >= 0): #Se o número for positivo
        if (num % 2 == 0): #Se o número for par
            print('""P-A-R!!!""')
            break
        else: #Se o número for ímpar
            print('"Tente outra vez!!"')
    else: #Se não for positivo
        print('"Tente outra vez!!"')