#Exercício 32 – Ano Bissexto
#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano = int(input("Digite o ano:"))
if ano % 4 == 0:
    print ("Este ano É bissexto!")
else:
    print ("Este ano NÃO é bissexto.")

#Método Guanabara
ano = int(input("Que ano quer analisar?"))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print ("O ano {} é BISSEXTO.".format(ano))
else:
    print ("O ano {} NÃO é BISSEXTO.".format(ano))