from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.Aresta import Aresta
from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.Grafo import Grafo
from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.GrafoMatrizIncidencia import GrafoMatrizIncidencia
import time
import sys

from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.Vertice import Vertice

if __name__ == "__main__":
    grafo = Grafo("coisa", True)

    vA = Vertice(peso_vertice='A', rotulo='A')
    vB = Vertice(peso_vertice='B', rotulo='B')
    vC = Vertice(peso_vertice='C', rotulo='C')

    grafo.adicionarVertice(vA)
    grafo.adicionarVertice(vB)
    grafo.adicionarVertice(vC)

    grafo.adicionarAresta(Aresta(vA, vB, rotulo='e1', peso=1))
    grafo.adicionarAresta(Aresta(vB, vC, rotulo='e1', peso=1))

    grafo.criar_arquivo_grafo_graphml()

    grafo.printar_matriz_adjacencia()
    grafo.printar_matriz_indicencia()
    grafo.printar_lista_adjacencia()

