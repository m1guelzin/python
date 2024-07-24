import time
while True:
    try:
        value = int(input('Digite um número natural: '))
        print("O reciproco",value, "é", 1/value)
    except ValueError:
        print("Número inválido!!!")
    except ZeroDivisionError:
        print("Zero não é um divisor!!!")
    except KeyboardInterrupt:
        break
    except:
        print("Algo de errado não está certo!!!")

time.sleep(2)