import time

#etapa 1
beatles = []

#etapa 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

print("Banda inicial", beatles)

#etapa 3
for i in range(2):
    novo_membro = (input("Digite o nome de um novo membro da banda (Stu Sutcliffe ou Pete Best):"))
    beatles.append(novo_membro)
    print(beatles)
time.sleep(0.5)

#etapa 4
print("Saida dos membros", beatles[-2], beatles[-1])
time.sleep(1)

del beatles[-2]
del beatles[-1]
time.sleep(1)

print(beatles)
time.sleep(1)

#etapa 5
print("Entrada de Ringo Starr")
beatles.insert(0, "Ringo Starr")
time.sleep(1)

print("Lista final dos beatles", beatles)
print("O FABULOSO", len(beatles))

time.sleep(5)