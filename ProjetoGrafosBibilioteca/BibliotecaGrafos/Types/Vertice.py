# CLASSE VÉRTICE#
class Vertice:
    def __init__(self, ponderacao_vertice, rotulo=None):
        self.ponderacao_vertice = ponderacao_vertice
        self.grau = 0
        self.arestas_de_entrada = []
        self.arestas_de_saida = []
        self.rotulo = rotulo

    def get_ponderacao_vertice(self):
        return self.ponderacao_vertice

    def set_valor_vertice(self, valor_vertice):
        self.ponderacao_vertice = valor_vertice

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

