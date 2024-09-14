import random
import matplotlib.pyplot as plt

# Grafo de caminhos para realizar o caixeiro viajante
matriz_caixeiro = [[0, 124, 182, 4, 338, 306, 16, 148, 329, 379],
                   [124, 0, 237, 109, 448, 269, 309, 330, 249, 184],
                   [182, 237, 0, 239, 377, 128, 13, 151, 141, 130],
                   [4, 109, 239, 0, 369, 303, 460, 331, 42, 433],
                   [338, 448, 377, 369, 0, 202, 368, 122, 408, 141],
                   [306, 269, 128, 303, 202, 0, 438, 381, 129, 454],
                   [16, 309, 13, 460, 368, 438, 0, 458, 68, 69],
                   [148, 330, 151, 331, 122, 381, 458, 0, 456, 271],
                   [329, 249, 141, 42, 408, 129, 68, 456, 0, 240],
                   [379, 184, 130, 433, 141, 454, 69, 271, 240, 0]
                   ]

matriz_caixeiro_20 = [
[0, 310,  43, 432, 218, 486, 326, 442, 412, 343, 139, 199, 157, 441, 426, 446,  68, 252, 453, 187],
[310, 0,  13, 324, 489, 500, 347,  77, 169,  72, 258, 144, 414, 116, 121, 388, 357, 409, 474, 345],
[ 43,  13, 0, 113,  32, 294, 407, 162, 290, 416, 228,  71, 246, 138, 270,  69, 159, 211, 146,   3],
[432, 324, 113, 0, 434, 164, 202, 189, 156,  34, 445,  51, 301, 353, 105, 150, 427, 473,  82,  19],
[218, 489,  32, 434,  0, 247, 500,  90, 399, 383, 120, 396, 318, 307, 478, 382, 113,   1, 273,  57],
[486, 500, 294, 164, 247, 0, 473,  32, 306, 237,   8, 321, 416, 114,  10, 152, 304,   6, 367,  57],
[326, 347, 407, 202, 500, 473, 0, 465, 198, 352, 345, 302, 411, 240, 128, 265, 331, 175, 234,  89],
[442,  77, 162, 189,  90,  32, 465, 0, 389, 493, 176,   6, 422, 245, 252,  25, 308, 459,  44, 420],
[412, 169, 290, 156, 399, 306, 198, 389, 0, 268, 266, 412, 454, 374,  80, 496, 376, 232, 420, 456],
[343,  72, 416,  34, 383, 237, 352, 493, 268, 0, 329, 434, 153, 349, 492, 211, 200, 465, 453, 108],
[139, 258, 228, 445, 120,   8, 345, 176, 266, 329, 0, 107,  61, 322, 281, 462,  17, 446, 247,  34],
[199, 144,  71,  51, 396, 321, 302,   6, 412, 434, 107, 0, 191, 223, 461,  86, 161, 456, 229,  86],
[157, 414, 246, 301, 318, 416, 411, 422, 454, 153,  61, 191, 0, 489, 176, 324, 404, 495, 333, 313],
[441, 116, 138, 353, 307, 114, 240, 245, 374, 349, 322, 223, 489,  0, 176,  80, 476, 115, 169, 109],
[426, 121, 270, 105, 478,  10, 128, 252,  80, 492, 281, 461, 176, 176, 0, 119, 164, 132,  33, 395],
[446, 388,  69, 150, 382, 152, 265,  25, 496, 211, 462,  86, 324,  80, 119, 0,  30,  22, 260, 481],
[ 68, 357, 159, 427, 113, 304, 331, 308, 376, 200,  17, 161, 404, 476, 164,  30,  0, 326, 417,  96],
[252, 409, 211, 473,   1,   6, 175, 459, 232, 465, 446, 456, 495, 115, 132,  22, 326, 0, 313, 196],
[453, 474, 146,  82, 273, 367, 234,  44, 420, 453, 247, 229, 333, 169,  33, 260, 417, 313, 0, 234],
[187, 345,   3,  19,  57,  57,  89, 420, 456, 108,  34,  86, 313, 109, 395, 481,  96, 196, 234,   0]
]

