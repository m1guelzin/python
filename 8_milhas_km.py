import time
while True:
    opt = input("Você deseja converter: \n1- Milhas para Km\n2- Km para Milhas\nexit- Sair\n")
    if opt == "exit":
        break
    opt = int(opt)
    dist = float(input("Digite a distância a ser convertida:\n"))
    dist = int(dist)
    if opt == 1:
        dist = round(dist * 1.61, 2)
        print("A distância em Km é:", dist, "Km!")
        time.sleep(2)
    elif opt == 2:
        dist = round(dist * 0.62, 2)
        print("Sua distância em Milhas é:", dist, "Milhas!")
        time.sleep(2)
