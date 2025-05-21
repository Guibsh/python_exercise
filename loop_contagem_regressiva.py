#Exercício 46 – Contagem regressiva
#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
for c in range (10,-1, -1):
    print(c)
    sleep(1)
print("\033[1;33mBOOM!!!\033[m")

#Imagine que o range() é como um trem nos trilhos, e você diz para ele:
#Onde ele começa (ex: 10),
#Onde ele para (ex: -1),
#E de quantos em quantos ele anda (ex: -1 pra trás, ou +1 pra frente).
#PRIMEIRO O NUMERO (10), DEPOIS PARA ONDE ELE ESTÁ INDO (-1 para ele ir até o "0") e depois para ele contar
#pulando 2 casas para para trás (-2) e para frente (2).