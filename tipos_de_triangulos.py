#Exercício 42 – Analisando Triângulos v2.0
#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo
#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes
reta1 = int(input("Tamanho da primeira reta:"))
reta2 = int(input("Tamanho da segunda reta:"))
reta3 = int(input("Tamanho da terceira reta:"))
if reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta3 + reta1 > reta2:
    print ("É possível formar um triângulo.")
    if reta1 == reta2 == reta3:
        print("É um triângulo EQUILÁTERO.")
    elif reta1 != reta2 != reta3 != reta1:
        print("É um triângulo ESCALENO.")
    else:
        print("É um triângulo ISÓSCELES.")
else:
    print("Vish!Não é possível montar um triângulo com essas retas.")