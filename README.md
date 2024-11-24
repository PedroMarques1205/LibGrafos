Trabalho de Grafos

Este repositório contém o trabalho acadêmico de **Manipulação de Grafos**, para a disciplina de Grafos do curso Engenharia de Software, PUC MG.

---

## 👩🏻‍💻 Alunos

- Pedro Henrique Marques de Oliveira
- Juliana Parreiras Guimarães da Cunha

---

## 🫡 Professor

- Leonardo Vilela Cardoso

---

## 📝 Estrutura do Trabalho

O trabalho é dividido em três partes.

### Parte 1: Biblioteca de Manipulação de Grafos

Desenvolver uma biblioteca para manipulação de grafos, que deve conter:

#### Representações:
- Grafo utilizando **Matriz de Adjacência**
- Grafo utilizando **Matriz de Incidência**
- Grafo utilizando **Lista de Adjacência**

#### Manipulações Básicas:
- Criação de um grafo com **X vértices** (especificado pelo usuário)
- Criação e remoção de arestas
- Ponderação e rotulação de vértices e arestas
- Checagem de adjacência entre vértices e arestas
- Verificação de existência de arestas
- Contagem de vértices e arestas
- Verificação de grafo **vazio** ou **completo**
- Verificação de **conectividade** (simples, semi-fortemente e fortemente conexo)
- Checagem de componentes fortemente conexos com o **Algoritmo de Kosaraju**
- Identificação de **ponte** e **articulação** no grafo

### Parte 2: Identificação de Pontes e Caminho Euleriano

Implementar dois métodos para identificação de **pontes** em um grafo:
1. **Método Naive**: Testa a conectividade do grafo após cada remoção de aresta (utilizando busca em largura ou profundidade).
2. **Método de Tarjan**: Baseado no artigo fornecido.

Após implementar ambos os métodos, encontrar um **caminho euleriano** usando o **Algoritmo de Fleury**. Testar as duas estratégias com grafos aleatórios de tamanhos 100, 1000, 10000 e 100000 vértices, comparando os tempos de execução.

### Parte 3: Exportação de Grafos para Gephi

Implementar a funcionalidade de **ler** e **salvar** grafos em formatos compatíveis com o software de visualização de grafos **Gephi**. Os formatos suportados são: GEXF, GDF, GML, GraphML, Pajek NET, GraphViz DOT, CSV, UCINET DL, Tulip TPL, Netdraw VNA, Spreadsheet. Gerar ilustrações dos grafos criados utilizando o Gephi.

---

