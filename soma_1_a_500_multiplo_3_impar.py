#Exercício 48 – Soma ímpares múltiplos de três
#Faça um programa que calcule a soma entre todos os números que são múltiplos
# de três e que se encontram no intervalo de 1 até 500.
soma = 0
for n in range (1, 501): #loop do numero 1 a 500
    if n % 3 == 0 and n % 2 != 0: #se o numero de 1 a 500 for dividido por "3" e restar "0", e por último se ele for ímpar.
                                  #todo número dividido por 2 que restar diferente de "0" é ímpar.
        soma = soma + n #soma que era "0" lá em cima, agora vai somar 1 por 1 os multiplos que passaram na estrutura de condição "if n % 3 == 0:" repetindo até o loop de 1 a 500 acabar.
        print(soma) #printa a soma de todos os "n" (multiplos de "3") de 1 a 500.
#print (soma) USAR ESTE E TIRAR O DE DENTRO DO "IF" PARA VER SÓ A SOMA FINAL!!!
# abro o cofrinho na variável soma = 0, depois eu uso o loop de 1 a 500, depois "if" condicional para estabelecer que quero
#apenas os multiplos de 3 (if n % 3 == 0:), depois eu dentro do "if" busco a variável soma e começo a somar 1 por 1 dos multiplos
#de 3 (soma = soma + n), por fim dou um print na soma dos multiplos de 3.

#RESUMO: “Eu comecei com uma caixinha vazia chamada soma.
#Depois, fui olhando os números de 1 até 500.
#Se o número podia ser dividido por 3, eu colocava ele na caixinha.
#No final, eu olhei dentro da caixinha pra ver o total acumulado.”