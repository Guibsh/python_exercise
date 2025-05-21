# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
co = float(input("Digite o cateto oposto:"))
ca = float(input("Digite o cateto adjacente:"))
hi = (co ** 2 + ca ** 2) ** 0.5
print ("O valor da hipotenusa é {:.2f}.".format(hi))
seno = co / hi
coss = ca / hi
tang = co / ca
print ("O seno é {:.2f}, o cosseno {:.2f} e a tangente {:.2f}.".format(seno,coss,tang))
# recriando e melhorando o código para responder corretamente a questão pela ângulo.
import math
ang = float(input("Digite o ângulo:"))
seno = math.sin(math.radians(ang))
print ("O ângulo de {} tem o SENO de {:.2f}.".format(ang, seno))
coss = math.cos(math.radians(ang))
print ("O ângulo de {} tem o COSSENO de {:.2f}.".format(ang, coss))
tang = math.tan(math.radians(ang))
print ("O ângulo de {} tem a TANGENTE de {:.2f}.".format(ang,tang))
# outra alternativa agora importante parte da biblioteca
from math import radians, sin, cos, tan
ang = float(input("Digite o ângulo que deseja:"))
seno = sin(radians(ang))
coss = cos(radians(ang))
tan = tan(radians(ang))
print ("O ângulo de {} tem o SENO {:.2f} o COSSENO {:.2f} e a TANGENTE de {:.2f}.".format(ang,seno,coss,tan))