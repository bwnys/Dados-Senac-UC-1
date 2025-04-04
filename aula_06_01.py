#Programa Salário Desafio

#Entrada de Dados

print("================== CÁLCULO SALARIAL - DESAFIO 1 SENAC ==================")

nome = input("\nDigite o nome do funcionário: ")
sh = float(input(f"Quanto vale o salário-hora do funcionário {nome}? "))
h = float(input(f"E por quantas horas {nome} trabalhou esse mês? "))

#Processamento de Dados

sb = sh * h
irrf = sb * (11/100)
inss = sb * (8/100)
sind = sb * (5/100)
sl = sb - (irrf+inss+sind)

#Saída de Dados

print(f"\nAqui estão os dados do contracheque do funcionário {nome}:")
print(f"\nSalário Bruto: R${sb:.2f}.")
print(f"Desconto de 11% do IRRF: R${irrf:.2f}.")
print(f"Desconto de 8% do INSS: R${inss:.2f}.")
print(f"Desconto de 5% do Sindicato: R${sind:.2f}.")
print(f"\nPor fim, o salário líquido a pagar é de R${sl:.2f}.")
print("\n=========================================================================")