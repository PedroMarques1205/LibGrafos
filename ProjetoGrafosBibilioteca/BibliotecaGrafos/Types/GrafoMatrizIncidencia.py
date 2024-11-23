from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.Aresta import Aresta
from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.Vertice import Vertice


class GrafoMatrizIncidencia:
    def __init__(self, isDirecionado=False):
        self.matriz_incidencia = []
        self.vertices = vertices
        self.arestas = []
        self.isDirecionado = isDirecionado

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

        if self.isDirecionado:
            # Grafo direcionado: A aresta vai de 'inicio' para 'fim'
            nova_linha[self.vertices.index(inicio)] = -1  # Saída do vértice inicial
            nova_linha[self.vertices.index(fim)] = 1  # Entrada no vértice final
        else:
            # Grafo não direcionado: A aresta conecta 'inicio' <-> 'fim'
            nova_linha[self.vertices.index(inicio)] = 1  # Saída do vértice inicial
            nova_linha[self.vertices.index(fim)] = 1  # Entrada no vértice final

        self.matriz_incidencia.append(nova_linha)

    def exibir_matriz(self):
        print("Matriz de Incidência:")

        # Exibe o cabeçalho com os rótulos das arestas
        arestas_rotulos = [a.get_rotulo() for a in self.arestas]
        print("       ", "  ".join(arestas_rotulos))  # Espaçamento inicial para alinhar com os rótulos dos vértices

        # Exibe cada linha da matriz de incidência com o rótulo do vértice
        for i, vertice in enumerate(self.vertices):
            vertice_rotulo = vertice.get_rotulo() if vertice.get_rotulo() is not None else str(
                vertice.get_valor_vertice())
            linha = [self.matriz_incidencia[j][i] for j in range(len(self.matriz_incidencia))]
            print(f"{vertice_rotulo: <7} ", "  ".join(map(str, linha)))

    def remover_aresta(self, aresta):
        # Verifica se a aresta existe na lista de arestas
        if aresta not in self.arestas:
            print("A aresta não existe.")
            return

        # Encontra o índice da aresta na lista de arestas
        indice_aresta = self.arestas.index(aresta)

        # Remove a linha correspondente à aresta da matriz de incidência
        self.matriz_incidencia.pop(indice_aresta)

        # Remove a aresta da lista de arestas
        self.arestas.remove(aresta)

        # Ajusta a matriz de incidência dos vértices após a remoção
        for linha in self.matriz_incidencia:
            # Remove a coluna que estava associada à aresta removida
            linha.pop(indice_aresta)

        print(f"A aresta {aresta.get_rotulo()} foi removida com sucesso.")

    def verificar_adjacencia_vertices(self, v1, v2):
        # Verifica se os vértices v1 e v2 são adjacentes na matriz de incidência
        for i, linha in enumerate(self.matriz_incidencia):
            # Verifica se a aresta conecta v1 e v2
            if linha[self.vertices.index(v1)] != 0 and linha[self.vertices.index(v2)] != 0:
                return True
        return False

    def verificar_adjacencia_arestas(self, aresta1, aresta2):
        # Verifica se duas arestas são adjacentes
        # Encontra os vértices associados a cada aresta
        inicio1, fim1 = aresta1.get_inicio(), aresta1.get_fim()
        inicio2, fim2 = aresta2.get_inicio(), aresta2.get_fim()

        # Para grafos direcionados, verifica se existe algum vértice compartilhado
        if self.isDirecionado:
            # Checa se algum vértice das arestas são iguais
            if inicio1 == inicio2 or inicio1 == fim2 or fim1 == inicio2 or fim1 == fim2:
                return True
        else:
            # Para grafos não direcionados, basta checar se a aresta compartilha vértices
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
    def criar_grafo(x, is_direcionado=False):

        grafo = GrafoMatrizIncidencia(is_direcionado=is_direcionado)

        # Adicionar vértices
        for i in range(1, x + 1):
            vertice = Vertice(valor_vertice=i, rotulo=f"V{i}")
            grafo.adicionar_vertice(vertice)

        # Adicionar arestas entre os vértices
        for i in range(len(grafo.vertices)):
            for j in range(i + 1, len(grafo.vertices)):
                inicio = grafo.vertices[i]
                fim = grafo.vertices[j]
                rotulo_aresta = f"A{i + 1}{j + 1}"
                aresta = Aresta(inicio=inicio, fim=fim, rotulo=rotulo_aresta,peso=1)
                grafo.adicionar_aresta(aresta)

        return grafo