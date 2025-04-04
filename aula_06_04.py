#Programa Números Desafio

#Entrada de Dados

num = []
print("================== LISTA DE NÚMEROS - DESAFIO 4 SENAC ==================")

for i in range(10):
    num.append(int(input(f"\nDigite o {i+1}º número: ")))

#Processamento de Dados

media = sum(num) / len(num)

#Saída de Dados

print(f"\nA lista completa de números é: {num}")
print(f"O maior número é {max(num)} e o menor é {min(num)}.")
print(f"A soma de todos os números é igual a {sum(num)} e a média desses números é  igual a {media}.")
print("\n========================================================================")