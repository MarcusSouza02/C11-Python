numero = int(input("Digite um número entre 1000 e 9999: "))

if 1000 <= numero <= 9999:
    unidade = numero % 10
    dezena = (numero // 10) % 10
    centena = (numero // 100) % 10
    milhar = numero // 1000

    print("Milhar:", milhar)
    print("Centena:", centena)
    print("Dezena:", dezena)
    print("Unidade:", unidade)
else:
    print("Número fora do intervalo!")
