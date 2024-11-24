from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types import Aresta
from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.Vertice import Vertice

class GrafoMatrizIncidencia:
    def __init__(self, isDirecionado=False):
        self.matriz_incidencia = []
        self.vertices = []
        self.arestas = []
        self.isDirecionado = isDirecionado

    def adicionar_vertice(self, vertice: Vertice):
        self.vertices.append(vertice)
        for linha in self.matriz_incidencia:
            linha.append(0)

    def remover_vertice(self, vertice: Vertice):
        if vertice not in self.vertices:
            print("O vértice não existe no grafo.")
            return

        indice_vertice = self.vertices.index(vertice)

        arestas_conectadas = [
            aresta for aresta in self.arestas
            if aresta.get_inicio() == vertice or aresta.get_fim() == vertice
        ]

        for aresta in arestas_conectadas:
            self.remover_aresta(aresta)

        self.vertices.pop(indice_vertice)

        for linha in self.matriz_incidencia:
            linha.pop(indice_vertice)

    def adicionar_aresta(self, aresta):
        self.arestas.append(aresta)
        nova_linha = [0] * len(self.vertices)

        inicio = aresta.get_inicio()
        fim = aresta.get_fim()

        if self.isDirecionado:
            nova_linha[self.vertices.index(inicio)] = -1
            nova_linha[self.vertices.index(fim)] = 1
            inicio.adicionar_aresta_de_saida(aresta)
            fim.adicionar_aresta_de_entrada(aresta)
        else:
            nova_linha[self.vertices.index(inicio)] = 1
            nova_linha[self.vertices.index(fim)] = 1
            inicio.adicionar_aresta_de_saida(aresta)
            inicio.adicionar_aresta_de_entrada(aresta)
            fim.adicionar_aresta_de_saida(aresta)
            fim.adicionar_aresta_de_entrada(aresta)

        self.matriz_incidencia.append(nova_linha)

    def remover_aresta(self, aresta: Aresta):
        if aresta not in self.arestas:
            print('Você tentou remover uma aresta que não existe. (MI)')
            return

        indice_aresta = self.arestas.index(aresta)

        self.arestas.remove(aresta)
        self.matriz_incidencia.pop(indice_aresta)

        inicio = aresta.get_inicio()
        fim = aresta.get_fim()

        if self.isDirecionado:
            inicio.remover_aresta_de_saida(aresta)
            fim.remover_aresta_de_entrada(aresta)
        else:
            inicio.remover_aresta_de_saida(aresta)
            inicio.remover_aresta_de_entrada(aresta)
            fim.remover_aresta_de_saida(aresta)
            fim.remover_aresta_de_entrada(aresta)

    def exibir_matriz(self):
        print("Matriz de Incidência:")

        arestas_rotulos = [a.get_rotulo() for a in self.arestas]
        espacamento = max(len(r) for r in arestas_rotulos) + 2
        header = " " * 7 + " ".join(f"{rotulo:>{espacamento}}" for rotulo in arestas_rotulos)
        print(header)

        for i, vertice in enumerate(self.vertices):
            vertice_rotulo = (
                vertice.get_rotulo()
                if vertice.get_rotulo() is not None
                else str(vertice.get_peso())
            )
            linha = [self.matriz_incidencia[j][i] for j in range(len(self.matriz_incidencia))]
            linha_formatada = " ".join(f"{valor:>{espacamento}}" for valor in linha)
            print(f"{vertice_rotulo:<7} {linha_formatada}")

    def verificar_adjacencia_arestas(self, rotulo_aresta1, rotulo_aresta2):
        aresta1 = next((aresta for aresta in self.arestas if aresta.get_rotulo() == rotulo_aresta1), None)
        aresta2 = next((aresta for aresta in self.arestas if aresta.get_rotulo() == rotulo_aresta2), None)

        if not aresta1 or not aresta2:
            return False

        inicio1, fim1 = aresta1.get_inicio(), aresta1.get_fim()
        inicio2, fim2 = aresta2.get_inicio(), aresta2.get_fim()

        if self.isDirecionado:
            if inicio1 == inicio2 or inicio1 == fim2 or fim1 == inicio2 or fim1 == fim2:
                return True
        else:
            if inicio1 == inicio2 or inicio1 == fim2 or fim1 == inicio2 or fim1 == fim2:
                return True

        return False

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

    def verificar_grau_vertices(self):
        for vertice in self.vertices:
            vertice.grau = len(vertice.get_arestas_de_saida()) + len(vertice.get_arestas_de_entrada())

    def encontrar_pontes_naive(self):
        pontes = []
        for aresta in self.arestas:
            matriz_backup = [linha[:] for linha in self.matriz_incidencia]
            arestas_backup = self.arestas[:]
            self.remover_aresta(aresta)
            if not self.verificar_conectividade():
                pontes.append(aresta)
            self.matriz_incidencia = matriz_backup
            self.arestas = arestas_backup
        return pontes

    def fleury_naive(self):
        self.verificar_grau_vertices()
        if len([v for v in self.vertices if v.grau % 2 != 0]) > 2:
            raise Exception("O grafo não possui caminho euleriano.")

        v_inicial = next((v for v in self.vertices if v.grau % 2 != 0), self.vertices[0])
        caminho = []
        arestas_restantes = self.arestas[:]

        while arestas_restantes:
            pontes = self.encontrar_pontes_naive()

            for vertice in self.vertices:
                for aresta in vertice.get_arestas_de_saida() + vertice.get_arestas_de_entrada():
                    if aresta in pontes and len(arestas_restantes) > 1:
                        continue

                    caminho.append(aresta)
                    v_inicial = aresta.get_fim() if aresta.get_inicio() == v_inicial else aresta.get_inicio()

                    if aresta in arestas_restantes:
                        arestas_restantes.remove(aresta)

        caminho_formatado = " / ".join(
            [f"{aresta.get_inicio().get_peso()} / {aresta.get_fim().get_peso()}" for aresta in
             caminho])
        return caminho_formatado