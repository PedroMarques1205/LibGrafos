from operator import truediv

from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.Aresta import Aresta
from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.Vertice import Vertice


# CLASSE GRAFO#
class Grafo:
    def __init__(self):
        self.vertices = []
        self.arestas = []

    # Função para adicionar um novo vértice ao grafo, recebe como parâmetros: valor_vertice, rotulo e o peso do mesmo.
    def adicionar_vertice(self, valor_vertice, rotulo=None, peso=1):
        if self.get_vertice(valor_vertice) is None:
            self.vertices.append(Vertice(valor_vertice, rotulo, peso))

    # Função para adicionar uma aresta entre dois vértices no grafo.
    # Parâmetros:
    # - inicio_aresta: o valor do vértice de início da aresta.
    # - fim_aresta: o valor do vértice de fim da aresta.
    # - rotulo (opcional): um rótulo descritivo para a aresta. Se não fornecido, será gerado automaticamente como "inicio_aresta-fim_aresta".
    # - peso (opcional): peso da aresta. O valor padrão é 1.
    def adicionar_aresta(self, inicio_aresta, fim_aresta, rotulo=None, peso=1):
        # Obtém os vértices correspondentes aos valores de início e fim.
        vertice_inicio = self.get_vertice(inicio_aresta)
        vertice_fim = self.get_vertice(fim_aresta)

        # Se nenhum rótulo foi fornecido, cria um rótulo padrão usando os valores dos vértices.
        if rotulo is None:
            rotulo = f"{inicio_aresta}-{fim_aresta}"

        # Adiciona a aresta se ambos os vértices existirem no grafo.
        if vertice_inicio is not None and vertice_fim is not None:
            # Cria uma nova aresta e a adiciona à lista de arestas do grafo.
            nova_aresta = Aresta(vertice_inicio, vertice_fim, rotulo, peso)
            self.arestas.append(nova_aresta)

            # Atualiza as referências de saída e entrada dos vértices conectados.
            vertice_inicio.adicionar_aresta_de_saida(nova_aresta)
            vertice_fim.adicionar_aresta_de_entrada(nova_aresta)

    # Função para buscar um vértice no grafo com base no valor do vértice.
    # Parâmetros:
    # - valor_vertice: o valor do vértice a ser procurado.
    # Retorno:
    # - O vértice correspondente, caso exista, ou None se não for encontrado.
    def get_vertice(self, valor_vertice):
        # Itera pela lista de vértices para encontrar aquele cujo valor corresponde ao valor fornecido.
        for vertice in self.vertices:
            if vertice.get_valor_vertice() == valor_vertice:
                return vertice
        # Retorna None se o vértice não existir.
        return None

    # Função para buscar um vértice no grafo com base no rótulo do vértice.
    # Parâmetros:
    # - rotulo: o rótulo do vértice a ser procurado.
    # Retorno:
    # - O vértice correspondente, caso exista, ou None se não for encontrado.
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
            if (aresta.get_inicio().get_valor_vertice() == valor_vertice_inicio and
                    aresta.get_fim().get_valor_vertice() == valor_vertice_fim):
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
            print(vertice.get_valor_vertice(), end=" ")
        print()

        # Exibe os valores da matriz.
        for i, vertice in enumerate(self.vertices):
            print(vertice.get_valor_vertice(), end=" ")
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
            print(vertice.get_valor_vertice(), end=" ")
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
                listaAdjacenciaDoVertice.append(aresta.get_fim().get_valor_vertice())

            listasDeAdjacencia.append(listaAdjacenciaDoVertice)

        # Exibe a lista de adjacência no console.
        for i, vertice in enumerate(self.vertices):
            print(f"Vértice {vertice.get_valor_vertice()}: {listasDeAdjacencia[i]}")

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
    def remover_aresta(self, valor_vertice_inicio, valor_vertice_fim):
        aresta_para_remover = self.get_aresta(valor_vertice_inicio, valor_vertice_fim)

        if aresta_para_remover is not None:
            # Remove a aresta da lista geral de arestas do grafo.
            self.arestas.remove(aresta_para_remover)

            # Remove a referência da aresta dos vértices de origem e destino.
            aresta_para_remover.get_inicio().get_arestas_de_saida().remove(aresta_para_remover)
            aresta_para_remover.get_fim().get_arestas_de_entrada().remove(aresta_para_remover)
        else:
            print(f"Aresta de {valor_vertice_inicio} para {valor_vertice_fim} não encontrada.")

    # Função para verificar se o grafo é simplesmente conexo.
    # Um grafo é simplesmente conexo se for conectado (todos os vértices são alcançáveis a partir de qualquer outro).
    # Retorno:
    # - Retorna True se o grafo for simplesmente conexo; caso contrário, False.
    def eh_simplesmente_conexo(self):
        visitados = set()

        # Função de busca em profundidade (DFS) para visitar vértices conectados.
        def dfs(vertice):
            visitados.add(vertice)
            for aresta in vertice.get_arestas_de_saida():
                proximo_vertice = aresta.get_fim()
                if proximo_vertice not in visitados:
                    dfs(proximo_vertice)

        if not self.vertices:
            return True

        dfs(self.vertices[0])

        return len(visitados) == len(self.vertices)

    # Função para verificar se o grafo é semi-fortemente conexo.
    # Um grafo é semi-fortemente conexo se sua versão não direcionada for simplesmente conexa.
    # Retorno:
    # - Retorna True se o grafo for semi-fortemente conexo; caso contrário, False.
    def eh_semi_fortemente_conexo(self):
        grafo_nao_direcionado = Grafo()

        # Cria uma cópia do grafo original como não direcionado.
        for vertice in self.vertices:
            grafo_nao_direcionado.adicionar_vertice(vertice.get_valor_vertice())
        for aresta in self.arestas:
            grafo_nao_direcionado.adicionar_aresta(
                aresta.get_inicio().get_valor_vertice(),
                aresta.get_fim().get_valor_vertice()
            )
            grafo_nao_direcionado.adicionar_aresta(
                aresta.get_fim().get_valor_vertice(),
                aresta.get_inicio().get_valor_vertice()
            )

        return grafo_nao_direcionado.eh_simplesmente_conexo()

    # Função para verificar se o grafo é fortemente conexo.
    # Um grafo é fortemente conexo se todos os vértices forem alcançáveis a partir de qualquer outro, considerando a direção das arestas.
    # Retorno:
    # - Retorna True se o grafo for fortemente conexo; caso contrário, False.
    def eh_fortemente_conexo(self):
        # Função de busca em profundidade (DFS) com direção especificada.
        def dfs(vertice, visitados, arestas_saida=True):
            visitados.add(vertice)
            arestas = vertice.get_arestas_de_saida() if arestas_saida else vertice.get_arestas_de_entrada()
            for aresta in arestas:
                proximo_vertice = aresta.get_fim() if arestas_saida else aresta.get_inicio()
                if proximo_vertice not in visitados:
                    dfs(proximo_vertice, visitados, arestas_saida)

        if not self.vertices:
            return True # Um grafo vazio é considerado fortemente conexo.

        # Verifica se todos os vértices são alcançáveis na direção das arestas.
        visitados = set()
        dfs(self.vertices[0], visitados, True)
        if len(visitados) != len(self.vertices):
            return False

        # Verifica se todos os vértices são alcançáveis na direção inversa das arestas.
        visitados.clear()
        dfs(self.vertices[0], visitados, False)
        return len(visitados) == len(self.vertices)

    # Método para contar o número de componentes fortemente conexos em um grafo dirigido.
    # Utiliza o algoritmo de Kosaraju, que consiste em duas passagens de DFS.
    def contar_componentes_fortemente_conexos(self):
        # Lista para armazenar a ordem de finalização dos vértices na primeira DFS.
        ordem_finalizacao = []

        # Conjunto para marcar os vértices visitados durante as DFS.
        visitados = set()

        # Primeira passagem da DFS: constrói a ordem de finalização.
        # Função auxiliar para realizar a DFS na primeira passagem.
        # Objetivo: Ordenar os vértices de acordo com o tempo de finalização.
        def dfs_primeira_passagem(vertice):
            # Marca o vértice como visitado.
            visitados.add(vertice)

            # Explora todas as arestas de saída do vértice atual.
            for aresta in vertice.get_arestas_de_saida():
                # Obtém o vértice de destino da aresta.
                proximo_vertice = aresta.get_fim()

                # Se o vértice de destino ainda não foi visitado, faz a DFS nele.
                if proximo_vertice not in visitados:
                    dfs_primeira_passagem(proximo_vertice)

            # Após explorar todas as arestas do vértice, adiciona-o à ordem de finalização.
            ordem_finalizacao.append(vertice)

        # Segunda passagem da DFS: encontra os componentes fortemente conexos.
        # Função auxiliar para realizar a DFS na segunda passagem.
        # Objetivo: Explorar componentes conexos no grafo transposto.
        def dfs_segunda_passagem(vertice, componente):

            # Marca o vértice como visitado.
            visitados.add(vertice)

            # Adiciona o vértice atual ao componente fortemente conexo em construção.
            componente.append(vertice)

            # Explora todas as arestas de entrada do vértice atual (grafo transposto).
            for aresta in vertice.get_arestas_de_entrada():
                # Obtém o vértice de origem da aresta.
                proximo_vertice = aresta.get_inicio()
                # Se o vértice de origem ainda não foi visitado, faz a DFS nele.
                if proximo_vertice not in visitados:
                    dfs_segunda_passagem(proximo_vertice, componente)

        # Executa a primeira passagem de DFS em todos os vértices do grafo.
        for vertice in self.vertices:
            # Se o vértice ainda não foi visitado, inicia a DFS a partir dele.
            if vertice not in visitados:
                dfs_primeira_passagem(vertice)

        # Limpa o conjunto de vértices visitados para reutilizá-lo na segunda passagem.
        visitados.clear()

        # Lista para armazenar todos os componentes fortemente conexos.
        componentes = []

        # Processa os vértices na ordem inversa de finalização.
        # Essa ordem garante que exploramos componentes no grafo transposto.
        while ordem_finalizacao:
            # Remove o último vértice da ordem de finalização.
            vertice = ordem_finalizacao.pop()

            # Se o vértice ainda não foi visitado, ele pertence a um novo componente.
            if vertice not in visitados:
                # Lista para armazenar o componente atual.
                componente = []
                # Inicia a DFS para explorar o componente conectado no grafo transposto.
                dfs_segunda_passagem(vertice, componente)
                # Adiciona o componente encontrado à lista de componentes.
                componentes.append(componente)

        # Retorna o número de componentes fortemente conexos encontrados.
        return len(componentes)
    
    # Método para criar um grafo com uma quantidade definida de vértices 
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

