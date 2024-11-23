from typing import List

import networkx as nx

from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.Aresta import Aresta
from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.GrafoListaAdjacencia import GrafoListaAdjacencia
from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.GrafoMatrizAdjascencia import GrafoMatrizAdjascencia
from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.GrafoMatrizIncidencia import GrafoMatrizIncidencia
from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.Vertice import Vertice


class Grafo:
    def __inir__(self, id = "grafo"):
        self.vertices: List[Vertice] = []
        self.arestas: List[Aresta] = []
        self.isDirecionado = False
        self.listaAdjacencia = GrafoListaAdjacencia(self.isDirecionado)
        self.matrizIncidencia = GrafoMatrizIncidencia(self.isDirecionado)
        self.matrizAdjacencia = GrafoMatrizAdjascencia(self.isDirecionado)
        self.id = id

    # PARTE 1

    def adicionarVertice(self, vertice: Vertice):
        self.vertices.append(vertice)

        self.listaAdjacencia.adicionar_vertice(vertice)
        self.matrizIncidencia.adicionar_vertice(vertice)
        self.matrizAdjacencia.adicionar_vertice(vertice)

    def removerVertice(self):
        print('a')

    def adicionarAresta(self, aresta: Aresta):
        rotuloVertice1 = aresta.get_inicio()
        rotuloVertice2 = aresta.get_fim()

        indice1 = next((i for i, vertice in enumerate(self.vertices) if vertice.valor_vertice == rotuloVertice1), None)
        indice2 = next((i for i, vertice in enumerate(self.vertices) if vertice.valor_vertice == rotuloVertice2), None)

        if (indice1 == None or indice2 == None):
            raise ValueError("Tentou adiciona ruma aresta com vértices que não existem no grafo.")

        self.arestas.append(aresta)
        self.listaAdjacencia.adicionar_aresta()
        self.matrizAdjacencia.adicionar_aresta()
        self.matrizIncidencia.adicionar_aresta()

    def removerAresta(self, rotulo_inicio: str, rotulo_fim: str):
        isFound = False

        for aresta in self.arestas:
            if aresta.get_inicio().rotulo == rotulo_inicio and aresta.get_fim().rotulo == rotulo_fim:
                self.arestas.remove(aresta)
                self.listaAdjacencia.remover_aresta(aresta)
                self.matrizAdjacencia.remover_aresta(aresta)
                self.matrizIncidencia.remover_aresta(aresta)
                isFound = True
                break

        if not isFound:
            raise ValueError("Tentou remover uma aresta que não existe.")

    def criar_grafo_com_x_vertices(self):
        print('a')

    def ponderar_vertice(self):
        print('a')

    def rotular_vertice(self):
        print("a")

    def ponderar_aresta(self):
        print('a')

    def rotular_aresta(self):
        print('a')

    def checar_adjacencia_entre_vertices(self):
        print('a')

    def checar_adjacencia_entre_arestas(self):
        print('a')

    def checar_existencia_de_aresta(self):
        print('a')

    def checar_quantidade_de_vertices(self):
        print('a')

    def checar_quantidade_de_arestas(self):
        print('a')

    def checar_se_grafo_vazio(self):
        print('a')

    def checar_se_grafo_completo(self):
        print('a')

    def checar_se_fortemente_conexo(self):
        print('a')

    def checar_se_semifortemente_conexo(self):
        print('a')

    def checar_se_simplesmente_conexo(self):
        print('a')

    def checar_quantidade_de_componentes_fortemente_conexos(self):
        print('a')

    def checar_ponte(self):
        print('a')

    def checar_articulacao(self):
        print('a')

    # PARTE 2

    # PARTE 3

    def criar_arquivo_grafo_graphml(self):
        grafo_networkx = self.para_networkx()
        nx.write_graphml(grafo_networkx, self.id + ".graphml")
        nx.write_gexf(grafo_networkx, self.id + ".graphml")

    def para_networkx(self):
        grafo = nx.DiGraph() if self.isDirecionado else nx.Graph()

        for vertice in self.vertices:
            grafo.add_node(vertice.valor_vertice)

        for (vertice1, vertice2), peso in self.arestas.items():
            grafo.add_edge(vertice1, vertice2, weight=peso)

        return grafo
