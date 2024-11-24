from typing import List
from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.Aresta import Aresta
from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.Vertice import Vertice


class GrafoMatrizAdjascencia:
    def __init__(self, isDirecionado=False):
        self.isDirecionado = isDirecionado
        self.vertices: List[Vertice] = []
        self.matrizAdjacencia = []
        self.arestas = {}

    def adicionar_vertice(self, vertice: Vertice):
        self.vertices.append(vertice)
        for linha in self.matrizAdjacencia:
            linha.append(0)
        self.matrizAdjacencia.append([0] * len(self.vertices))

    def remover_vertice(self, vertice: Vertice):
        if vertice not in self.vertices:
            raise ValueError("Vértice não encontrado. (MA)")

        indice = self.vertices.index(vertice)
        self.vertices.pop(indice)
        self.matrizAdjacencia.pop(indice)

        for linha in self.matrizAdjacencia:
            linha.pop(indice)

        arestas_para_remover = [
            chave for chave in self.arestas.keys()
            if chave[0] == vertice or chave[1] == vertice
        ]
        for chave in arestas_para_remover:
            del self.arestas[chave]

    def adicionar_aresta(self, aresta: Aresta):
        indice1 = self.retorna_vertice_existente(aresta.get_inicio().get_rotulo())
        indice2 = self.retorna_vertice_existente(aresta.get_fim().get_rotulo())

        if indice1 is None or indice2 is None:
            raise ValueError("Vértice não encontrado. (MA)")

        self.matrizAdjacencia[indice1][indice2] = aresta.get_peso()
        self.arestas[(aresta.get_inicio(), aresta.get_fim())] = aresta.get_peso()

        if not self.isDirecionado:
            self.matrizAdjacencia[indice2][indice1] = aresta.get_peso()
            self.arestas[(aresta.get_fim(), aresta.get_inicio())] = aresta.get_peso()

    def remover_aresta(self, aresta: Aresta):
        indice1 = self.retorna_vertice_existente(aresta.get_inicio().get_rotulo())
        indice2 = self.retorna_vertice_existente(aresta.get_fim().get_rotulo())

        if indice1 is None or indice2 is None:
            raise ValueError("Vértice não encontrado. (MA)")

        self.matrizAdjacencia[indice1][indice2] = 0

        if (aresta.get_inicio(), aresta.get_fim()) in self.arestas:
            del self.arestas[(aresta.get_inicio(), aresta.get_fim())]

        if not self.isDirecionado:
            self.matrizAdjacencia[indice2][indice1] = 0
            if (aresta.get_fim(), aresta.get_inicio()) in self.arestas:
                del self.arestas[(aresta.get_fim(), aresta.get_inicio())]

        if self.isDirecionado:
            aresta.get_inicio().remover_aresta_de_saida(aresta)
            aresta.get_fim().remover_aresta_de_entrada(aresta)
        else:
            aresta.get_inicio().remover_aresta_de_saida(aresta)
            aresta.get_inicio().remover_aresta_de_entrada(aresta)
            aresta.get_fim().remover_aresta_de_saida(aresta)
            aresta.get_fim().remover_aresta_de_entrada(aresta)

    def rotular_vertice(self, indice: int, novo_rotulo: str):
        if indice < 0 or indice >= len(self.vertices):
            raise ValueError("Vértice não encontrado. (MA)")
        self.vertices[indice].rotulo = novo_rotulo

    def ponderar_aresta(self, rotuloVertice1: str, rotuloVertice2: str, novo_peso: int):
        indice1 = self.retorna_vertice_existente(rotuloVertice1)
        indice2 = self.retorna_vertice_existente(rotuloVertice2)

        if indice1 is None or indice2 is None:
            raise ValueError("Vértice não encontrado. (MA)")

        self.matrizAdjacencia[indice1][indice2] = novo_peso
        self.arestas[(rotuloVertice1, rotuloVertice2)] = novo_peso

        if not self.isDirecionado:
            self.matrizAdjacencia[indice2][indice1] = novo_peso
            self.arestas[(rotuloVertice2, rotuloVertice1)] = novo_peso

    def checar_adjacencia_vertices(self, rotuloVertice1: str, rotuloVertice2: str) -> bool:
        indice1 = self.retorna_vertice_existente(rotuloVertice1)
        indice2 = self.retorna_vertice_existente(rotuloVertice2)

        if indice1 is None or indice2 is None:
            raise ValueError("Vértice não encontrado. (MA)")

        return self.matrizAdjacencia[indice1][indice2] != 0

    def printar_matriz_adjacencia(self):
        print("Matriz de Adjacência:")
        print("    ", end="")
        for vertice in self.vertices:
            print(f"{vertice.get_rotulo():>4}", end="")
        print()

        for i, vertice in enumerate(self.vertices):
            print(f"{self.vertices[i].get_rotulo():>4}", end="")

            for valor in self.matrizAdjacencia[i]:
                print(f"{valor:>4}", end="")
            print()

    def set_ponderacao_vertice(self, rotulo, ponderacao):
        for i, vertice in enumerate(self.vertices):
            if (vertice.get_rotulo() == rotulo):
                vertice.set_ponderacao(ponderacao)

    def set_rotulaco_vertice(self, rotulo, novoRotulo):
        for i, vertice in enumerate(self.vertices):
            if (vertice.get_rotulo() == rotulo):
                vertice.set_rotulo(novoRotulo)

    def set_ponderacao_aresta(self, rotulo, ponderacao):
        if rotulo in self.arestas:
            aresta = self.arestas[rotulo]
            aresta.set_ponderacao(ponderacao)

    def set_rotulacao_aresta(self, rotulo, novoRotulo):
        if rotulo in self.arestas:
            self.arestas[novoRotulo] = self.arestas.pop(rotulo)

    def retorna_vertice_existente(self, rotulo_do_vertice: str):
        indice = next((i for i, vertice in enumerate(self.vertices) if vertice.rotulo == rotulo_do_vertice), None)
        return indice