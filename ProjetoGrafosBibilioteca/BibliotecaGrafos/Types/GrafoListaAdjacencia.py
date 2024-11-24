from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.Aresta import Aresta
from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.Vertice import Vertice


# CLASSE GRAFO#
class GrafoListaAdjacencia:
    def __init__(self, isDirecionado=False):
        self.vertices = []
        self.arestas = []
        self.isDirecionado = False

    def adicionar_vertice(self, vertice: Vertice):
        self.vertices.append(vertice)

    def adicionar_aresta(self, aresta: Aresta):
        vertice_inicio = self.get_vertice(aresta.get_inicio().get_peso())
        vertice_fim = self.get_vertice(aresta.get_fim().get_peso())

        if vertice_inicio is not None and vertice_fim is not None:
            self.arestas.append(aresta)

            vertice_inicio.adicionar_aresta_de_saida(aresta)
            vertice_fim.adicionar_aresta_de_entrada(aresta)
        else:
            raise ValueError("Vértice não encontrado. (LA)")

    def get_vertice(self, valor_vertice):
        for vertice in self.vertices:
            if vertice.get_peso() == valor_vertice:
                return vertice
        return None

    def get_vertice_by_rotulo(self, rotulo):
        # Itera pela lista de vértices para encontrar aquele cujo rótulo corresponde ao rótulo fornecido.
        for vertice in self.vertices:
            if vertice.get_rotulo() == rotulo:
                return vertice
        # Retorna None se o vértice não existir.
        return None

    # Função para buscar uma aresta no grafo com base nos valores de início e fim dos vértices conectados por ela.
    # Parâmetros:
    # - valor_vertice_inicio: valor do vértice de início da aresta.
    # - valor_vertice_fim: valor do vértice de fim da aresta.
    # Retorno:
    # - A aresta correspondente, caso exista, ou None se não for encontrada.
    def get_aresta(self, valor_vertice_inicio, valor_vertice_fim):
        # Itera pela lista de arestas para encontrar aquela conectando os vértices especificados.
        for aresta in self.arestas:
            if (aresta.get_inicio().get_peso() == valor_vertice_inicio and
                    aresta.get_fim().get_peso() == valor_vertice_fim):
                return aresta
        # Retorna None se a aresta não existir.
        return None

    # Função para exibir a matriz de adjacência do grafo.
    # Cada célula na matriz indica se há uma conexão entre os vértices correspondentes.
    # Retorno:
    # - Não retorna valor; exibe a matriz no console.
    def mostrar_matriz_adjacencia(self):
        # Determina o número de vértices no grafo.
        tamanho = len(self.vertices)

        # Cria uma matriz quadrada inicializada com zeros.
        matriz_adjacencia = [[0] * tamanho for _ in range(tamanho)]

        # Preenche a matriz com base nas conexões das arestas.
        for aresta in self.arestas:
            inicio = aresta.get_inicio()
            fim = aresta.get_fim()

            # Determina os índices dos vértices de início e fim da aresta.
            indice_inicio = self.vertices.index(inicio)
            indice_fim = self.vertices.index(fim)

            # Marca a célula correspondente com 1 para indicar conexão.
            if indice_inicio != -1 and indice_fim != -1:
                matriz_adjacencia[indice_inicio][indice_fim] = 1

        # Exibe os cabeçalhos da matriz.
        print("  ", end="")
        for vertice in self.vertices:
            print(vertice.get_peso(), end=" ")
        print()

        # Exibe os valores da matriz.
        for i, vertice in enumerate(self.vertices):
            print(vertice.get_peso(), end=" ")
            for j in range(tamanho):
                print(matriz_adjacencia[i][j], end=" ")
            print()

    # Função para exibir a matriz de incidência do grafo.
    # Cada linha representa um vértice e cada coluna representa uma aresta.
    # Os valores na matriz indicam se o vértice é origem (-1), destino (1) ou não está conectado à aresta (0).
    # Retorno:
    # - Não retorna valor; exibe a matriz no console.
    def mostrar_matriz_incidencia(self):
        qtdVertices = len(self.vertices)  # Número de vértices.
        qtdArestas = len(self.arestas)  # Número de arestas.

        # Cria uma matriz inicializada com zeros.
        matriz_incidencia = [[0] * qtdArestas for _ in range(qtdVertices)]

        # Preenche a matriz com base nas conexões das arestas.
        for i, vertice in enumerate(self.vertices):
            for j, aresta in enumerate(self.arestas):
                if aresta.get_inicio() == vertice:
                    matriz_incidencia[i][j] = -1  # Origem da aresta.
                elif aresta.get_fim() == vertice:
                    matriz_incidencia[i][j] = 1  # Destino da aresta.

        # Exibe os cabeçalhos da matriz.
        print("   ", end="")
        for aresta in self.arestas:
            print(aresta.get_rotulo(), end=" ")
        print()

        # Exibe os valores da matriz.
        for i, vertice in enumerate(self.vertices):
            print(vertice.get_peso(), end=" ")
            for j in range(qtdArestas):
                print(matriz_incidencia[i][j], end=" ")
            print()

        # Função para exibir a lista de adjacência do grafo.
        # Cada linha representa um vértice, e cada coluna indica os vértices conectados por arestas de saída.
        # Retorno:
        # - Não retorna valor; exibe a lista de adjacência no console.

    def mostrar_lista_adjacencia(self):
        listasDeAdjacencia = []

        # Cria uma lista de adjacência para cada vértice do grafo.
        for vertice in self.vertices:
            arestasDeSaidaVertice = vertice.get_arestas_de_saida()
            listaAdjacenciaDoVertice = []

            # Adiciona os valores dos vértices de destino para cada aresta de saída.
            for aresta in arestasDeSaidaVertice:
                listaAdjacenciaDoVertice.append(aresta.get_fim().get_peso())

            listasDeAdjacencia.append(listaAdjacenciaDoVertice)

        # Exibe a lista de adjacência no console.
        for i, vertice in enumerate(self.vertices):
            print(f"Vértice {vertice.get_peso()}: {listasDeAdjacencia[i]}")

    # Função para verificar a adjacência entre dois vértices.
    # Entrada:
    # - valor_vertice_inicial: o valor do vértice de origem.
    # - valor_vertice_final: o valor do vértice de destino.
    # Retorno:
    # - Retorna True se existir uma aresta conectando os dois vértices; caso contrário, False.
    def verificar_adjacencia_entre_vertices(self, valor_vertice_inicial, valor_vertice_final):
        aresta = self.get_aresta(valor_vertice_inicial, valor_vertice_final)
        return aresta is not None

    # Função para remover uma aresta entre dois vértices.
    # Entrada:
    # - valor_vertice_inicio: o valor do vértice de origem.
    # - valor_vertice_fim: o valor do vértice de destino.
    # Retorno:
    # - Não retorna valor; remove a aresta do grafo se ela existir.
    # - Exibe uma mensagem se a aresta não for encontrada.
    def remover_aresta(self, aresta_para_remover: Aresta):

        if aresta_para_remover is not None:
            # Remove a aresta da lista geral de arestas do grafo.
            self.arestas.remove(aresta_para_remover)

            # Remove a referência da aresta dos vértices de origem e destino.
            aresta_para_remover.get_inicio().get_arestas_de_saida().remove(aresta_para_remover)
            aresta_para_remover.get_fim().get_arestas_de_entrada().remove(aresta_para_remover)
        else:
            print(f"Aresta não encontrada.")
    
    @staticmethod
    def criar_grafo_com_x_vertices():
        try:
            print('== CRIAR GRAFO COM X VÉRTICES ==')
            entrada = input("Informe quantos vértices terá o grafo OU digite 'sair' para sair: ")
            if entrada.lower() == 'sair':
                return None
            vertices = int(entrada)
            if vertices <= 0:
                print('Valor inválido. Insira um número maior que 0.')
                return None
        except ValueError:
            print('Informe um valor válido.')
            return None

        grafo = Grafo()

        for i in range(vertices):
            valor_vertice = input(f"Insira o valor do vértice {i + 1}: ")
            rotulo = input(f"Insira o rótulo do vértice {i + 1} (ou deixe vazio): ")
            try:
                peso = float(input(f"Insira o peso do vértice {i + 1} (padrão é 1): ") or 1)
            except ValueError:
                print("Peso inválido. Usando o valor padrão 1.")
                peso = 1

            grafo.adicionar_vertice(valor_vertice, rotulo if rotulo else None, peso)

        print("Grafo criado com sucesso!")
        return grafo

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

