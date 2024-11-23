class Menu:
    def __init__(self):
        self.grafo = None
        self.tipo_grafo = None

    def mostrar_menu(self):
        while True:
            print("\nBem-vindo ao Gerenciador de Grafos!")
            print("1. Criar Grafo")
            print("2. Operar no Grafo")
            print("3. Sair")
            opcao = input("\nEscolha uma opção: ")

            if opcao == "1":
                self.escolher_tipo_grafo()
            elif opcao == "2":
                if not self.grafo:
                    print("Crie um grafo primeiro!")
                else:
                    self.menu_operacoes()
            elif opcao == "3":
                print("Saindo do programa.")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def escolher_tipo_grafo(self):
        print("\nEscolha o tipo de representação do grafo:")
        print("1. Matriz de Adjacência")
        print("2. Lista de Adjacência")
        print("3. Matriz de Incidência")
        tipo = input("\nDigite sua escolha: ")

        if tipo not in ["1", "2", "3"]:
            print("Opção inválida. Retornando ao menu principal.")
            return

        self.tipo_grafo = tipo
        num_vertices = int(input("Digite o número de vértices do grafo: "))

        if tipo == "1":
            print("Crie um grafo primeiro!")
        elif tipo == "2":
            print("Crie um grafo primeiro!")
        elif tipo == "3":
            print("Crie um grafo primeiro!")

