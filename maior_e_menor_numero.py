#Exercício 33 – Maior e menor valores
#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
primeiro_n = int(input("Digite o primeiro número:"))
segundo_n = int(input("Agora digite o segundo número:"))
terceiro_n = int(input("Por fim, digite o terceiro número:"))
if primeiro_n > segundo_n and primeiro_n > terceiro_n:
    print ("O maior número dentre os três é o {}.".format(primeiro_n))
if segundo_n > primeiro_n and segundo_n > terceiro_n:
    print ("O maior número dentre os três é o {}.".format(segundo_n))
if terceiro_n > primeiro_n and terceiro_n > segundo_n:
    print ("O maior número é o {}.".format(terceiro_n))

    #Método Guanabara
a = int(input("Primeiro valor:"))
b = int(input("Segundo valor:"))
c = int(input("Terceiro valor:"))
#Verificando quem é o menor.
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
    # Verificando quem é o maior.
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print ("O menor valor digitado foi {} e o maior digitado foi o {}.".format(menor,maior))