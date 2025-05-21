#Exercício 41 – Classificando Atletas
#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
# atleta e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER
from datetime import date
atual = date.today().year
nasc = int(input("Ano de nascimento:"))
idade = atual - nasc
print("Sua idade é {} anos.".format(idade))
if idade <= 9:
    print("Sua categoria é MIRIM.")
elif idade <= 14 and idade > 9:
    print("Sua categoria é INFANTIL.")
elif idade > 14 and idade <= 19:
    print("Sua categoria é JÚNIOR.")
elif idade > 19 and idade <= 25:
    print("Sua categoria é SÊNIOR.")
else:
    print("Sua categoria é MASTER.")