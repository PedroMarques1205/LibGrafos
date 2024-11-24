from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.Aresta import Aresta
from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.Grafo import Grafo
from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.GrafoMatrizIncidencia import GrafoMatrizIncidencia
import time
import sys

from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.Vertice import Vertice

if __name__ == "__main__":
    grafo = Grafo("coisa", True)

    vA = Vertice(peso_vertice='1', rotulo='A')
    vB = Vertice(peso_vertice='2', rotulo='B')
    vC = Vertice(peso_vertice='3', rotulo='C')

    grafo.adicionarVertice(vA)
    grafo.adicionarVertice(vB)
    grafo.adicionarVertice(vC)

    grafo.adicionarAresta(Aresta(vA, vB, rotulo='e1', peso=1))
    grafo.adicionarAresta(Aresta(vB, vC, rotulo='e1', peso=1))

    grafo.criar_arquivo_grafo_graphml()

    print(" ")
    print("== ANTES DA EDICAO ==")
    print(" ")

    grafo.printar_matriz_adjacencia()
    grafo.printar_matriz_indicencia()
    grafo.printar_lista_adjacencia()

    grafo.rotular_vertice('A', 'y')

    print(" ")
    print("== ANTES DA APÓS EDIT 1 ==")
    print(" ")

    grafo.printar_matriz_adjacencia()
    grafo.printar_matriz_indicencia()
    grafo.printar_lista_adjacencia()

    grafo.ponderar_vertice('Y', 8)

    print(" ")
    print("== ANTES DA APÓS EDIT 2 ==")
    print(" ")

    grafo.printar_matriz_adjacencia()
    grafo.printar_matriz_indicencia()
    grafo.printar_lista_adjacencia()

    grafo.rotular_aresta('e1', 'y1')

    print(" ")
    print("== ANTES DA APÓS EDIT 3 ==")
    print(" ")

    grafo.printar_matriz_adjacencia()
    grafo.printar_matriz_indicencia()
    grafo.printar_lista_adjacencia()

    grafo.ponderar_aresta('y1', 8)

    print(" ")
    print("== ANTES DA APÓS EDIT 4 ==")
    print(" ")

    grafo.printar_matriz_adjacencia()
    grafo.printar_matriz_indicencia()
    grafo.printar_lista_adjacencia()


