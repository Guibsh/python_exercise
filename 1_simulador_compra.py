#Exercício 44 – Gerenciador de Pagamentos
#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço normal
#– 3x ou mais no cartão: 20% de juros
print("{:=^40}".format(" LOJAS BRITES "))
valor_produto = float(input("Qual o valor do produto? R$"))
forma_pg = int(input("[1] à vista no dinheiro ou cheque: 10% desconto.\n"
                 "[2] à vista no cartão: 5% de desconto.\n"
                 "[3] em até 2x no cartão: preço normal.\n"
                 "[4] 3x ou mais no cartão: 20% de juros.\n"
                 "Qual a forma de pagamento?"))
if forma_pg == 1:
    desc10 = valor_produto * 0.1
    valor_final = valor_produto - desc10
    print ("O valor do produto é R${:.2f}, mas com o desconto de R${:.2f}, ficará por R${:.2f}.".format(valor_produto, desc10, valor_final))
elif forma_pg == 2:
    desc5 = valor_produto * 0.05
    valor_final = valor_produto - desc5
    print ("O valor do produto é R${:.2f}, mas com o desconto de R${:.2f}, ficará por R${:.2f}.".format(valor_produto, desc5, valor_final))
elif forma_pg == 3:
    valor_parcelado = valor_produto / 2
    print ("O valor do produto parcelado em 2x no cartão ficará por R${:.2f} cada parcela, sem desconto e sem juros, totalizando R${:.2f}.".format(valor_parcelado, valor_produto))
elif forma_pg == 4:
    juro20 = valor_produto * 0.2
    valor_final = valor_produto + juro20
    total_parcela = int(input("Você pretende fazer em quantas parcelas?"))
    parcela = valor_final / total_parcela
    print ("O valor do produto de R${:.2f} parcelado em {}x no cartão ficará com um acréscimo de R${:.2f}\n"
           "em virtude dos 20% de juros. No total o produto ficará por R${:.2f} com cada parcela de R${:.2f}."
           .format(valor_produto, total_parcela, juro20, valor_final, parcela))
else:
    print ("\033[1;31mOPÇÃO INVÁLIDA de pagamento. Tente novamente.\033[m")
