while True:
    sexo = input("Digite seu sexo (M ou F): ").upper()

    if sexo == "M":
        print("homem.")
        break
    elif sexo == "F":
        print("mulher.")
        break
    else:
        print("Entrada inválida. Por favor, digite M ou F.")
