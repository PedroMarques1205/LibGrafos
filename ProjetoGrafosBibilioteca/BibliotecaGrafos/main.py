import networkx as nx

from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.Aresta import Aresta
from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.GrafoMatrizAdjascencia import GrafoMatrizAdjascencia
from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.GrafoMatrizIncidencia import GrafoMatrizIncidencia
from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.Vertice import Vertice

if __name__ == "__main__":
    grafo = GrafoMatrizAdjascencia()
    grafo.isDirecionado = False

    vA = Vertice("A")
    vB = Vertice("B")
    vC = Vertice("C")
    vD = Vertice("D")

    grafo.adicionar_vertice(vA)
    grafo.adicionar_vertice(vB)
    grafo.adicionar_vertice(vC)
    grafo.adicionar_vertice(vD)

    grafo.criar_arestas(vA.valor_vertice, vB.valor_vertice)
    grafo.criar_arestas(vD.valor_vertice, vB.valor_vertice)
    grafo.criar_arestas(vC.valor_vertice, vA.valor_vertice)
    grafo.criar_arestas(vC.valor_vertice, vD.valor_vertice)


    isFConexo = grafo.verificar_fortemente_conexo()
    grafo.printar_matriz_adjacencia()
    
    print(" ")
    print("== TESTE FORTEMENTE CONEXO GRAFO 1 ==")
    print(" ")
    print(isFConexo)
    
    grafo_networkx = grafo.para_networkx()


    nx.write_graphml(grafo_networkx, "testeconectividade.graphml")
    nx.write_gexf(grafo_networkx, "testeconectividade.gexf")
    
    grafoOriginal = GrafoMatrizAdjascencia()
    grafoOriginal.isDirecionado = True

    grafoOriginal.adicionar_vertice(vA)
    grafoOriginal.adicionar_vertice(vB)
    grafoOriginal.adicionar_vertice(vC)
    
    grafoOriginal.criar_arestas(vA.valor_vertice, vB.valor_vertice)
    grafoOriginal.criar_arestas(vB.valor_vertice, vC.valor_vertice)
    
    print(" ")
    print("== TESTE SEMI-FORTEMENTE CONEXO GRAFO 2 ==")
    print(" ")
    print(grafoOriginal.verificar_semi_fortemente_conexo())
    
    grafo_networkx_dois = grafoOriginal.para_networkx()
    nx.write_graphml(grafo_networkx_dois, "grafo_semiforte.graphml")
    nx.write_gexf(grafo_networkx_dois, "grafo_semiforte.gexf")
    
    print(" ")
    print("== MATRIZ DO SEMIFORTE ==")
    print(" ")
    grafoOriginal.printar_matriz_adjacencia()
    
    grafoTransposto = grafoOriginal.transpor()
    print(" ")
    print("== MATRIZ DO SEMIFORTE TRANSPOSTO ==")
    print(" ")
    grafoTransposto.printar_matriz_adjacencia()
    
    
    grafo_networkx_dois_transposto = grafoTransposto.para_networkx()
    nx.write_graphml(grafo_networkx_dois_transposto, "grafo_transposto.graphml")
    nx.write_gexf(grafo_networkx_dois_transposto, "grafo_transposto.gexf")

    
    

