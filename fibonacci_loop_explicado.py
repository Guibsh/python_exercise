'''25/05/2025'''
#código melhorado após REFATORAÇÃO. Obs: eliminando más práticas de programação (fedores).
FIRST_MEMBER = 0
SECOND_MEMBER = 1
n_termos = int(input("Escreva um número de termos para solucionarmos a sequência de Fibonacci: "))
actual = FIRST_MEMBER
next = SECOND_MEMBER
for x in range(n_termos):
    print(actual)
    finonacci = actual + next
    actual = next
    next = finonacci
