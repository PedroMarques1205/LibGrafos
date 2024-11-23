
class GrafoMatrizIncidencia:
    def __init__(self):
        self.matriz_incidencia = []  # Inicializa a matriz vazia
        self.vertices = []  # Lista para armazenar os vértices
        self.arestas = []  # Lista para armazenar as arestas

    def adicionar_vertice(self, vertice):
        self.vertices.append(vertice)
        # Expandir a matriz para incluir o novo vértice
        for linha in self.matriz_incidencia:
            linha.append(0)  # Adiciona uma coluna para o novo vértice

    def adicionar_aresta(self, aresta):
        self.arestas.append(aresta)
        # Cria uma nova linha para a nova aresta
        nova_linha = [0] * len(self.vertices)

        inicio = aresta.get_inicio()
        fim = aresta.get_fim()

        # Define as entradas da matriz de incidência
        nova_linha[self.vertices.index(inicio)] = -1  # Saída do vértice inicial
        nova_linha[self.vertices.index(fim)] = 1  # Entrada no vértice final

        self.matriz_incidencia.append(nova_linha)

    def exibir_matriz(self):
        print("Matriz de Incidência:")
        for linha in self.matriz_incidencia:
            print(linha)