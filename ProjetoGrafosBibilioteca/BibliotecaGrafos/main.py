from Types.Grafo import Grafo

if __name__ == "__main__":
    grafo = Grafo()

    grafo.adicionar_vertice('a')
    grafo.adicionar_vertice('b')
    grafo.adicionar_vertice('c')
    grafo.adicionar_vertice('d')
    grafo.adicionar_vertice('e')

    grafo.adicionar_aresta('a', 'b')
    grafo.adicionar_aresta('a', 'c')
    grafo.adicionar_aresta('c', 'b')
    grafo.adicionar_aresta('c', 'd')
    grafo.adicionar_aresta('b', 'd')
    grafo.adicionar_aresta('b', 'e')
    grafo.adicionar_aresta('d', 'e')

    print(f"\nMatriz Adjacência:\n")
    grafo.mostrar_matriz_adjacencia()
    print(f"\nMatriz Incidência:\n")
    grafo.mostrar_matriz_incidencia()

    print(f"\nLista Adjacência:\n")
    grafo.mostrar_lista_adjacencia()

    print(f"\n \n")
    print(grafo.eh_fortemente_conexo())
    print(grafo.eh_semi_fortemente_conexo())
    print(grafo.eh_simplesmente_conexo())

    print(grafo.contar_componentes_fortemente_conexos())