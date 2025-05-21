#Exercício 36 – Aprovando Empréstimo
#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário
# ou então o empréstimo será negado.
casa = float(input("Qual o valor da casa?"))
salario = float(input("Qual o salário do comprador?"))
tempo_prestacao = int(input("Em quanto tempo (meses) quitará a casa?"))
prestacao = casa / tempo_prestacao
limite_prestacao = salario * 0.3
if prestacao > limite_prestacao:
    print ("Infelizmente não poderemos fazer o empréstimo para o senhor pois sua prestação ficará R${:.2f},\n"
           "acima dos 30% do salário permitido pelo banco. \n\033[1;31mEMPRÉSTIMO NEGADO\033[m!".format(prestacao))
else:
    print ("Bem vindo ao sonho da casa nova! Sua prestação mensal será de R${:.2f}. \n\033[1;32mEMPRÉSTIMO APROVADO!\033[m".format(prestacao))