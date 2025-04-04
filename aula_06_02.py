#Programa Tinta Desafio

import math

#Entrada de Dados

area_lata = 18 * 3
valor_lata = 130

print("================== LOJA DE TINTAS - DESAFIO 2 SENAC ==================")
area = int(input("Qual é o tamanho em metros quadrados da área a ser pintada? "))

#Processamento de Dados

qntd_latas = math.ceil(area / area_lata)
valor_total = qntd_latas * valor_lata

#Saída de Dados

print(f"\nA quantidade de latas necessárias para {area} m² é de {qntd_latas:.0f} latas.")
print(f"O valor total a se pagar em cima da quantidade é R${valor_total:.2f}.")
print("\n======================================================================")