# Troque o grafo aqui para realizar o caixeiro em outros caminhos
MATRIZ = matriz_caixeiro_20

N = len(MATRIZ)
SEED = 159
random.seed(SEED)


# Gerando um individuo aleatorio
def criar_individuo():
    return [random.randint(0, N - 1) for _ in range(N)]

def recortarPai(pai1, pai2, crossover=[3,4,5,6,7,8]):
    if max(crossover) >= N or min(crossover) < 0:
        raise ValueError("O valor do crossover deve ser positivo e estar entre o tamanho do array")
    if 0 not in crossover:
        crossover.append(0)
    copia1 = pai1.copy()
    copia2 = pai2.copy()

    copia1 = pai1.copy()
    copia2 = pai2.copy()

    for i in crossover:
        if copia1[i] != copia2[0]:
            copia2.remove(copia1[i])

    cont = 1
    for i in range(1, N):
        if i not in crossover:
            copia1[i] = copia2[cont]
            cont += 1


    return copia1
# cálculo do fitness
def calcular_fitness(individuo):
    fit = 0;
    for i in range(N):
        fit += MATRIZ[individuo[i]][individuo[i+1]]
    return fit


# Seleção dos melhores individuos
def selecao(populacao):
    populacao.sort(key=lambda ind: calcular_fitness(ind))
    return populacao[:len(populacao) // 2]  # Retorna a metade superior da população


# Crossover com ponto de corte aleatorio
def crossover(pai1, pai2):
    return recortarPai(pai1, pai2)


# Mutacao com uma taxa de 0.1
def mutacao(individuo, taxa_mutacao=0.1):
    if random.random() < taxa_mutacao:
        i = random.randint(1, 8)
        aux = individuo[i]
        individuo[i] = individuo[i+1]
        individuo[i+1] = aux
    return individuo


# execucao do AG
def algoritmo_genetico(tamanho_populacao=100, geracoes=1000):

    populacao = []
    for i in range(tamanho_populacao):
        atual = random.randint(0, len(MATRIZ) - 1)
        comeco = atual
        caminho = [atual]
        for j in range(len(MATRIZ) - 1):
            vou_para = random.randint(0, len(MATRIZ) - 1)
            while True:
                if vou_para not in caminho:
                    break
                vou_para = random.randint(0, len(MATRIZ) - 1)
            caminho.append(vou_para)
        caminho.append(comeco)
        populacao.append(caminho)
    historico_fitness = []

    contagemSemAlteracao = 0
    melhor_fitness = 99999999
    melhor_geracao = 0
    for geracao in range(geracoes):
        contagemSemAlteracao += 1
        melhor_individuo = min(populacao, key=lambda ind: calcular_fitness(ind))
        fitness = calcular_fitness(melhor_individuo)
        historico_fitness.append(fitness)

        if melhor_fitness > fitness:
            melhor_geracao = geracao
            melhor_fitness = fitness
            contagemSemAlteracao = 0

        if contagemSemAlteracao == 30:
            break

        nova_populacao = selecao(populacao)

        while len(nova_populacao) < tamanho_populacao:
            pai1, pai2 = random.sample(nova_populacao, 2)
            filho = crossover(pai1, pai2)
            filho = mutacao(filho)
            nova_populacao.append(filho)

        populacao = nova_populacao

    # Plotando o gráfico de fitness ao longo das gerações
    print(f"Solução encontrada na geração {melhor_geracao}: {melhor_individuo} - Com fitness de {melhor_fitness}")
    plt.plot(historico_fitness)
    plt.title('Evolução do Fitness ao Longo das Gerações')
    plt.xlabel('Geração')
    plt.ylabel('Fitness (Menor é melhor)')
    plt.show()

    return melhor_individuo

algoritmo_genetico()

