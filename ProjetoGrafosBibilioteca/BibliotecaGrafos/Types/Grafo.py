class Vertice:
    def __init__(self, valor_vertice):
        self.valor_vertice = valor_vertice
        self.grau = 0
        self.arestas_de_entrada = []
        self.arestas_de_saida = []

    def get_valor_vertice(self):
        return self.valor_vertice

    def set_valor_vertice(self, valor_vertice):
        self.valor_vertice = valor_vertice

    def get_arestas_de_entrada(self):
        return self.arestas_de_entrada

    def adicionar_aresta_de_entrada(self, aresta):
        self.arestas_de_entrada.append(aresta)

    def adicionar_aresta_de_saida(self, aresta):
        self.arestas_de_saida.append(aresta)


class Aresta:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

    def get_inicio(self):
        return self.inicio

    def set_inicio(self, inicio):
        self.inicio = inicio

    def get_fim(self):
        return self.fim

    def set_fim(self, fim):
        self.fim = fim


class Grafo:
    def __init__(self):
        self.vertices = []
        self.arestas = []

    def adicionar_vertice(self, valor_vertice):
        if self.get_vertice(valor_vertice) is None:
            self.vertices.append(Vertice(valor_vertice))

    def adicionar_aresta(self, inicio_aresta, fim_aresta):
        vertice_inicio = self.get_vertice(inicio_aresta)
        vertice_fim = self.get_vertice(fim_aresta)
        nova_aresta = Aresta(vertice_inicio, vertice_fim)
        self.arestas.append(nova_aresta)

    def get_vertice(self, valor_vertice):
        for vertice in self.vertices:
            if vertice.get_valor_vertice() == valor_vertice:
                return vertice
        return None

    def mostrar_matriz_adjacencia(self):
        tamanho = len(self.vertices)
        matriz_adjacencia = [[0] * tamanho for _ in range(tamanho)]

        for aresta in self.arestas:
            inicio = aresta.get_inicio()
            fim = aresta.get_fim()

            indice_inicio = self.vertices.index(inicio)
            indice_fim = self.vertices.index(fim)

            if indice_inicio != -1 and indice_fim != -1:
                matriz_adjacencia[indice_inicio][indice_fim] = 1

        print("  ", end="")
        for vertice in self.vertices:
            print(vertice.get_valor_vertice(), end=" ")
        print()

        for i, vertice in enumerate(self.vertices):
            print(vertice.get_valor_vertice(), end=" ")
            for j in range(tamanho):
                print(matriz_adjacencia[i][j], end=" ")
            print()

    def mostrar_matriz_incidencia(self):
        qtdVertices = len(self.vertices)
        qtdArestas = len(self.arestas)

        matriz_incidencia = [[0] * qtdArestas for _ in range(qtdVertices)]

        for i, vertice in enumerate(self.vertices):
            for j, aresta in enumerate(self.arestas):
                if aresta.get_inicio() == vertice:
                    matriz_incidencia[i][j] = -1
                elif aresta.get_fim() == vertice:
                    matriz_incidencia[i][j] = 1

        print("  ", end="")
        for idx, _ in enumerate(self.arestas):
            print(f"A{idx + 1}", end=" ")
        print()

        for i, vertice in enumerate(self.vertices):
            print(vertice.get_valor_vertice(), end=" ")
            for j in range(qtdArestas):
                print(matriz_incidencia[i][j], end=" ")
            print()
