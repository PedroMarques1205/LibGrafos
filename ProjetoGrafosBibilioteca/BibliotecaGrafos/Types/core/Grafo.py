import networkx as nx

from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.core.Aresta import Aresta
from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.representations.GrafoListaAdjacencia import GrafoListaAdjacencia
from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.representations.GrafoMatrizAdjascencia import GrafoMatrizAdjascencia
from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.representations.GrafoMatrizIncidencia import GrafoMatrizIncidencia
from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.core.Vertice import Vertice

class Grafo:
    def __init__(self, id: str, isDirecionado: bool):
        self.vertices = []
        self.arestas = []
        self.isDirecionado = isDirecionado
        self.listaAdjacencia = GrafoListaAdjacencia(self.isDirecionado)
        self.matrizIncidencia = GrafoMatrizIncidencia(self.isDirecionado)
        self.matrizAdjacencia = GrafoMatrizAdjascencia(self.isDirecionado)
        self.id = id

    # MÉTODOS DA PARTE 1

    def printar_matriz_adjacencia(self):
        if self.checar_se_grafo_vazio():
            print("O grafo está vazio.")
            return

        self.matrizAdjacencia.printar_matriz_adjacencia()

    def printar_lista_adjacencia(self):
        if self.checar_se_grafo_vazio():
            print("O grafo está vazio.")
            return

        self.listaAdjacencia.mostrar_lista_adjacencia()

    def printar_matriz_indicencia(self):
        if self.checar_se_grafo_vazio():
            print("O grafo está vazio.")
            return

        self.matrizIncidencia.exibir_matriz()

    def adicionarVertice(self, vertice: Vertice):

        self.vertices.append(vertice)
        self.listaAdjacencia.adicionar_vertice(vertice)
        self.matrizIncidencia.adicionar_vertice(vertice)
        self.matrizAdjacencia.adicionar_vertice(vertice)

    def removerVertice(self, rotulo_vertice: str):
        vertice = self.get_vertice(rotulo_vertice)

        if vertice == None:
            raise ValueError('Você tentou remover um vértice que não existe.')

        for aresta in vertice.get_arestas_de_saida():
            self.removerAresta(aresta.get_inicio().get_rotulo(), aresta.get_fim().get_rotulo())
        for aresta in vertice.get_arestas_de_entrada():
            self.removerAresta(aresta.get_inicio().get_rotulo(), aresta.get_fim().get_rotulo())

        self.listaAdjacencia.remover_vertice(vertice)
        self.matrizAdjacencia.remover_vertice(vertice)
        self.matrizIncidencia.remover_vertice(vertice)


    def adicionarAresta(self, aresta: Aresta):

        for a in self.arestas:
            if a.get_rotulo() == aresta.get_rotulo():
                raise ValueError(f"Erro: O vértice com o rótulo {aresta.get_rotulo()} já existe.")

        v1 = aresta.get_inicio()
        v2 = aresta.get_fim()

        self.arestas.append(aresta)
        self.listaAdjacencia.adicionar_aresta(aresta)
        self.matrizAdjacencia.adicionar_aresta(aresta)
        self.matrizIncidencia.adicionar_aresta(aresta)

    def removerAresta(self, rotulo_inicio: str, rotulo_fim: str):
        isFound = False

        for aresta in self.arestas:
            if aresta.get_inicio().rotulo == rotulo_inicio and aresta.get_fim().rotulo == rotulo_fim:
                self.listaAdjacencia.remover_aresta(aresta)
                self.matrizAdjacencia.remover_aresta(aresta)
                self.matrizIncidencia.remover_aresta(aresta)
                self.arestas.remove(aresta)

                aresta.get_inicio().remover_aresta_de_saida(aresta)
                aresta.get_fim().remover_aresta_de_entrada(aresta)

                if not self.isDirecionado:
                    aresta.get_inicio().remover_aresta_de_entrada(aresta)
                    aresta.get_fim().remover_aresta_de_saida(aresta)
                isFound = True
                break

        if not isFound:
            raise ValueError("Tentou remover uma aresta que não existe.")

    @staticmethod
    def criar_grafo_com_x_vertices(quantidade_vertices, isDirecionado: bool):
        grafo = Grafo(f"grafo{quantidade_vertices}Vertices", isDirecionado)

        vertices = []
        for i in range(quantidade_vertices):
            vertice = Vertice(peso_vertice=str(i), rotulo=f"V{i}")
            vertices.append(vertice)
            grafo.adicionarVertice(vertice)

        for i in range(quantidade_vertices):
            for j in range(i + 1, quantidade_vertices):
                grafo.adicionarAresta(Aresta(vertices[i], vertices[j], rotulo=f"e{i}-{j}", peso=1))

                if not isDirecionado:
                    grafo.adicionarAresta(Aresta(vertices[j], vertices[i], rotulo=f"e{j}-{i}", peso=1))

        return grafo

    def ponderar_vertice(self, rotulo_vertice: str, ponderacao_vertice):
        for v in self.vertices:
            if v.get_rotulo() == rotulo_vertice:
                v.set_ponderacao(ponderacao_vertice)
                self.listaAdjacencia.set_ponderacao_vertice(rotulo_vertice, ponderacao_vertice)
                self.matrizAdjacencia.set_ponderacao_vertice(rotulo_vertice, ponderacao_vertice)
                self.matrizIncidencia.set_ponderacao_vertice(rotulo_vertice, ponderacao_vertice)
                break

    def rotular_vertice(self, rotulo_atual_vertice: str, rotulo_novo_vertice: str):
        for v in self.vertices:
            if v.get_rotulo() == rotulo_atual_vertice:
                v.set_rotulo(rotulo_novo_vertice)
                self.listaAdjacencia.set_rotulaco_vertice(rotulo_atual_vertice, rotulo_novo_vertice)
                self.matrizAdjacencia.set_rotulaco_vertice(rotulo_atual_vertice, rotulo_novo_vertice)
                self.matrizIncidencia.set_rotulaco_vertice(rotulo_atual_vertice, rotulo_novo_vertice)
                break

    def ponderar_aresta(self, rotulo_aresta: str, peso_aresta):
        for a in self.arestas:
            if a.get_rotulo() == rotulo_aresta:
                a.set_peso(peso_aresta)
                self.listaAdjacencia.set_ponderacao_aresta(rotulo_aresta, peso_aresta)
                self.matrizAdjacencia.set_ponderacao_aresta(rotulo_aresta, peso_aresta)
                self.matrizIncidencia.set_ponderacao_aresta(rotulo_aresta, peso_aresta)
                break

    def rotular_aresta(self, rotulo_atual_aresta: str, rotulo_novo_aresta: str):
        for a in self.arestas:
            if a.get_rotulo() == rotulo_atual_aresta:
                a.set_rotulo(rotulo_novo_aresta)
                self.listaAdjacencia.set_rotulacao_aresta(rotulo_atual_aresta, rotulo_novo_aresta)
                self.matrizAdjacencia.set_rotulacao_aresta(rotulo_atual_aresta, rotulo_novo_aresta)
                self.matrizIncidencia.set_rotulacao_aresta(rotulo_atual_aresta, rotulo_novo_aresta)

    def checar_adjacencia_entre_vertices(self, rotulo_vertice_um: str, rotulo_vertice_dois: str):
        return self.matrizAdjacencia.checar_adjacencia_vertices(rotulo_vertice_um, rotulo_vertice_dois)

    def checar_adjacencia_entre_arestas(self, rotulo_vertice_um: str, rotulo_vertice_dois: str):
        return self.matrizIncidencia.verificar_adjacencia_arestas(rotulo_vertice_um, rotulo_vertice_dois)

    def checar_existencia_de_aresta(self, rotulo: str):
        return any(a.get_rotulo() == rotulo for a in self.arestas)

    def checar_existencia_de_vertice(self, rotulo: str):
        return any(v.get_rotulo() == rotulo for v in self.vertices)

    def checar_quantidade_de_vertices(self):
        return len(self.vertices)

    def checar_quantidade_de_arestas(self):
        return len(self.arestas)

    def checar_se_grafo_vazio(self):
        return len(self.vertices) == 0

    def checar_se_grafo_completo(self):
        for vertice in self.vertices:
            if len(vertice.get_arestas_de_saida()) != len(self.vertices) - 1:
                return False

        return True

    def checar_se_fortemente_conexo(self):
        def dfs(vertice, visitados, arestas_saida=True):
            visitados.add(vertice)
            arestas = vertice.get_arestas_de_saida() if arestas_saida else vertice.get_arestas_de_entrada()
            for aresta in arestas:
                proximo_vertice = aresta.get_fim() if arestas_saida else aresta.get_inicio()
                if proximo_vertice not in visitados:
                    dfs(proximo_vertice, visitados, arestas_saida)

        if not self.vertices:
            return True

        visitados = set()
        dfs(self.vertices[0], visitados, True)
        if len(visitados) != len(self.vertices):
            return False

        visitados.clear()
        dfs(self.vertices[0], visitados, False)
        return len(visitados) == len(self.vertices)

    def checar_se_semifortemente_conexo(self):
        if not self.vertices:
            return True

        visitados = set()

        def dfs(v):
            visitados.add(v)
            for aresta in v.get_arestas_de_saida():
                if aresta.get_fim() not in visitados:
                    dfs(aresta.get_fim())
            for aresta in v.get_arestas_de_entrada():
                if aresta.get_inicio() not in visitados:
                    dfs(aresta.get_inicio())

        dfs(self.vertices[0])

        return len(visitados) == len(self.vertices)

    def checar_se_simplesmente_conexo(self):
        visitados = set()
        tem_ciclo = [False]

        def dfs(vertice, parent):
            visitados.add(vertice)
            for aresta in vertice.get_arestas_de_saida():
                proximo_vertice = aresta.get_fim()
                if proximo_vertice not in visitados:
                    dfs(proximo_vertice, vertice)
                elif proximo_vertice != parent:
                    tem_ciclo[0] = True

        if not self.vertices:
            return True

        dfs(self.vertices[0], None)

        return len(visitados) == len(self.vertices) and not tem_ciclo[0]

    def verificar_conectividade(self):
        if not self.vertices:
            return True
        visitados = set()

        def dfs(v):
            visitados.add(v)
            for aresta in v.get_arestas_de_saida() + v.get_arestas_de_entrada():
                vizinho = aresta.get_fim() if aresta.get_inicio() == v else aresta.get_inicio()
                if vizinho not in visitados:
                    dfs(vizinho)

        dfs(self.vertices[0])

        return len(visitados) == len(self.vertices)

    def checar_quantidade_de_componentes_fortemente_conexos(self):
        ordem_finalizacao = []

        visitados = set()

        def dfs_primeira_passagem(vertice):
            visitados.add(vertice)

            for aresta in vertice.get_arestas_de_saida():
                proximo_vertice = aresta.get_fim()

                if proximo_vertice not in visitados:
                    dfs_primeira_passagem(proximo_vertice)

            ordem_finalizacao.append(vertice)

        def dfs_segunda_passagem(vertice, componente):

            visitados.add(vertice)

            componente.append(vertice)

            for aresta in vertice.get_arestas_de_entrada():
                proximo_vertice = aresta.get_inicio()
                if proximo_vertice not in visitados:
                    dfs_segunda_passagem(proximo_vertice, componente)

        for vertice in self.vertices:
            if vertice not in visitados:
                dfs_primeira_passagem(vertice)

        visitados.clear()

        componentes = []

        while ordem_finalizacao:
            vertice = ordem_finalizacao.pop()

            if vertice not in visitados:
                componente = []
                dfs_segunda_passagem(vertice, componente)
                componentes.append(componente)

        return len(componentes)

    def checar_ponte(self):
        return self.checar_pontes_tarjan()

    def checar_articulacoes(self):
        tempo = [0]
        discovery_time = {}
        low_time = {}
        parent = {}
        articulacoes = set()

        for vertice in self.vertices:
            discovery_time[vertice] = -1
            low_time[vertice] = -1
            parent[vertice] = None

        def dfs_iterativo(vertice_inicial):
            stack = [(vertice_inicial, iter(vertice_inicial.get_arestas_de_saida()))]
            discovery_time[vertice_inicial] = low_time[vertice_inicial] = tempo[0]
            tempo[0] += 1
            filhos = 0

            while stack:
                vertice_atual, vizinhos = stack[-1]
                try:
                    aresta = next(vizinhos)
                    vizinho = aresta.get_fim() if aresta.get_inicio() == vertice_atual else aresta.get_inicio()

                    if discovery_time[vizinho] == -1:
                        parent[vizinho] = vertice_atual
                        discovery_time[vizinho] = low_time[vizinho] = tempo[0]
                        tempo[0] += 1
                        filhos += 1
                        stack.append((vizinho, iter(vizinho.get_arestas_de_saida())))

                    elif vizinho != parent[vertice_atual]:
                        low_time[vertice_atual] = min(low_time[vertice_atual], discovery_time[vizinho])

                except StopIteration:
                    stack.pop()
                    if parent[vertice_atual] is not None:
                        low_time[parent[vertice_atual]] = min(low_time[parent[vertice_atual]], low_time[vertice_atual])

                        if (parent[vertice_atual] is None and filhos > 1) or (
                                parent[vertice_atual] is not None and low_time[vertice_atual] >= discovery_time[
                            parent[vertice_atual]]):
                            articulacoes.add(vertice_atual)

        for vertice in self.vertices:
            if discovery_time[vertice] == -1:
                dfs_iterativo(vertice)

        return articulacoes

    # MÉTODOS DA PARTE 2

    def checar_pontes_naive(self):
        pontes = []
        for aresta in self.arestas:
            u = aresta.get_inicio().get_rotulo()  
            v = aresta.get_fim().get_rotulo()  

            self.removerAresta(u, v)

            if not self.checar_se_simplesmente_conexo():  
                pontes.append((u, v))  

            self.adicionarAresta(aresta)

        return pontes

    def checar_pontes_tarjan(self):
        tempo = [0]
        discovery_time = {}
        low_time = {}
        parent = {}
        pontes = []

        for vertice in self.vertices:
            discovery_time[vertice] = -1
            low_time[vertice] = -1
            parent[vertice] = None

        def dfs_iterativo(vertice_inicial):
            global aresta
            stack = [(vertice_inicial, iter(vertice_inicial.get_arestas_de_saida() + vertice_inicial.get_arestas_de_entrada()))]
            discovery_time[vertice_inicial] = low_time[vertice_inicial] = tempo[0]
            tempo[0] += 1

            while stack:
                vertice_atual, vizinhos = stack[-1]
                try:
                    aresta = next(vizinhos)
                    vizinho = aresta.get_fim() if aresta.get_inicio() == vertice_atual else aresta.get_inicio()

                    if discovery_time[vizinho] == -1:
                        parent[vizinho] = vertice_atual
                        discovery_time[vizinho] = low_time[vizinho] = tempo[0]
                        tempo[0] += 1
                        stack.append((vizinho, iter(vizinho.get_arestas_de_saida() + vizinho.get_arestas_de_entrada())))
                    elif vizinho != parent[vertice_atual]:
                        low_time[vertice_atual] = min(low_time[vertice_atual], discovery_time[vizinho])
                except StopIteration:
                    stack.pop()
                    if parent[vertice_atual] is not None:
                        low_time[parent[vertice_atual]] = min(low_time[parent[vertice_atual]], low_time[vertice_atual])
                        if low_time[vertice_atual] > discovery_time[parent[vertice_atual]]:
                            pontes.append(aresta)

        for vertice in self.vertices:
            if discovery_time[vertice] == -1:
                dfs_iterativo(vertice)

        return pontes

    def fleury_naive(self):
        return self.matrizIncidencia.fleury_naive()

    def fleury_tarjan(self):
        self.verificar_grau_vertices()
        if len([v for v in self.vertices if v.grau % 2 != 0]) > 2:
            raise Exception("O grafo não possui caminho euleriano.")

        v_inicial = next((v for v in self.vertices if v.grau % 2 != 0), self.vertices[0])
        caminho = []
        arestas_restantes = self.arestas[:]

        while arestas_restantes:
            pontes = self.checar_pontes_tarjan()

            for vertice in self.vertices:
                for aresta in vertice.get_arestas_de_saida() + vertice.get_arestas_de_entrada():
                    if aresta in pontes and len(arestas_restantes) > 1:
                        continue

                    caminho.append(aresta)
                    v_inicial = aresta.get_fim() if aresta.get_inicio() == v_inicial else aresta.get_inicio()

                    if aresta in arestas_restantes:
                        arestas_restantes.remove(aresta)

            break

        caminho_formatado = " / ".join(
            [f"{aresta.get_inicio().get_peso()} / {aresta.get_fim().get_peso()}" for aresta in caminho])
        return caminho_formatado

    def verificar_grau_vertices(self):
        for vertice in self.vertices:
            vertice.grau = len(vertice.get_arestas_de_saida()) + len(vertice.get_arestas_de_entrada())

    # MÉTODOS DA PARTE 3 #

    def criar_arquivo_grafo_graphml(self):
        grafo_networkx = self.para_networkx()
        nx.write_graphml(grafo_networkx, self.id + ".graphml")
        nx.write_gexf(grafo_networkx, self.id + ".graphml")

    def para_networkx(self):
        grafo = nx.DiGraph() if self.isDirecionado else nx.Graph()

        for vertice in self.vertices:
            grafo.add_node(vertice.get_rotulo())

        for aresta in self.arestas:
            grafo.add_edge(aresta.get_inicio().get_rotulo(), aresta.get_fim().get_rotulo(), weight=aresta.get_peso())

        return grafo

    # MÉTODOS AUXILIARES

    def get_vertice(self, rotulo: str):
        return next((v for v in self.vertices if v.get_rotulo() == rotulo), None)

