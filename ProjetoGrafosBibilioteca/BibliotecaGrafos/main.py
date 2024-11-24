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

















