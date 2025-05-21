# Exercício 26 – Primeira e última ocorrência de uma string
# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
f = str(input("Digite uma frase:")).upper()
tem_a = "A" in f
if tem_a:
    print ("Tem letra 'A' aparece {} vezes na frase.".format(f.count("A")))
else:
    print ("Não tem a letra 'A' nesta frase.")
quantos_a = f.count ("A")
print ("A letra 'A' se repete {} vezes".format(quantos_a))
primeira_posicao = f.find("A")
ultima_posicao = f.rfind("A")
print ("A primeira vez que aparece a letra 'A' é {} e a última é {}.".format(primeira_posicao,ultima_posicao))

# Método Guanabara
frase = str(input("Digite uma frase:")).upper().strip()
print ("A letra A aparece {} vezes na frase.".format(frase.count('A')))
print ("A primeira letra A apareceu na posição {}.".format(frase.find("A")+1))
print ("A última letra A apareceu na posição {}.".format(frase.rfind("A")+1))