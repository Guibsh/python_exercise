#Exercício 45 – GAME: Pedra Papel e Tesoura
#Crie um programa que faça o computador jogar Jokenpô com você.
import random
from time import sleep
opcoes = [0, 1, 2]
pc_escolhe = random.choice (opcoes)
print ("\033[1;35m-=\033[m" * 18)
print ("JOGO JOKENPÔ - PEDRA, PAPEL, TESOURA")
print ("\033[1;35m-=\033[m" * 18)
print ("Suas opções:\n"
       "[0] PEDRA\n"
       "[1] PAPEL\n"
       "[2] TESOURA")
vc_escolhe = int(input("Qual é sua jogada?"))
sleep(1)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ!!!")
sleep(1)
if pc_escolhe == 0 and vc_escolhe == 0:
    print("Deu empate meu querido.")
elif pc_escolhe == 0 and vc_escolhe == 1:
    print("\033[1;34mParabéns, você ganhou, juninho.\033[m")
elif pc_escolhe == 0 and vc_escolhe == 2:
    print("\033[1;31mVish, você perdeu papai.\033[m")
elif pc_escolhe == 1 and vc_escolhe == 0:
    print("\033[1;31mShiiii... você perdeu papai.\033[m")
elif pc_escolhe == 1 and vc_escolhe == 1:
    print("Deu empate meu bom.")
elif pc_escolhe == 1 and vc_escolhe == 2:
    print("\033[1;34mDeu bão, você ganhou.\033[m")
elif pc_escolhe == 2 and vc_escolhe == 0:
    print("\033[1;34mVocê ganhou, meu jovem.\033[m")
elif pc_escolhe == 2 and vc_escolhe == 1:
    print("\033[1;31mShiii... deu ruim papai. Perdeu playboy.\033[m")
elif pc_escolhe == 2 and vc_escolhe == 2:
    print("Empate. Vamos em melhor de 3?")
opcoes = {0: "PEDRA", 1: "PAPEL", 2:"TESOURA"}
print ("Resultado: PC = {} x Você = {}.".format(opcoes[pc_escolhe], opcoes [vc_escolhe]))
