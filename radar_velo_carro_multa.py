#Exercício 29 – Radar eletrônico
# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
v = int(input("Com qual velocidade o carro passou no radar?"))
from time import sleep
print ("Processando velocidade...")
sleep(3)
if v <= 80:
    print ("Tenha um bom dia! Dirija com segurança!")
else:
    velo_acima = v - 80
    valor_multa = velo_acima * 7
    print("Você foi multado por passar acima de 80Km/h.\n"
          "Registramos {}Km/h e sua multa será de R${:.2f}, por ter passado {}Km/h do limite.".format(v,valor_multa,velo_acima))

# Método Guanabara

velocidade = float(input("Qual é a velocidade atual do carro?"))
if velocidade > 80:
    print ("MULTADO! Você excedeu o limite permitido que é de 80Kmh/")
    multa = (velocidade-80) * 7
    print ("Você deve pagar uma multa de R${:.2f}!".format(multa))
print ("Tenha um bom dia! Direja com segurança.")