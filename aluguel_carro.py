# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
# que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input("Quantos Km o carro percorreu?"))
dias = int(input("Quantos dias o carro alugado foi utilizado?"))
pgtkm = km * 0.15
pgtdias = dias * 60
print ("Percorrendo {:.2f}Km em {} dias você terá que pagar R${:.2f}.".format(km, dias,pgtkm + pgtdias))