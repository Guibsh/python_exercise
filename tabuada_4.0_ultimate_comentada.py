#Exercício 4 (Nível Fácil): Escreva um programa que imprima a tabuada de 1 a 10 usando um loop for.
'''for x in range (1,11):
    resultado1 = 1 * x
    print("{} x {:2} = {}".format(1, x, resultado1))'''
for tabuada in range (1,11): #loop de cada tabuada
    for numero in range (1,11): #loop resultados das tabuadas
        produto = tabuada * numero
        print("{} x {:2} = {}".format(tabuada, numero, produto))
        #print(f"{tabuada} x {numero} = {produto:>10}", end="")
    print()

'''é como se o primeiro laço fosse a mãe... a mãe fala mais calma com 1 passo de cada vez... 
o filho mais afoito já fala tudo (10x) de uma vez só para cada 1 palavra da mãe são 10 do filho. 
aí o filho faz uma pausa para a mãe conseguir falar de novo'''

#ou

'''é como se eu desse 1 tiro no primeiro loop e metralhasse 10 no segundo loop e depois vem o segundo tiro do 
primeiro loop e depois metralha mais 10 no segundo... consegui. aí pra extrair o produto da interação dos laços 
eu fiz aquela formula. Chamo a formula de operação ou botei uma variavel "produto = tabuada * numero"?(pergunto a llm)'''

'''for numero in range(1, 11):
    for tabuada in range(1, 11):
        produto = tabuada * numero
        print(f"{tabuada} x {numero} = {produto:>2}", end="\t")  
    print()'''
#ESTE ÚLTIMO CÓDIGO DEIXA PERFEITAMENTE ORGANIZADA A TABUADA POR COLUNAS.