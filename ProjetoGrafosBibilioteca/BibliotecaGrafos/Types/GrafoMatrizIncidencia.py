from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.Aresta import Aresta
from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.Vertice import Vertice
import random

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

    def remover_aresta(self, aresta):

        if aresta not in self.arestas:
            print("A aresta não existe.")
            return

        # Encontra o índice da aresta na lista de arestas
        indice_aresta = self.arestas.index(aresta)

        # Remove a linha correspondente à aresta da matriz de incidência
        self.matriz_incidencia.pop(indice_aresta)

        # Remove a aresta da lista de arestas do grafo
        self.arestas.remove(aresta)

        # Atualiza as listas de arestas de entrada e saída dos vértices
        inicio = aresta.get_inicio()
        fim = aresta.get_fim()

        #if aresta in inicio.get_arestas_de_saida():
        #    inicio.get_arestas_de_saida().remove(aresta)
        #if aresta in fim.get_arestas_de_entrada():
        #    fim.get_arestas_de_entrada().remove(aresta)

        # Ajusta a matriz de incidência dos vértices após a remoção da aresta
        for linha in self.matriz_incidencia:
            # Remove a coluna que estava associada à aresta removida
            if len(linha) > indice_aresta:
                del linha[indice_aresta]

        # print(f"A aresta {aresta.get_rotulo()} foi removida com sucesso.")

    def verificar_adjacencia_vertices(self, v1, v2):
        # Verifica se os vértices v1 e v2 são adjacentes na matriz de incidência
        for i, linha in enumerate(self.matriz_incidencia):
            # Verifica se a aresta conecta v1 e v2
            if linha[self.vertices.index(v1)] != 0 and linha[self.vertices.index(v2)] != 0:
                return True
        return False

    def verificar_adjacencia_arestas(self, rotulo_aresta1, rotulo_aresta2):
        # Procura as arestas pelos rótulos
        aresta1 = next((aresta for aresta in self.arestas if aresta.get_rotulo() == rotulo_aresta1), None)
        aresta2 = next((aresta for aresta in self.arestas if aresta.get_rotulo() == rotulo_aresta2), None)

        # Se alguma das arestas não for encontrada, retorna False
        if not aresta1 or not aresta2:
            return False

        # Obtém os vértices de início e fim de cada aresta
        inicio1, fim1 = aresta1.get_inicio(), aresta1.get_fim()
        inicio2, fim2 = aresta2.get_inicio(), aresta2.get_fim()

        # Para grafos direcionados, verifica se existe algum vértice compartilhado
        if self.isDirecionado:
            if inicio1 == inicio2 or inicio1 == fim2 or fim1 == inicio2 or fim1 == fim2:
                return True
        else:
            # Para grafos não direcionados, verifica se compartilham vértices
            if inicio1 == inicio2 or inicio1 == fim2 or fim1 == inicio2 or fim1 == fim2:
                return True

        return False

    def verificar_existencia_aresta(self, inicio, fim):

        if inicio not in self.vertices or fim not in self.vertices:
            print("Um ou ambos os vértices não pertencem ao grafo.")
            return False

        indice_inicio = self.vertices.index(inicio)
        indice_fim = self.vertices.index(fim)

        for linha in self.matriz_incidencia:
            if self.isDirecionado:
                # Para grafo direcionado, checa se a aresta parte de 'inicio' e chega em 'fim'
                if linha[indice_inicio] == -1 and linha[indice_fim] == 1:
                    return True
            else:
                # Para grafo não direcionado, checa se há conexão entre 'inicio' e 'fim'
                if linha[indice_inicio] == 1 and linha[indice_fim] == 1:
                    return True

        return False

    def checar_grafo_vazio(self):
        """
        Verifica se o grafo é vazio.
        Um grafo é considerado vazio se não possui arestas conectando seus vértices.
        """
        # Se não houver nenhuma aresta, o grafo é vazio
        if not self.arestas:
            return True

        # Se a matriz de incidência só contém zeros, o grafo também é vazio
        for linha in self.matriz_incidencia:
            if any(valor != 0 for valor in linha):
                return False

        return True

    def checar_grafo_completo(self):
        """
        Verifica se o grafo é completo.
        Um grafo completo é aquele em que cada par de vértices distintos possui exatamente uma aresta conectando-os.
        """
        # Calcula o número de arestas que um grafo completo deveria ter
        num_vertices = len(self.vertices)

        # Um grafo com menos de 2 vértices não pode ser completo
        if num_vertices < 2:
            return False

        if self.isDirecionado:
            # Para um grafo direcionado, o número máximo de arestas é n * (n - 1)
            arestas_necessarias = num_vertices * (num_vertices - 1)
        else:
            # Para um grafo não direcionado, o número máximo de arestas é n * (n - 1) / 2
            arestas_necessarias = num_vertices * (num_vertices - 1) // 2

        # Verifica se o número atual de arestas corresponde ao necessário
        return len(self.arestas) == arestas_necessarias

    def checar_num_vertices(self):
        return len(self.vertices)

    def checar_num_arestas(self):
        return len(self.arestas)

    @staticmethod
    def criar_grafo(x, is_direcionado=False, probabilidade_aresta=0.5):
        grafo = GrafoMatrizIncidencia(is_direcionado=is_direcionado)

        # Adicionar vértices
        for i in range(1, x + 1):
            vertice = Vertice(peso_vertice=i, rotulo=f"V{i}")
            grafo.adicionar_vertice(vertice)

        for i in range(len(grafo.vertices)):
            for j in range(i + 1, len(grafo.vertices)):
                if random.random() < probabilidade_aresta:
                    inicio = grafo.vertices[i]
                    fim = grafo.vertices[j]
                    rotulo_aresta = f"A{i + 1}{j + 1}"
                    aresta = Aresta(inicio=inicio, fim=fim, rotulo=rotulo_aresta, peso=1)
                    grafo.adicionar_aresta(aresta)

        return grafo

    def copiar_grafo(self):
        novo_grafo = GrafoMatrizIncidencia(self.isDirecionado)

        vertices_map = {}

        for vertice in self.vertices:
            novo_vertice = Vertice(vertice.get_peso(), vertice.get_rotulo())
            novo_grafo.adicionar_vertice(novo_vertice)
            vertices_map[vertice] = novo_vertice

        for aresta in self.arestas:
            inicio = vertices_map[aresta.get_inicio()]
            fim = vertices_map[aresta.get_fim()]
            nova_aresta = Aresta(inicio, fim, aresta.get_rotulo(), aresta.get_peso())

            novo_grafo.adicionar_aresta(nova_aresta)

        return novo_grafo

    def verificar_grau_vertices(self):
        for vertice in self.vertices:
            vertice.grau = len(vertice.get_arestas_de_saida()) + len(vertice.get_arestas_de_entrada())

    def encontrar_pontes_naive(self):
        """
        Método naive para encontrar pontes no grafo.
        Remove cada aresta e verifica se o grafo se desconecta.
        """
        pontes = []
        for aresta in self.arestas:
            # Cria uma cópia temporária da matriz de incidência e das arestas
            matriz_backup = [linha[:] for linha in self.matriz_incidencia]
            arestas_backup = self.arestas[:]
            # Remove a aresta atual
            self.remover_aresta(aresta)
            # Verifica a conectividade
            if not self.verificar_conectividade():
                pontes.append(aresta)
            # Restaura o estado original
            self.matriz_incidencia = matriz_backup
            self.arestas = arestas_backup
        return pontes

    def verificar_conectividade(self):
        """
        Verifica se o grafo é conectado usando busca em profundidade (DFS).
        """
        if not self.vertices:
            return True  # Grafo vazio é considerado conectado
        visitados = set()

        def dfs(v):
            visitados.add(v)
            for aresta in v.get_arestas_de_saida() + v.get_arestas_de_entrada():
                vizinho = aresta.get_fim() if aresta.get_inicio() == v else aresta.get_inicio()
                if vizinho not in visitados:
                    dfs(vizinho)

        # Começa a DFS pelo primeiro vértice
        dfs(self.vertices[0])
        # Se todos os vértices foram visitados, o grafo é conectado
        return len(visitados) == len(self.vertices)

    def fleury_naive(self):
        """
        Implementação do Método de Fleury utilizando encontrar_pontes_naive.
        """
        self.verificar_grau_vertices()
        if len([v for v in self.vertices if v.grau % 2 != 0]) > 2:
            raise Exception("O grafo não possui caminho euleriano.")

        v_inicial = next((v for v in self.vertices if v.grau % 2 != 0), self.vertices[0])
        caminho = []
        arestas_restantes = self.arestas[:]

        while arestas_restantes:
            pontes = self.encontrar_pontes_naive()

            # Iterar sobre todos os vértices do grafo
            for vertice in self.vertices:  # Supondo que 'self.vertices' seja a lista de vértices no grafo
                # Pegar as arestas de saída e de entrada de cada vértice
                for aresta in vertice.get_arestas_de_saida() + vertice.get_arestas_de_entrada():
                    # Verifica se a aresta é uma ponte e se há mais de uma aresta restante
                    if aresta in pontes and len(arestas_restantes) > 1:
                        continue  # Pula as pontes quando há mais de uma aresta restante

                    caminho.append(aresta)
                    # Atualiza o vértice inicial com base na aresta
                    v_inicial = aresta.get_fim() if aresta.get_inicio() == v_inicial else aresta.get_inicio()

                    # Remove a aresta da lista de arestas restantes
                    if aresta in arestas_restantes:
                        arestas_restantes.remove(aresta)

        caminho_formatado = " / ".join(
            [f"{aresta.get_inicio().get_peso()} / {aresta.get_fim().get_peso()}" for aresta in
             caminho])
        return caminho_formatado

    def fleury_tarjan(self):
        """
        Implementação do Método de Fleury utilizando encontrar_pontes_tarjan.
        """
        self.verificar_grau_vertices()
        if len([v for v in self.vertices if v.grau % 2 != 0]) > 2:
            raise Exception("O grafo não possui caminho euleriano.")

        v_inicial = next((v for v in self.vertices if v.grau % 2 != 0), self.vertices[0])
        caminho = []
        arestas_restantes = self.arestas[:]

        while arestas_restantes:
            pontes = self.encontrar_pontes_tarjan()

            # Iterar sobre todos os vértices do grafo
            for vertice in self.vertices:  # Supondo que 'self.vertices' seja a lista de vértices no grafo
                # Pegar as arestas de entrada e de saída de cada vértice
                for aresta in vertice.get_arestas_de_saida() + vertice.get_arestas_de_entrada():
                    # Verifica se a aresta é uma ponte e se há mais de uma aresta restante
                    if aresta in pontes and len(arestas_restantes) > 1:
                        continue  # Pula as pontes quando há mais de uma aresta restante

                    caminho.append(aresta)
                    # Atualiza o vértice inicial com base na aresta
                    v_inicial = aresta.get_fim() if aresta.get_inicio() == v_inicial else aresta.get_inicio()

                    # Remove a aresta da lista de arestas restantes
                    if aresta in arestas_restantes:
                        arestas_restantes.remove(aresta)

            break

        caminho_formatado = " / ".join(
            [f"{aresta.get_inicio().get_peso()} / {aresta.get_fim().get_peso()}" for aresta in
             caminho])
        return caminho_formatado

    @staticmethod
    def criar_grafo_euleriano(x, is_direcionado=False):
        """
        Cria um grafo euleriano com x vértices e arestas suficientes para garantir
        que todos os vértices tenham grau par.
        """
        grafo = GrafoMatrizIncidencia(is_direcionado=is_direcionado)

        # Adicionar vértices
        for i in range(1, x + 1):
            vertice = Vertice(peso_vertice=i, rotulo=f"V{i}")
            grafo.adicionar_vertice(vertice)

        # Adicionar arestas para garantir que o grafo seja euleriano (grau par)
        for i in range(len(grafo.vertices)):
            for j in range(i + 1, len(grafo.vertices)):
                inicio = grafo.vertices[i]
                fim = grafo.vertices[j]

                # Criação de uma aresta, garantindo que todos os vértices terão grau par
                rotulo_aresta = f"A{i + 1}{j + 1}"
                aresta = Aresta(inicio=inicio, fim=fim, rotulo=rotulo_aresta, peso=1)
                grafo.adicionar_aresta(aresta)

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
