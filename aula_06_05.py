#Programa Pesquisa Desafio

#Entrada de Dados

sexo = []
c_olhos = []
c_cabelos = []
idade = []
m_adultas = 0
v_loiros = 0

print("================== PESQUISA - DESAFIO 5 SENAC ==================")

n = int(input("\nQuantas pessoas participarão da pesquisa? "))

#Processamento de Dados

for i in range(n):
    sexo.append(input("\nQual é seu sexo? Responda M para Masculino e F para Feminino. "))
    c_olhos.append(input("Qual a cor dos seus olhos? "))
    c_cabelos.append(input("Qual a cor dos seus cabelos? "))
    idade.append(int(input("Qual é a sua idade? ")))
    if idade[i] >= 18 and idade[i] < 35:
        if sexo[i] == "F":
            m_adultas += 1

    if c_olhos[i] == "Verde":
        if c_cabelos[i] == "Loiro":
            v_loiros += 1

#Saída de Dados

print("\nAqui estão os resultados da pesquisa:")
print(f"\nLista de sexo: {sexo}")
print(f"Lista de cores dos olhos: {c_olhos}")
print(f"Lista de cores de cabelo: {c_cabelos}")
print(f"Lista de idades: {idade}")
print(f"\nA maior idade entre todas da lista foi {max(idade)}.")
print(f"A quantidade de mulheres entre os 18 a 35 anos foi {m_adultas}.")
print(f"A quantidade de pessoas com olhos verdes e cabelos loiros foi {v_loiros}.")
print("\n================================================================")