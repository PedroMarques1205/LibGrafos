class GrafoMatrizAdjascencia:
    def __init__(self):
        self.isDirecionado = False
        self.vertices = []  
        self.matrizAdjacencia = []  
        self.arestas = {}  

    def adicionar_vertice(self, newVertice):
        self.vertices.append(newVertice)
        for linha in self.matrizAdjacencia:
            linha.append(0)  
        self.matrizAdjacencia.append([0] * len(self.vertices))
        
    def criar_arestas(self, rotuloVertice1: str, rotuloVertice2: str, peso: int = 1):
        indice1 = next((i for i, vertice in enumerate(self.vertices) if vertice.rotulo == rotuloVertice1), None)
        indice2 = next((i for i, vertice in enumerate(self.vertices) if vertice.rotulo == rotuloVertice2), None)

        if indice1 is None or indice2 is None:
            raise ValueError("Um ou ambos os vértices não foram encontrados.")

        self.matrizAdjacencia[indice1][indice2] = peso
        self.arestas[(rotuloVertice1, rotuloVertice2)] = peso
        
        if not self.isDirecionado:
            self.matrizAdjacencia[indice2][indice1] = peso
            self.arestas[(rotuloVertice2, rotuloVertice1)] = peso

    def remover_arestas(self, rotuloVertice1: str, rotuloVertice2: str):
        indice1 = next((i for i, vertice in enumerate(self.vertices) if vertice.rotulo == rotuloVertice1), None)
        indice2 = next((i for i, vertice in enumerate(self.vertices) if vertice.rotulo == rotuloVertice2), None)

        if indice1 is None or indice2 is None:
            raise ValueError("Um ou ambos os vértices não foram encontrados.")

        self.matrizAdjacencia[indice1][indice2] = 0
        del self.arestas[(rotuloVertice1, rotuloVertice2)]
        
        if not self.isDirecionado:
            self.matrizAdjacencia[indice2][indice1] = 0
            del self.arestas[(rotuloVertice2, rotuloVertice1)]

    def rotular_vertice(self, indice: int, novo_rotulo: str):
        if indice < 0 or indice >= len(self.vertices):
            raise ValueError("Índice de vértice inválido.")
        self.vertices[indice].rotulo = novo_rotulo 
    
    def ponderar_aresta(self, rotuloVertice1: str, rotuloVertice2: str, novo_peso: int):
        indice1 = next((i for i, vertice in enumerate(self.vertices) if vertice.rotulo == rotuloVertice1), None)
        indice2 = next((i for i, vertice in enumerate(self.vertices) if vertice.rotulo == rotuloVertice2), None)

        if indice1 is None or indice2 is None:
            raise ValueError("Um ou ambos os vértices não foram encontrados.")

        self.matrizAdjacencia[indice1][indice2] = novo_peso
        self.arestas[(rotuloVertice1, rotuloVertice2)] = novo_peso

        if not self.isDirecionado:
            self.matrizAdjacencia[indice2][indice1] = novo_peso
            self.arestas[(rotuloVertice2, rotuloVertice1)] = novo_peso

    def checar_adjacencia_vertices(self, rotuloVertice1: str, rotuloVertice2: str) -> bool:
        indice1 = next((i for i, vertice in enumerate(self.vertices) if vertice.rotulo == rotuloVertice1), None)
        indice2 = next((i for i, vertice in enumerate(self.vertices) if vertice.rotulo == rotuloVertice2), None)

        if indice1 is None or indice2 is None:
            raise ValueError("Um ou ambos os vértices não foram encontrados.")

        return self.matrizAdjacencia[indice1][indice2] != 0

    def checar_adjacencia_arestas(self, rotuloVertice1: str, rotuloVertice2: str, rotuloVertice3: str, rotuloVertice4: str) -> bool:
        return self.checar_adjacencia_vertices(rotuloVertice1, rotuloVertice2) and self.checar_adjacencia_vertices(rotuloVertice3, rotuloVertice4)

    def checar_existencia_aresta(self, rotuloVertice1: str, rotuloVertice2: str) -> bool:
        return self.checar_adjacencia_vertices(rotuloVertice1, rotuloVertice2)

    def quantidade_vertices(self) -> int:
        return len(self.vertices)

    def quantidade_arestas(self) -> int:
        return len(self.arestas)

    def grafo_vazio(self) -> bool:
        return len(self.vertices) == 0

    def grafo_completo(self) -> bool: #revisar essa aqui
        if self.grafo_vazio():
            return False
        num_vertices = len(self.vertices)
        for i in range(num_vertices):
            for j in range(num_vertices):
                if i != j and self.matrizAdjacencia[i][j] == 0:
                    return False
        return True
