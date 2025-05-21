# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
# triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
catetoopo = float(input("Digite o valor do cateto oposto:"))
catetoadj = float(input("Digite o valor do cateto adjacente:"))
hipotenusa = (catetoopo ** 2 + catetoadj ** 2) ** 0.5
print ("Aplicando o teorema de pitágora no cateto oposto {} e no cateto adjacente {} "
       "me deixa como resultado a hipotenusa {:.2f}".format(catetoopo,catetoadj,hipotenusa))
# opção com a biblioteca inteira
import math
catetoopo = float(input("Digite o valor do cateto oposto:"))
catetoadj = float(input("Digite o valor do cateto adjacente:"))
hipotenusa = math.hypot(catetoopo,catetoadj)
print ("Hipotenusa é igual a", hipotenusa)
# opção apenas com a parte que interessa da biblioteca
from math import hypot
co = float(input("Comprimento do cateto oposto:"))
ca = float(input("Comprimento do cateto adjacente:"))
hi = hypot(co,ca)
print ("A hipotenusa vai medir {:.2f}".format(hi))