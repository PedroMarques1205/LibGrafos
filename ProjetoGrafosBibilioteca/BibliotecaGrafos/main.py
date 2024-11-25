from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.core.Aresta import Aresta

from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.core.Grafo import Grafo
from ProjetoGrafosBibilioteca.BibliotecaGrafos.Types.core.Vertice import Vertice
import sys
import time

grafo = None

def criar_grafo_grande(quantidade_vertices):
    grafo = Grafo("grafogrande", False)

    vertices = []
    for i in range(quantidade_vertices):
        vertice = Vertice(peso_vertice=str(i), rotulo=f"V{i}")
        vertices.append(vertice)
        grafo.adicionarVertice(vertice)

    for i in range(quantidade_vertices - 1):
        grafo.adicionarAresta(Aresta(vertices[i], vertices[i + 1], rotulo=f"e{i}", peso=1))

    grafo.adicionarAresta(
        Aresta(vertices[quantidade_vertices - 1], vertices[0], rotulo=f"e{quantidade_vertices - 1}", peso=1))

    return grafo

def menu():
    global grafo
    while True:
        print("\nEscolha as opções abaixo:")
        print("1. Criar/manipular Grafo")
        print("2. Realizar Teste de tempo algoritimo Fleury (Parte 2)")
        print("3. Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            while True:
                print("\n\n\n\n\n\n\nEscolha as opções abaixo:")
                print("1. Criar novo Grafo vazio")
                print("2. Adicionar novo vértice")
                print("3. Adicionar Aresta")
                print("4. Mostrar Matriz Adjacência")
                print("5. Mostrar Lista Adjacência")
                print("6. Mostrar Matriz Incidência")
                print("7. Exportar grafo para .graphml")
                print("8. Indentificar pontes")
                print("9. Indentificar articulações")
                print("10. Obter quantidade de componentes fortemente conexos utilizando kosaraju")
                print("11. Cria grafo com X vértices")
                print("12. Remover Vértice")
                print("13. Remover Aresta")
                print("14. Ponderar vértice")
                print("15. Renomear vértice")
                print("16. Ponderar aresta")
                print("17. Verificar adjacência entre vértices")
                print("18. Verificar adjacência entre arestas")
                print("19. Verificar existência de aresta")
                print("20. Mostrar quantidade de vértices e arestas")
                print("21. Verificar se o grafo é vazio e completo")
                print("22. Verificar tipo de conexão do grafo")
                print("25. Voltar")

                opcaoNovoGrafo = int(input("Escolha uma opção: "))
                if opcaoNovoGrafo == 1:
                    id_grafo = input("Digite o ID do grafo: ")
                    is_direcionado = input("O grafo é direcionado? (s/n): ").lower() == 's'
                    grafo = Grafo(id_grafo, is_direcionado)
                    print(f"Grafo {id_grafo} criado com sucesso!")
                elif opcaoNovoGrafo == 2:
                    if grafo is None:
                        print("Primeiro crie um grafo!")
                    else:
                        rotulo = input("Digite o rótulo do vértice: ")
                        vertice = Vertice(rotulo=rotulo, peso_vertice=rotulo)
                        grafo.adicionarVertice(vertice)
                        print(f"Vértice {rotulo} adicionado com sucesso!")
                elif opcaoNovoGrafo == 3:
                    if grafo is None:
                        print("Primeiro crie um grafo!")
                    else:
                        rotulo_inicio = input("Digite o rótulo do vértice de início: ")
                        rotulo_fim = input("Digite o rótulo do vértice de fim: ")
                        peso = float(input("Digite o peso da aresta: "))
                        aresta = Aresta(grafo.get_vertice(rotulo_inicio), grafo.get_vertice(rotulo_fim),
                                        rotulo=f"{rotulo_inicio}-{rotulo_fim}", peso=peso)
                        grafo.adicionarAresta(aresta)
                        print(f"Aresta de {rotulo_inicio} para {rotulo_fim} adicionada com sucesso!")
                elif opcaoNovoGrafo == 4:
                    if grafo is None:
                        print("Primeiro crie um grafo!")
                    else:
                        grafo.printar_matriz_adjacencia()
                elif opcaoNovoGrafo == 5:
                    if grafo is None:
                        print("Primeiro crie um grafo!")
                    else:
                        grafo.printar_lista_adjacencia()
                elif opcaoNovoGrafo == 6:
                    if grafo is None:
                        print("Primeiro crie um grafo!")
                    else:
                        grafo.printar_matriz_indicencia()
                elif opcaoNovoGrafo == 7:
                    if grafo is None:
                        print("Primeiro crie um grafo!")
                    else:
                        grafo.criar_arquivo_grafo_graphml()
                elif opcaoNovoGrafo == 8:
                    if grafo is None:
                        print("Primeiro crie um grafo!")
                    else:
                        pontes = grafo.checar_pontes_tarjan()
                        rotulos = [ponte.get_rotulo() for ponte in pontes]
                        print(f"Pontes: {', '.join(rotulos)}")
                elif opcaoNovoGrafo == 9:
                    if grafo is None:
                        print("Primeiro crie um grafo!")
                    else:
                        articulacoes= grafo.checar_articulacoes()
                        rotulos = [articulacao.get_rotulo() for articulacao in articulacoes]
                        print(f"Articulações: {', '.join(rotulos)}")
                elif opcaoNovoGrafo == 10:
                    print(f"Num componentes fortemente conexos :{grafo.checar_quantidade_de_componentes_fortemente_conexos()}")
                elif opcaoNovoGrafo == 11:
                        x = int(input("Digite o valor de X: "))
                        is_direcionado = input("O grafo é direcionado? (s/n): ").lower() == 's'
                        grafo = Grafo.criar_grafo_com_x_vertices(x,is_direcionado)
                        print("Grafo criado com sucesso")
                elif opcaoNovoGrafo == 12:
                    if grafo is None:
                        print("Primeiro crie um grafo!")
                    else:
                        rotulo_remover = input("Digite o rótulo do vértice a ser removido: ")
                        grafo.removerVertice(rotulo_remover)
                        print(f"Vértice {rotulo_remover} removido com sucesso!")

                elif opcaoNovoGrafo == 13:
                    if grafo is None:
                        print("Primeiro crie um grafo!")
                    else:
                        rotulo_inicio = input("Digite o rótulo do vértice de início: ")
                        rotulo_fim = input("Digite o rótulo do vértice de fim: ")
                        grafo.removerAresta(rotulo_inicio, rotulo_fim)
                        print(f"Aresta entre {rotulo_inicio} e {rotulo_fim} removida com sucesso!")
                elif opcaoNovoGrafo == 14:
                    if grafo is None:
                        print("Primeiro crie um grafo!")
                    else:
                        rotulo_vertice = input("Digite o rótulo do vértice para ponderar: ")
                        ponderacao = float(input("Digite a ponderação do vértice: "))
                        grafo.ponderar_vertice(rotulo_vertice, ponderacao)
                        print(f"Vértice {rotulo_vertice} ponderado com sucesso!")
                elif opcaoNovoGrafo == 15:
                    if grafo is None:
                        print("Primeiro crie um grafo!")
                    else:
                        rotulo_atual = input("Digite o rótulo atual do vértice: ")
                        rotulo_novo = input("Digite o novo rótulo do vértice: ")
                        grafo.rotular_vertice(rotulo_atual, rotulo_novo)
                        print(f"Vértice {rotulo_atual} renomeado para {rotulo_novo} com sucesso!")
                elif opcaoNovoGrafo == 16:
                    if grafo is None:
                        print("Primeiro crie um grafo!")
                    else:
                        rotulo_aresta = input("Digite o rótulo da aresta para ponderar: ")
                        peso = float(input("Digite o peso da aresta: "))
                        grafo.ponderar_aresta(rotulo_aresta, peso)
                        print(f"Aresta {rotulo_aresta} ponderada com sucesso!")
                elif opcaoNovoGrafo == 17:
                    if grafo is None:
                        print("Primeiro crie um grafo!")
                    else:
                        vertice1 = input("Digite o rótulo do primeiro vértice: ")
                        vertice2 = input("Digite o rótulo do segundo vértice: ")
                        if grafo.checar_adjacencia_entre_vertices(vertice1, vertice2):
                            print(f"Os vértices {vertice1} e {vertice2} são adjacentes.")
                        else:
                            print(f"Os vértices {vertice1} e {vertice2} não são adjacentes.")
                elif opcaoNovoGrafo == 18:
                    if grafo is None:
                        print("Primeiro crie um grafo!")
                    else:
                        aresta1 = input("Digite o rótulo da primeira aresta: ")
                        aresta2 = input("Digite o rótulo da segunda aresta: ")
                        if grafo.checar_adjacencia_entre_arestas(aresta1, aresta2):
                            print(f"As arestas {aresta1} e {aresta2} são adjacentes.")
                        else:
                            print(f"As arestas {aresta1} e {aresta2} não são adjacentes.")
                elif opcaoNovoGrafo == 19:
                    if grafo is None:
                        print("Primeiro crie um grafo!")
                    else:
                        aresta = input("Digite o rótulo da aresta para verificar existência: ")
                        if grafo.checar_existencia_de_aresta(aresta):
                            print(f"A aresta {aresta} existe.")
                        else:
                            print(f"A aresta {aresta} não existe.")
                elif opcaoNovoGrafo == 20:
                    if grafo is None:
                        print("Primeiro crie um grafo!")
                    else:
                        print(f"Quantidade de vértices: {len(grafo.vertices)}")
                        print(f"Quantidade de arestas: {len(grafo.arestas)}")
                elif opcaoNovoGrafo == 21:
                    if grafo is None:
                        print("Primeiro crie um grafo!")
                    else:
                        if grafo.checar_se_grafo_vazio():
                            print("O grafo está vazio.")
                        else:
                            print("O grafo não está vazio.")
                        if grafo.checar_se_grafo_completo():
                            print("O grafo é completo.")
                        else:
                            print("O grafo não é completo.")
                elif opcaoNovoGrafo == 22:
                    if grafo is None:
                        print("Primeiro crie um grafo!")
                    else:
                        if grafo.checar_se_simplesmente_conexo():
                            print("O grafo é simplesmente conexo.")
                        elif grafo.checar_se_fortemente_conexo():
                            print("O grafo é fortemente conexo.")
                        else:
                            print("O grafo não é semifortemente conexo.")
                elif opcaoNovoGrafo == 25:
                    break

        elif opcao == 2:
            if grafo is None:
                print("Primeiro crie um grafo!")
            else:
                print("Teste de Desempenho (Parte 2) em andamento...")
                start_time = time.time()
                print(f"Grafo construído em {time.time() - start_time:.5f} segundos.")

                print("Executando Fleury com Tarjan...")
                start_time = time.time()
                resultado_tarjan = grafo.fleury_tarjan()
                print(f"Algoritmo Fleury com Tarjan executado em {time.time() - start_time:.5f} segundos.")

                print("Executando Fleury com Naive...")
                start_time = time.time()
                resultado_naive = grafo.fleury_naive()
                print(f"Algoritmo Fleury com Naive executado em {time.time() - start_time:.5f} segundos.")

        elif opcao == 3:
            print("Saindo.......")
            break



if __name__ == "__main__":
    menu()










