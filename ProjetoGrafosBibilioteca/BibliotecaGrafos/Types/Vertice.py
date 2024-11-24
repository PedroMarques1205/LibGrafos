class Vertice:
    def __init__(self, peso_vertice, rotulo=None):
        self.peso_vertice = peso_vertice
        self.grau = 0
        self.arestas_de_entrada = []
        self.arestas_de_saida = []
        self.rotulo = rotulo

    def get_peso(self):
        return self.peso_vertice

    def set_valor_vertice(self, valor_vertice):
        self.peso_vertice = valor_vertice

    def get_arestas_de_entrada(self):
        return self.arestas_de_entrada

    def get_arestas_de_saida(self):
        return self.arestas_de_saida

    def adicionar_aresta_de_entrada(self, aresta):
        self.arestas_de_entrada.append(aresta)

    def adicionar_aresta_de_saida(self, aresta):
        self.arestas_de_saida.append(aresta)

    def get_rotulo(self):
        return self.rotulo

    def set_rotulo(self, rotulo):
        self.rotulo = rotulo

    def set_ponderacao(self, ponderacao):
        self.peso_vertice = ponderacao

    def remover_aresta_de_saida(self, aresta):
        if aresta in self.arestas_de_saida:
            self.arestas_de_saida.remove(aresta)

    def remover_aresta_de_entrada(self, aresta):
        if aresta in self.arestas_de_entrada:
            self.arestas_de_entrada.remove(aresta)

