#Exercício 40 – Aquele clássico da Média
#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO
n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite a segunda nota:"))
media = (n1 + n2) / 2
print("Sua média foi {:.1f}.".format(media))
if media >= 7.0:
    print ("\033[1;34mPARABÉNS!\033[m Você foi \033[1;34mAPROVADO!\033[m")
elif media >= 5.0 and media <= 6.9:
    print ("\033[1;33mCUIDADO!\033[m Você está de \033[1;33mRECUPERAÇÃO!\033[m")
else:
    print ("Você foi \033[1;31mREPROVADO!\033[m")