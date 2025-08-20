nomes = []
pesos = []

for _ in range(3):
    nomes.append(input("Nome: "))
    pesos.append(float(input("Peso: ")))

mais_pesada = max(pesos)
mais_leve = min(pesos)

print(f"Mais pesada: {nomes[pesos.index(mais_pesada)]} ({mais_pesada} kg)")
print(f"Mais leve: {nomes[pesos.index(mais_leve)]} ({mais_leve} kg)")
