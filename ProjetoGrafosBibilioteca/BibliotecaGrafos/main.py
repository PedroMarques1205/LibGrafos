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
    vD = Vertice(peso_vertice='8', rotulo='D')

    grafo.adicionarVertice(vA)
    grafo.adicionarVertice(vB)
    grafo.adicionarVertice(vC)
    grafo.adicionarVertice(vD)

    grafo.adicionarAresta(Aresta(vA, vB, rotulo='e1', peso=1))
    grafo.adicionarAresta(Aresta(vB, vC, rotulo='e2', peso=1))
    grafo.adicionarAresta(Aresta(vC, vD, rotulo='e3', peso=1))


    grafo.printar_matriz_adjacencia()

    grafo.criar_arquivo_grafo_graphml()






