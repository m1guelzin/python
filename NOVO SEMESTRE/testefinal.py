try:
    print(10 / 0)
    break
except ZeroDivisionError:
    print("Ocorreu um erro de divisão por zero...")
except (ValueError, TypeError):
    print("Ocorreu um erro de valor ou tipo...")
except:
    print("Ocorreu um erro desconhecido...")
 
 