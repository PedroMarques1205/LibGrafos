from typing import List

import networkx as nx

from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.Aresta import Aresta
from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.GrafoListaAdjacencia import GrafoListaAdjacencia
from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.GrafoMatrizAdjascencia import GrafoMatrizAdjascencia
from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.GrafoMatrizIncidencia import GrafoMatrizIncidencia
from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.Vertice import Vertice


class Grafo:
    def __init__(self, id: str, isDirecionado: bool):
        self.vertices = []
        self.arestas = []
        self.isDirecionado = isDirecionado
        self.listaAdjacencia = GrafoListaAdjacencia(self.isDirecionado)
        self.matrizIncidencia = GrafoMatrizIncidencia(self.isDirecionado)
        self.matrizAdjacencia = GrafoMatrizAdjascencia(self.isDirecionado)
        self.id = id

    # PARTE 1

    def printar_matriz_adjacencia(self):
        self.matrizAdjacencia.printar_matriz_adjacencia()

    def printar_lista_adjacencia(self):
        self.listaAdjacencia.mostrar_lista_adjacencia()

    def printar_matriz_indicencia(self):
        self.matrizIncidencia.exibir_matriz()

    def adicionarVertice(self, vertice: Vertice):
        self.vertices.append(vertice)

        self.listaAdjacencia.adicionar_vertice(vertice)
        self.matrizIncidencia.adicionar_vertice(vertice)
        self.matrizAdjacencia.adicionar_vertice(vertice)

    def removerVertice(self):
        print('a')

    def adicionarAresta(self, aresta: Aresta):
        A1 = aresta.get_inicio()
        A2 = aresta.get_fim()

        indice1 = next((i for i, vertice in enumerate(self.vertices) if vertice.ponderacao_vertice == A1.get_ponderacao_vertice()), None)
        indice2 = next((i for i, vertice in enumerate(self.vertices) if vertice.ponderacao_vertice == A2.get_ponderacao_vertice()), None)

        if (indice1 == None or indice2 == None):
            raise ValueError("FOI AQUI QUE ESSE ERRO ESTOUROU.")

        self.arestas.append(aresta)
        self.listaAdjacencia.adicionar_aresta(aresta)
        self.matrizAdjacencia.adicionar_arestas(aresta)
        self.matrizIncidencia.adicionar_aresta(aresta)

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

        # Adicionar os vértices ao grafo
        for vertice in self.vertices:
            grafo.add_node(vertice.ponderacao_vertice)

        # Iterar pelas arestas e adicionar as conexões
        for aresta in self.arestas:
            grafo.add_edge(aresta.get_inicio(), aresta.get_fim(), weight=aresta.get_peso())

        return grafo

