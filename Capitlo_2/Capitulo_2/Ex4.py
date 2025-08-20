distancia = int(input("Digite a quilometragem: "))

if distancia <= 200:
    valor = distancia * 0.5
    print(f"Valor da passagem: R${valor}")
else:
    valor = distancia * 0.45
    print(f"Valor da passagem: R${valor}")
