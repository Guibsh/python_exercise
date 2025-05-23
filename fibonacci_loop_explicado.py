#Exercício 5 (Nível Fácil): Escreva um programa que imprima a sequência de Fibonacci
# até um determinado número de termos informado pelo usuário.
#A sequência de Fibonacci é uma série de números em que cada número é a soma dos dois
# anteriores, começando com 0 e 1. Por exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, etc.
n_termos = int(input("Escreva um número de termos para solucionarmos a sequência de Fibonacci: "))
a = 0
b = 1
for x in range(n_termos):
    print(a)
    finonacci = a + b
    a = b
    b = finonacci
# Gui, pense em um sistema de roletas. Toda vez que "n_termos" começa o laço (loop), é exercido de cima para baixo a ordem
# lógica de execução, ou seja por ordem de linha de código cada variável assume um novo papel e tem um valor renovado para
# a próxima rodada de loop, alimentando assim a sequência de Fibonacci renovando os valores a cada rodada e estocando e
# executando as operações em loop novamente estocando novos valores até o "n_termos" se cumprir (número de vezes que o loop
# irá correr, de acordo com o input do usuário).