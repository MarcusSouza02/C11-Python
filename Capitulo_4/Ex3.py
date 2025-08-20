import numpy as np
import random

matriz = np.zeros((2, 2))

linha = random.randint(0, 1)
coluna = random.randint(0, 1)
matriz[linha, coluna] = 1

tentativas = 0
achou = False
posicoes_escolhidas = []

while tentativas < 3 and not achou:
    print("\nDigite a posição que deseja jogar (linha e coluna de 0 a 1)")
    l = int(input("Linha (0 ou 1): "))
    c = int(input("Coluna (0 ou 1): "))

    if (l, c) in posicoes_escolhidas:
        print("Você já tentou essa posição, escolha outra!")
        continue

    posicoes_escolhidas.append((l, c))
    tentativas += 1

    if matriz[l, c] == 1:
        achou = True
        print("\nGame Over :( Try Again!")
        break

if not achou:
    print("\nCongratulations! You beat the game! :)")
