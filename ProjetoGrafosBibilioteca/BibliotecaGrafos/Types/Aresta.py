class Aresta:
    def __init__(self, inicio, fim, rotulo, peso):
        self.inicio = inicio
        self.fim = fim
        self.rotulo = rotulo
        self.peso = peso

    def get_inicio(self):
        return self.inicio

    def set_inicio(self, inicio):
        self.inicio = inicio

    def get_fim(self):
        return self.fim

    def set_fim(self, fim):
        self.fim = fim

    def get_rotulo(self):
        return self.rotulo

    def set_rotulo(self, rotulo):
        self.rotulo = rotulo

    def get_peso(self):
        return self.peso

    def set_peso(self, peso):
        self.peso = peso

