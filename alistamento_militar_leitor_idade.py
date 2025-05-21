#Exercício 39 – Alistamento Militar
#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou
# do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
nasc = int(input("Seu ano de nascimento:"))
idade = 2025 - nasc
anos_velho = idade - 18
anos_novo = 18 - idade
if idade == 18:
    print ("Este é o seu ano de alistamento no EB.")
elif idade > 18:
    print ("Você possui {} anos e passou {} anos de se alistar no EB.".format(idade, anos_velho))
else:
    print ("Faltam {} anos para você se alistar no EB, pois ainda possui {} anos de idade.".format(anos_novo, idade))

#Método Guanabara

from datetime import date
atual = date.today().year
nasc = int(input("Ano de nascimento:"))
idade = atual - nasc
print("Quem nasceu em {} tem {} anos em {}.".format(nasc, idade, atual))
if idade == 18:
    print("Você tem que se alistar IMEDIATAMENTE!")
elif idade < 18:
    saldo = 18 - idade
    print("Ainda faltam {} anos para o alistamento.".format(saldo))
    ano = atual + saldo
    print("Seu alistamente será em {}.".format(ano))
elif idade > 15:
    saldo = idade - 18
    print("Você já deveria ter se alistado há {} anos.".format(saldo))
    ano = atual - saldo
    print("Seu alistamento foi em {}.".format(ano))