#Exercício 34 – Aumentos múltiplos
#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input("Qual o salário que receberá o aumento?"))
if salario > 1250:
    menor_aumento = salario * 0.1
    novo_salario = salario + menor_aumento
    print ("Seu salário de R${:.2f} recebeu um aumento de R${:.2f} e agora passará a ser R${:.2f}.".format(salario, menor_aumento, novo_salario))
if salario <= 1250:
    maior_aumento = salario * 0.15
    novo_salario = salario + maior_aumento
    print ("Seu salário de R$ {:.2f} recebeu aumento de R${:.2f} e agora passará a ser R${:.2f}.".format(salario, maior_aumento, novo_salario))

#Método Guanabara
salario = float(input("Qual é o salário do funcionário? R$"))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print ("Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.".format(salario, novo))