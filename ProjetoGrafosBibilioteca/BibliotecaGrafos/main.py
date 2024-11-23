from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.Aresta import Aresta
from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.GrafoMatrizIncidencia import GrafoMatrizIncidencia
from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.Vertice import Vertice

if __name__ == "__main__":
    grafo = GrafoMatrizIncidencia(True)

    v1 = Vertice("a")
    v2 = Vertice("b")
    v3 = Vertice("c")
    v4 = Vertice("d")
    v5 = Vertice("e")

    a1 = Aresta(v1, v2, "e1", 1)
    a2 = Aresta(v1, v3, "e2", 1)
    a3 = Aresta(v2, v3, "e3", 1)
    a4 = Aresta(v2, v4, "e4", 1)
    a5 = Aresta(v3, v4, "e5", 1)
    a6 = Aresta(v4, v5, "e6", 1)
    a7 = Aresta(v3, v5, "e7", 1)

    grafo.adicionar_vertice(v1)
    grafo.adicionar_vertice(v2)
    grafo.adicionar_vertice(v3)
    grafo.adicionar_vertice(v4)
    grafo.adicionar_vertice(v5)

    grafo.adicionar_aresta(a1)
    grafo.adicionar_aresta(a2)
    grafo.adicionar_aresta(a3)
    grafo.adicionar_aresta(a4)
    grafo.adicionar_aresta(a5)
    grafo.adicionar_aresta(a6)
    grafo.adicionar_aresta(a7)

    grafo.exibir_matriz()


    print(grafo.verificar_existencia_aresta(v1,v5))


