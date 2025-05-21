# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
n = int(input("Informe um número entre 0 e 9999:"))
milhar = n // 1000
centena = (n % 1000) // 100
dezena = (n % 100) // 10
unidade = n % 10
print (f"Milhar: {milhar}.")
print (f"Centena: {centena}.")
print (f"Dezena: {dezena}.")
print (f"unidade: {unidade}.")

# Segunda forma de resolver transformando número em string, mas só funciona se digitar 4 algarismos se não buga.
#num = int(input("Informe um número:"))
#n = str(num)
#print ("Analisando o número {}.".format(num))
#print ("Unidade: {}.".format(n[3]))
#print ("Dezena: {}.".format(n[2]))
#print ("Centena: {}.".format(n[1]))
#print ("Milhar: {}.".format(n[0]))

# Agora a forma do Gustavo Guanabara.
num = int(input("Informe um número:"))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print ("Analisando o número {}.".format(num))
print ("Unidade: {}.".format(u))
print ("Dezena: {}.".format(d))
print ("Centena: {}.".format(c))
print ("Milhar: {}.".format(m))