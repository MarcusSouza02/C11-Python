idades = []
mulheres_menos_20 = 0

while True:
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").strip().upper()
    idades.append(idade)
    if sexo == "F" and idade < 20:
        mulheres_menos_20 += 1
    if input("Adicionar mais? (S/N): ").strip().upper() == "N":
        break

print(f"Média de idade: {sum(idades)/len(idades):.2f}")
print(f"Mulheres com menos de 20 anos: {mulheres_menos_20}")
