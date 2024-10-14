from Types.Grafo import Grafo

if __name__ == "__main__":
    grafo = Grafo()

    grafo.adicionar_vertice(1)
    grafo.adicionar_vertice(2)
    grafo.adicionar_vertice(3)
    grafo.adicionar_vertice(4)
    grafo.adicionar_vertice(5)

    grafo.adicionar_aresta(1, 2)
    grafo.adicionar_aresta(2, 3)
    grafo.adicionar_aresta(1, 4)

    grafo.mostrar_matriz_adjacencia()
