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

    vA = Vertice(peso_vertice='1', rotulo='A')
    vB = Vertice(peso_vertice='2', rotulo='B')
    vC = Vertice(peso_vertice='3', rotulo='C')
    vD = Vertice(peso_vertice='4', rotulo='D')
    vE = Vertice(peso_vertice='5', rotulo='E')
    vF = Vertice(peso_vertice='6', rotulo='F')

    grafo_maior.adicionarVertice(vA)
    grafo_maior.adicionarVertice(vB)
    grafo_maior.adicionarVertice(vC)
    grafo_maior.adicionarVertice(vD)
    grafo_maior.adicionarVertice(vE)
    grafo_maior.adicionarVertice(vF)

    grafo_maior.adicionarAresta(Aresta(vA, vB, rotulo='e1', peso=1))
    grafo_maior.adicionarAresta(Aresta(vB, vC, rotulo='e2', peso=1))
    grafo_maior.adicionarAresta(Aresta(vC, vD, rotulo='e3', peso=1))
    grafo_maior.adicionarAresta(Aresta(vD, vA, rotulo='e4', peso=1))

    grafo_maior.adicionarAresta(Aresta(vA, vE, rotulo='e5', peso=1))
    grafo_maior.adicionarAresta(Aresta(vE, vF, rotulo='e6', peso=1))
    grafo_maior.adicionarAresta(Aresta(vF, vD, rotulo='e7', peso=1))
    grafo_maior.adicionarAresta(Aresta(vD, vB, rotulo='e8', peso=1))

    print(" ")
    print('== PASSOU 1 ==')
    print(" ")

    grafo_maior.printar_matriz_adjacencia()
    grafo_maior.printar_matriz_indicencia()
    grafo_maior.printar_lista_adjacencia()

    grafo_maior.removerAresta(vA.get_rotulo(), vB.get_rotulo())

    print(" ")
    print('== PASSOU 2 - REMOVER ARESTA ==')
    print(" ")

    grafo_maior.printar_matriz_adjacencia()
    grafo_maior.printar_matriz_indicencia()
    grafo_maior.printar_lista_adjacencia()

    grafo_maior.removerVertice(vD.get_rotulo())

    print(" ")
    print('== PASSOU 3 - REMOVER VERTICES ==')
    print(" ")


    print(grafo_maior.vertices)

    grafo_maior.printar_matriz_adjacencia()
    grafo_maior.printar_matriz_indicencia()
    grafo_maior.printar_lista_adjacencia()














