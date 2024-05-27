import time
#Definindo o número secreto
secret_number = 777
#Escrevendo a mensagem inicial
print(
"""
+===================================+
| Bem vindo ao meu jogo, #&$!@*!    |
| Insira um número inteiro          |
| e adivinhar o número que tenho    |
| escolhidos para você.             |
| Então, qual é o número secreto?   |
+===================================+
""")
#Recebendo o valor do número escolhido
num = int(input("Digite logo o seu número: "))
#Enquanto o número escolhido não ser o número secreto
while num != secret_number:
    #Informa o jogador e recebe outro valor
    print("Ha ha! Você está preso no meu loop!")
    num = int(input("Digite logo o seu número: "))
#Se ele adivinhar, parabenize ele
print("Muito bem! Você está livre agora.")

time.sleep(2)