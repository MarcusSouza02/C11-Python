nome = str(input("Digite seu nome: "))
media = float(input("Digite sua média: "))

dicionario = {'nome': nome, 'media': media}

if media >= 50:
    dicionario['situacao'] = 'Aprovado'  # Aprovado
else:
    dicionario['situacao'] = 'Reprovado'  # Reprovado


print(dicionario)
