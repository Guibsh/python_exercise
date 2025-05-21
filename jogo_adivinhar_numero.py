# Exercício 28 – Jogo da Adivinhação v.1.0
# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
print ("--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-\n"
       "Vou pensar em um número entre 0 e 5. Tente adivinhar...\n"
       "--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-")
import random
lista = [0,1,2,3,4,5]
numero_pensado = random.choice(lista)
numero_escolhido = int(input ("Em que número eu pensei?"))
if numero_pensado == numero_escolhido:
    print (f"PARABÉNS! Pensei no número {numero_pensado}. Você acertou =D")
else:
    print (f"Pensei no número {numero_pensado}. Essa foi por pouco. Tente novamente ^^")