import random

matriz_caixeiro = [[  0, 124, 182,   4, 338, 306,  16, 148, 329, 379],
                   [124,   0, 237, 109, 448, 269, 309, 330, 249, 184],
                   [182, 237,   0, 239, 377, 128,  13, 151, 141, 130],
                   [  4, 109, 239,   0, 369, 303, 460, 331,  42, 433],
                   [338, 448, 377, 369,   0, 202, 368, 122, 408, 141],
                   [306, 269, 128, 303, 202,   0, 438, 381, 129, 454],
                   [ 16, 309,  13, 460, 368, 438,   0, 458,  68,  69],
                   [148, 330, 151, 331, 122, 381, 458,   0, 456, 271],
                   [329, 249, 141,  42, 408, 129,  68, 456,   0, 240],
                   [379, 184, 130, 433, 141, 454,  69, 271, 240,   0]
               ]

for i in range(6):
    atual = random.randint(0, len(matriz_caixeiro)-1)
    comeco = atual
    fit = 0
    caminho = [atual]
    for j in range(len(matriz_caixeiro) - 1):
        vou_para = random.randint(0, len(matriz_caixeiro)-1)
        while True:
            if vou_para not in caminho:
                break
            vou_para = random.randint(0, len(matriz_caixeiro)-1)
        fit += matriz_caixeiro[atual][vou_para]
        caminho.append(vou_para)
        atual = vou_para
    fit += matriz_caixeiro[atual][comeco]
    caminho.append(comeco)

    print(caminho)
    print(fit)
