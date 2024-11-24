from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.Aresta import Aresta
from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.Grafo import Grafo
import time
import sys

from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.Vertice import Vertice


def criar_grafo_grande(quantidade_vertices):
    grafo = Grafo("grafo_grande", False)

    vertices = []
    for i in range(quantidade_vertices):
        vertice = Vertice(peso_vertice=str(i), rotulo=f"V{i}")
        vertices.append(vertice)
        grafo.adicionarVertice(vertice)

    for i in range(quantidade_vertices - 1):
        grafo.adicionarAresta(Aresta(vertices[i], vertices[i + 1], rotulo=f"e{i}", peso=1))

    grafo.adicionarAresta(
        Aresta(vertices[quantidade_vertices - 1], vertices[0], rotulo=f"e{quantidade_vertices - 1}", peso=1))

    return grafo

if __name__ == "__main__":
    sys.setrecursionlimit(100000000)
    quantidade_vertices = 10000

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







