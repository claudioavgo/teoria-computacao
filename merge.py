import random
import time

def merge_sort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]

        # Recursão nas duas metades
        merge_sort(esquerda)
        merge_sort(direita)

        # Combinação das metades
        i = j = k = 0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1

        # Elementos restantes
        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1
        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1

def kth_smallest_merge_sort(lista, k):
    merge_sort(lista)
    return lista[k - 1]

# Tamanhos das listas para testar
tamanhos = [10000, 20000, 30000, 40000, 50000]

# Número de repetições para cada tamanho
repeticoes = 5

for n in tamanhos:
    tempos = []
    ks = []
    for _ in range(repeticoes):
        # Gerar lista aleatória de tamanho n
        lista_teste = [random.randint(1, 1000000) for _ in range(n)]
        k = random.randint(1, n)  # Escolher k aleatório válido
        ks.append(k)
        
        # Medir tempo de execução
        inicio = time.time()
        resultado = kth_smallest_merge_sort(lista_teste, k)
        fim = time.time()
        
        tempos.append(fim - inicio)
    
    tempo_medio = sum(tempos) / len(tempos)
    tempo_maximo = max(tempos)
    
    print(f"Tamanho da lista: {n}")
    print(f"Valores de k testados: {ks}")
    print(f"Tempo médio: {tempo_medio:.6f} segundos")
    print(f"Tempo máximo: {tempo_maximo:.6f} segundos")
    print("-----------------------------")