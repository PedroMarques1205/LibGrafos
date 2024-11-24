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
        print('IMPLEMENTAR DEPOIS')

    def adicionarAresta(self, aresta: Aresta):
        A1 = aresta.get_inicio()
        A2 = aresta.get_fim()

        indice1 = next((i for i, vertice in enumerate(self.vertices) if vertice.peso_vertice == A1.get_ponderacao_vertice()), None)
        indice2 = next((i for i, vertice in enumerate(self.vertices) if vertice.peso_vertice == A2.get_ponderacao_vertice()), None)

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

    def criar_grafo_com_x_vertices(self, num_vertices: int):
        for i in range(num_vertices):
            newVertice = Vertice("V"+i, "V"+i)
            self.adicionarVertice(newVertice)
            
    def criar_grafo_com_x_arestas(self):
        print('IMPLEMENTAR DEPOIS')

    def ponderar_vertice(self, rotulo_vertice: str, ponderacao_vertice):
        for v in self.vertices:
            if v.get_rotulo() == rotulo_vertice:
                v.set_ponderacao(ponderacao_vertice)
                self.listaAdjacencia.set_ponderacao_vertice(rotulo_vertice, ponderacao_vertice)
                self.matrizAdjacencia.set_ponderacao_vertice(rotulo_vertice, ponderacao_vertice)
                self.matrizIncidencia.set_ponderacao_vertice(rotulo_vertice, ponderacao_vertice)
                break

    def rotular_vertice(self, rotulo_atual_vertice: str, rotulo_novo_vertice: str):
        for v in self.vertices:
            if v.get_rotulo() == rotulo_atual_vertice:
                v.set_rotulo(rotulo_novo_vertice)
                self.listaAdjacencia.set_rotulaco_vertice(rotulo_atual_vertice, rotulo_novo_vertice)
                self.matrizAdjacencia.set_rotulaco_vertice(rotulo_atual_vertice, rotulo_novo_vertice)
                self.matrizIncidencia.set_rotulaco_vertice(rotulo_atual_vertice, rotulo_novo_vertice)
                break

    def ponderar_aresta(self, rotulo_aresta: str, peso_aresta):
        for a in self.arestas:
            if a.get_rotulo() == rotulo_aresta:
                a.set_peso(peso_aresta)
                self.listaAdjacencia.set_ponderacao_aresta(rotulo_aresta, peso_aresta)
                self.matrizAdjacencia.set_ponderacao_aresta(rotulo_aresta, peso_aresta)
                self.matrizIncidencia.set_ponderacao_aresta(rotulo_aresta, peso_aresta)
                break

    def rotular_aresta(self, rotulo_atual_aresta: str, rotulo_novo_aresta: str):
        for a in self.arestas:
            if a.get_rotulo() == rotulo_atual_aresta:
                a.set_rotulo(rotulo_novo_aresta)
                self.listaAdjacencia.set_rotulacao_aresta(rotulo_atual_aresta, rotulo_novo_aresta)
                self.matrizAdjacencia.set_rotulacao_aresta(rotulo_atual_aresta, rotulo_novo_aresta)
                self.matrizIncidencia.set_rotulacao_aresta(rotulo_atual_aresta, rotulo_novo_aresta)

    def checar_adjacencia_entre_vertices(self, rotulo_vertice_um: str, rotulo_vertice_dois: str):
        return self.matrizAdjacencia.checar_adjacencia_vertices(rotulo_vertice_um, rotulo_vertice_dois)

    def checar_adjacencia_entre_arestas(self, rotulo_vertice_um: str, rotulo_vertice_dois: str):
        return self.matrizIncidencia.verificar_adjacencia_arestas(rotulo_vertice_um, rotulo_vertice_dois)

    def checar_existencia_de_aresta(self, rotulo: str):
        return any(a.get_rotulo() == rotulo for a in self.arestas)

    def checar_existencia_de_vertice(self, rotulo: str):
        return any(v.get_rotulo() == rotulo for v in self.vertices)

    def checar_quantidade_de_vertices(self):
        return len(self.vertices)

    def checar_quantidade_de_arestas(self):
        return len(self.arestas)

    def checar_se_grafo_vazio(self):
        return len(self.vertices) == 0

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
            grafo.add_node(vertice.peso_vertice)

        for aresta in self.arestas:
            grafo.add_edge(aresta.get_inicio(), aresta.get_fim(), weight=aresta.get_peso())

        return grafo

