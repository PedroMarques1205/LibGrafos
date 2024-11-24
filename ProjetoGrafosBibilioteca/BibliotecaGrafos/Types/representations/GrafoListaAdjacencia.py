from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.core.Aresta import Aresta
from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.core.Vertice import Vertice

class GrafoListaAdjacencia:
    def __init__(self, isDirecionado=False):
        self.vertices = []
        self.arestas = []
        self.isDirecionado = False

    def adicionar_vertice(self, vertice: Vertice):
        self.vertices.append(vertice)

    def remover_vertice(self, vertice: Vertice):
        self.vertices.remove(vertice)

    def adicionar_aresta(self, aresta: Aresta):
        vertice1 = self.retorna_vertice_existente(aresta.get_inicio().get_rotulo())
        vertice2 = self.retorna_vertice_existente(aresta.get_fim().get_rotulo())

        if vertice1 is not None and vertice2 is not None:
            self.arestas.append(aresta)
            vertice1.adicionar_aresta_de_saida(aresta)
            vertice2.adicionar_aresta_de_entrada(aresta)
        else:
            raise ValueError("Vértice não encontrado. (LA)")

    def remover_aresta(self, aresta_para_remover: Aresta):
        if aresta_para_remover is not None:
            self.arestas.remove(aresta_para_remover)

            aresta_para_remover.get_inicio().get_arestas_de_saida().remove(aresta_para_remover)
            aresta_para_remover.get_fim().get_arestas_de_entrada().remove(aresta_para_remover)
        else:
            print(f"Aresta não encontrada. (LA)")

    def retorna_vertice_existente(self, rotulo_do_vertice: str):
        indice = next((i for i, vertice in enumerate(self.vertices) if vertice.rotulo == rotulo_do_vertice), None)
        return self.vertices[indice]

    def get_aresta(self, valor_vertice_inicio, valor_vertice_fim):
        for aresta in self.arestas:
            if (aresta.get_inicio().get_peso() == valor_vertice_inicio and
                    aresta.get_fim().get_peso() == valor_vertice_fim):
                return aresta
        return None

    def mostrar_lista_adjacencia(self):
        listasDeAdjacencia = []
        for vertice in self.vertices:
            arestasDeSaidaVertice = vertice.get_arestas_de_saida()
            listaAdjacenciaDoVertice = set()

            for aresta in arestasDeSaidaVertice:
                listaAdjacenciaDoVertice.add(aresta.get_fim().get_rotulo())

            listasDeAdjacencia.append(list(listaAdjacenciaDoVertice))

        for i, vertice in enumerate(self.vertices):
            print(f"{vertice.get_rotulo()}: {listasDeAdjacencia[i]}")

    def set_ponderacao_vertice(self, rotulo, ponderacao):
        for i, vertice in enumerate(self.vertices):
            if (vertice.get_rotulo() == rotulo):
                vertice.set_ponderacao(ponderacao)

    def set_rotulaco_vertice(self, rotulo, novoRotulo):
        for i, vertice in enumerate(self.vertices):
            if (vertice.get_rotulo() == rotulo):
                vertice.set_rotulo(novoRotulo)

    def set_ponderacao_aresta(self, rotulo, ponderacao):
        for aresta in self.arestas:
            if (aresta.get_rotulo() == rotulo):
                aresta.set_peso(ponderacao)

    def set_rotulacao_aresta(self, rotulo, novoRotulo):
        for aresta in self.arestas:
            if (aresta.get_rotulo() == rotulo):
                aresta.set_rotulo(novoRotulo)