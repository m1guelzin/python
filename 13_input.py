import time
count = 0

#Recebendo os valores de horas e minutos
hr = int(input("Digite as horas de início do evento: "))
mn = int(input("Digite os minutos de início do evento: "))

#Recebe o tempo do evento em minutos
t = int(input("Digite o tempo de duração do evento (em minutos): "))

#Soma os minutos de início com a duração, se maior que 60, tira 60 e adciona 1 hora
fin = mn + t
while fin > 59:
    fin -= 60
    hr += 1

#Verifica se um dia passou
while hr > 23:
    hr -= 24
    count += 1

if count > 0:
    #Informa a hora e os minutos do fim do evento se um dia passou
    print("Hora de término do evento: ", hr, ":", fin, " de algum dia seguinte", sep = "")
else:
    #Informa a hora e os minutos do fim do evento se no mesmo dia
    print("Hora de término do evento: ", hr, ":", fin, sep = "")

time.sleep(5)