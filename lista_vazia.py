import time

my_list = [] #criando lista vazia

for i in range(5):
    my_list.append(i + 1)
    print(my_list)

print("______________________________") #divisoria
#lista vazia 2
my_list2 = [] #criando segunda lista vazia

for i in range(5):
    my_list2.insert(0, i + 1)
    
print(my_list2)

print("______________________________")

#terceira lista
my_list3 = [10,1,8,3,5]

total = 0

for i in range(len(my_list3)):
    total += my_list3[i]
   
print(total)

total = 0

for i in my_list3:
    total += i

print(total)
print("______________________________")
#reordenando a lista
# my_list3[0], my_list3[4] = my_list3[4], my_list3[0]
# my_list3[1], my_list3[3] = my_list3[3], my_list3[1]

print(my_list3)

#reordenando sem saber o tamanho da lista
tamanhoLista = len(my_list3)

for i in range(tamanhoLista // 2):
    my_list3[i], my_list3[tamanhoLista - i - 1] = my_list3[tamanhoLista - i - 1], my_list3[i]

print(my_list3)




time.sleep(5)