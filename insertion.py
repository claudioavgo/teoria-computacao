import random
import time

def insertion_sort(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key

def kth_smallest_sort(lista, k):
    insertion_sort(lista)
    return lista[k - 1]

# Tamanhos das listas para testar
tamanhos = [1000, 2000, 3000, 4000, 5000]

# Número de repetições para cada tamanho
repeticoes = 5

for n in tamanhos:
    tempos = []
    for _ in range(repeticoes):
        # Gerar lista aleatória de tamanho n
        lista_teste = [random.randint(1, 1000000) for _ in range(n)]
        k = random.randint(1, n)  # Escolher k aleatório válido

        # Medir tempo de execução
        inicio = time.time()
        kth_smallest_sort(lista_teste, k)
        fim = time.time()

        tempos.append(fim - inicio)

    tempo_medio = sum(tempos) / len(tempos)
    tempo_maximo = max(tempos)

    print(f"Tamanho da lista: {n}")
    print(f"Tempo médio: {tempo_medio:.4f} segundos")
    print(f"Tempo máximo: {tempo_maximo:.4f} segundos")
    print("-----------------------------")