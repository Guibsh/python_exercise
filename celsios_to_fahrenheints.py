# Escreva um programa que converta uma temperatura digitando em graus
grauscelsius = float(input("Qual a temperatura em graus Celsiu?"))
f = grauscelsius * 9/5 + 32
print ("A temperatura {}ºC, fica {}ºF (fahrenheints) quando convertida.".format(grauscelsius,f))
