from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.GrafoMatrizIncidencia import GrafoMatrizIncidencia
import time
import sys

if __name__ == "__main__":
    sys.setrecursionlimit(1000000)
    # Criação do grafo euleriano com 50 vértices
    grafo = GrafoMatrizIncidencia(True).criar_grafo_euleriano(100)

    # Medindo o tempo de execução do método Fleury com Tarjan
    start_time = time.time()
    resultado_tarjan = grafo.fleury_tarjan()
    tempo_tarjan = time.time() - start_time

    # Medindo o tempo de execução do método Fleury com abordagem Naive
    start_time = time.time()
    resultado_naive = grafo.fleury_naive()
    tempo_naive = time.time() - start_time

    # Imprimindo os resultados e comparando os tempos
    # print(f"Resultado do Fleury com Tarjan: {resultado_tarjan}")
    print(f"Tempo de execução do Fleury com Tarjan: {tempo_tarjan:.6f} segundos")

    # print(f"Resultado do Fleury com Naive: {resultado_naive}")
    print(f"Tempo de execução do Fleury com Naive: {tempo_naive:.6f} segundos")


