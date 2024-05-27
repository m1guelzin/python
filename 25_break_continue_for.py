import time

#Exemplo com break
print("A instrução break: ")
for i in range (1, 6):
    if i == 3:
        break
    print("Dentro do laço:", i)
print("Fora do laço!")
print()
print()

#Exemplo com continue
print("A instrução continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro do laço:", i)
print("Fora do laço!!!")
time.sleep(2)