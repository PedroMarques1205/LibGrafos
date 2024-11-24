from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.Aresta import Aresta
import sys

from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.Grafo import Grafo
from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.Vertice import Vertice

if __name__ == "__main__":
    vA = Vertice(peso_vertice='1', rotulo='A')
    vB = Vertice(peso_vertice='2', rotulo='B')
    vC = Vertice(peso_vertice='3', rotulo='C')
    vD = Vertice(peso_vertice='4', rotulo='D')

    grafo = Grafo(isDirecionado=True, id='aaaaa')

    grafo.adicionarVertice(vA)
    grafo.adicionarVertice(vB)
    grafo.adicionarVertice(vC)
    grafo.adicionarVertice(vD)

    e1 = Aresta(vA, vB, 'e1', 1)

    grafo.adicionarAresta(e1)

    grafo.printar_lista_adjacencia()
    grafo.printar_matriz_adjacencia()
    grafo.printar_matriz_indicencia()

    grafo.criar_arquivo_grafo_graphml()














    print(f"Construindo um grafo com {quantidade_vertices} vértices...")
    start_time = time.time()
    grafo_grande = criar_grafo_grande(quantidade_vertices)
    print(f"Grafo construído em {time.time() - start_time:.5f} segundos.")

    print("Executando Fleury com Tarjan...")
    start_time = time.time()
    resultado_tarjan = grafo_grande.fleury_tarjan()
    print(f"Algoritmo Fleury com Tarjan executado em {time.time() - start_time:.5f} segundos.")

    print("Executando Fleury com Naive...")
    start_time = time.time()
    resultado_naive = grafo_grande.fleury_naive()
    print(f"Algoritmo Fleury com Naive executado em {time.time() - start_time:.5f} segundos.")

    print(grafo_grande.printar_lista_adjacencia())