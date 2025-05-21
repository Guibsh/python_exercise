#Exercício 49 – Tabuada v.2.0
#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
n_tabuada = int(input("Digite o número que você deseja a tabuada:"))
for n in range (1, 11):
    tabuada = n_tabuada * n
    print(n_tabuada, "x", n,"=", tabuada)
