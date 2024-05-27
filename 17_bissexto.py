import time

#Recebe o ano
year = int(input("Digite o ano: "))
#Checa se o ano é parte do calendário gregoriano
if year < 1582:
    print("O ano digitado não está dentro do período do calendário gregoriano")
else:
    #Faz os cálculos para descobrir se o ano é ou não bissexto 
    if year % 4 != 0:
        estado = "é comum"
    elif year % 100 != 0:
        estado = "é bissexto"
    elif year % 400 != 0:
        estado = "é comum"
    else:
        estado = "é bissexto"
    #Informa o resultado ao usuário
    print("O ano digitado", estado)
    time.sleep(2)