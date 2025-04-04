#Programa Temperaturas Desafio

#Entrada de Dados

temperaturas = []
n = 0
resp = "S"

print("================== TEMPERATURAS - DESAFIO 3 SENAC ==================")

#Processamento de Dados

while resp == "S" or resp == "s":
    n += 1
    temperaturas.append(float(input(f"\nInforme a {n}ª temperatura: ")))
    resp = input("Deseja continuar? (S/N) ")

media = sum(temperaturas) / len(temperaturas)

#Saída de Dados

print(f"\nAs temperaturas foram: {temperaturas}")
print(f"Dentre elas, a menor foi de {min(temperaturas)}°C e a maior foi de {max(temperaturas)}°C.")
print(f"E a média das temperaturas foi de aproximadamente {media:.1f}°C.")
print("\n====================================================================")
