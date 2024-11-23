import networkx as nx
from typing import List

from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.Aresta import Aresta
from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.Vertice import Vertice


class GrafoMatrizAdjascencia:
    def __init__(self):
        self.isDirecionado = False
        self.vertices: List[Vertice] = []
        self.matrizAdjacencia = []
        self.arestas = {}

    def adicionar_vertice(self, newVertice):
        self.vertices.append(newVertice)
        for linha in self.matrizAdjacencia:
            linha.append(0)
        self.matrizAdjacencia.append([0] * len(self.vertices))

    def criar_arestas(self, rotuloVertice1: str, rotuloVertice2: str, peso: int = 1):
        indice1 = next((i for i, vertice in enumerate(self.vertices) if vertice.valor_vertice == rotuloVertice1), None)
        indice2 = next((i for i, vertice in enumerate(self.vertices) if vertice.valor_vertice == rotuloVertice2), None)

        if indice1 is None or indice2 is None:
            raise ValueError("Vértice não encontrado.")

        self.matrizAdjacencia[indice1][indice2] = peso
        self.arestas[(rotuloVertice1, rotuloVertice2)] = peso

        if not self.isDirecionado:
            self.matrizAdjacencia[indice2][indice1] = peso
            self.arestas[(rotuloVertice2, rotuloVertice1)] = peso

    def remover_arestas(self, rotuloVertice1: str, rotuloVertice2: str):
        indice1 = next((i for i, vertice in enumerate(self.vertices) if vertice.rotulo == rotuloVertice1), None)
        indice2 = next((i for i, vertice in enumerate(self.vertices) if vertice.rotulo == rotuloVertice2), None)

        if indice1 is None or indice2 is None:
            raise ValueError("Vértice não encontrado.")

        self.matrizAdjacencia[indice1][indice2] = 0
        del self.arestas[(rotuloVertice1, rotuloVertice2)]

        if not self.isDirecionado:
            self.matrizAdjacencia[indice2][indice1] = 0
            del self.arestas[(rotuloVertice2, rotuloVertice1)]

    def rotular_vertice(self, indice: int, novo_rotulo: str):
        if indice < 0 or indice >= len(self.vertices):
            raise ValueError("Vértice não encontrado.")
        self.vertices[indice].rotulo = novo_rotulo

    def ponderar_aresta(self, rotuloVertice1: str, rotuloVertice2: str, novo_peso: int):
        indice1 = next((i for i, vertice in enumerate(self.vertices) if vertice.rotulo == rotuloVertice1), None)
        indice2 = next((i for i, vertice in enumerate(self.vertices) if vertice.rotulo == rotuloVertice2), None)

        if indice1 is None or indice2 is None:
            raise ValueError("Vértice não encontrado.")

        self.matrizAdjacencia[indice1][indice2] = novo_peso
        self.arestas[(rotuloVertice1, rotuloVertice2)] = novo_peso

        if not self.isDirecionado:
            self.matrizAdjacencia[indice2][indice1] = novo_peso
            self.arestas[(rotuloVertice2, rotuloVertice1)] = novo_peso

    def checar_adjacencia_vertices(self, rotuloVertice1: str, rotuloVertice2: str) -> bool:
        indice1 = next((i for i, vertice in enumerate(self.vertices) if vertice.rotulo == rotuloVertice1), None)
        indice2 = next((i for i, vertice in enumerate(self.vertices) if vertice.rotulo == rotuloVertice2), None)

        if indice1 is None or indice2 is None:
            raise ValueError("Vértice não encontrado.")

        return self.matrizAdjacencia[indice1][indice2] != 0

    def checar_adjacencia_arestas(self, rotuloVertice1: str, rotuloVertice2: str, rotuloVertice3: str,
                                  rotuloVertice4: str) -> bool:
        return self.checar_adjacencia_vertices(rotuloVertice1, rotuloVertice2) and self.checar_adjacencia_vertices(
            rotuloVertice3, rotuloVertice4)

    def checar_existencia_aresta(self, rotuloVertice1: str, rotuloVertice2: str) -> bool:
        return self.checar_adjacencia_vertices(rotuloVertice1, rotuloVertice2)

    def quantidade_vertices(self) -> int:
        return len(self.vertices)

    def quantidade_arestas(self) -> int:
        return len(self.arestas)

    def grafo_vazio(self) -> bool:
        return len(self.vertices) == 0

    def grafo_completo(self) -> bool:  # revisar essa aqui
        if self.grafo_vazio():
            return False
        num_vertices = len(self.vertices)
        for i in range(num_vertices):
            for j in range(num_vertices):
                if i != j and self.matrizAdjacencia[i][j] == 0:
                    return False
        return True

    def para_networkx(self):
        grafo = nx.DiGraph() if self.isDirecionado else nx.Graph()

        for vertice in self.vertices:
            grafo.add_node(vertice.valor_vertice)

        for (vertice1, vertice2), peso in self.arestas.items():
            grafo.add_edge(vertice1, vertice2, weight=peso)

        return grafo

    def printar_matriz_adjacencia(self):
        if self.grafo_vazio():
            print("O grafo está vazio.")
            return

        print("Matriz de Adjacência:")
        print("    ", end="")
        for vertice in self.vertices:
            print(f"{vertice.valor_vertice:>4}", end="")
        print()

        for i, vertice in enumerate(self.vertices):
            print(f"{self.vertices[i].valor_vertice:>4}", end="")

            for valor in self.matrizAdjacencia[i]:
                print(f"{valor:>4}", end="")
            print()

    def verificar_fortemente_conexo(self):
        visitados = set()

        def busca_em_profundidade(vertice, grafo, visitado=None):
            if visitado is None:
                visitado = set()
            visitado.add(vertice)

            indice = self.vertices.index(vertice)
            for i, adjacente in enumerate(self.matrizAdjacencia[indice]):
                if adjacente != 0 and self.vertices[i] not in visitado:
                    busca_em_profundidade(self.vertices[i], grafo, visitado)

        if not self.vertices:
            return True

        busca_em_profundidade(self.vertices[0], self, visitados)
        if len(visitados) != len(self.vertices):
            return False

        if self.isDirecionado:
            visitados.clear()
            grafo_invertido = self.transpor()
            busca_em_profundidade(grafo_invertido.vertices[0], grafo_invertido, visitados)

        if len(visitados) != len(self.vertices):
            return False

        return True
    
    def verificar_semi_fortemente_conexo(self):
        def busca_em_profundidade(vertice, grafo, visitado = None):
            if visitado is None:
                visitado = set()
            visitado.add(vertice)
            
            indice = self.vertices.index(vertice)
            for i, adjacente in enumerate(self.matrizAdjacencia[indice]):
                if adjacente != 0 and self.vertices[i] not in visitado:
                    busca_em_profundidade(self.vertices[i], grafo, visitado)
                    
        if not self.vertices:
            return True
        visitados = set()
        busca_em_profundidade(self.vertices[0], self, visitados)
        if len(visitados) != len(self.vertices):
            return False
        visitadosGrafoInvertido = set()
        grafoInvertido = self.transpor()
        busca_em_profundidade(grafoInvertido.vertices[0], grafoInvertido, visitadosGrafoInvertido)
        
        if len(visitadosGrafoInvertido) != len(self.vertices):
            return False
        
        return True

    def vertifica_simplesmente_conexo(self):
        isFortementeConexo = self.verificar_fortemente_conexo()
        isSemiForte = self.verificar_semi_fortemente_conexo()

        if not isFortementeConexo and not isSemiForte:
            return True
        return False
        
        
    def transpor(self):
        grafo_invertido = GrafoMatrizAdjascencia()
        for vertice in self.vertices:
            grafo_invertido.adicionar_vertice(vertice)
        for (vertice1, vertice2), peso in self.arestas.items():
            grafo_invertido.criar_arestas(vertice2, vertice1, peso)
        return grafo_invertido