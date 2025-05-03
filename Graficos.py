import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

class Graficos:
    def __init__(self):  
        """
        Inicializa a classe de gráficos.
        Não é necessário passar parâmetros, pois a configuração do gráfico é feita nos métodos.
        """
        pass

    def histograma(self, dados, passo_y=5000, nome="histograma discreto"):
        """
        Gera um histograma discreto baseado nos dados fornecidos.

        Args:
            dados (list[int]): Lista de dados a serem plotados.
            passo_y (int): Intervalo de unidades no eixo Y. Padrão é 5000.
            nome (str): Título do gráfico. Padrão é "histograma discreto".
        """
        contagem = Counter(dados)  # Conta a frequência de cada valor nos dados
        x = sorted(contagem.keys())  # Ordena as chaves (valores)
        y = [contagem[val] for val in x]  # Lista de frequências correspondentes

        # Configura o gráfico de barras
        plt.figure(figsize=(20, 6))
        barras = plt.bar(x, y, color='skyblue', edgecolor='black', alpha=0.8)

        # Escreve os valores no topo das barras
        for xi, yi in zip(x, y):
            if yi > 0:
                plt.text(xi, yi, str(yi), ha='center', va='bottom', fontsize=7)

        # Mostrar TODOS os valores no eixo X
        plt.xticks(x, rotation=90, fontsize=6)
        plt.yticks(range(0, max(y) + passo_y, passo_y))

        # Adiciona título e rótulos aos eixos
        plt.title(nome, fontsize=14)
        plt.xlabel('Valores', fontsize=12)
        plt.ylabel('Frequência', fontsize=12)
        plt.grid(axis='y', linestyle='--', alpha=0.4)
        plt.tight_layout()  # Ajusta o layout para não cortar elementos
        plt.show()  # Exibe o gráfico

    def linhas(self, dados):
        """
        Gera um gráfico de linha para várias trajetórias.

        Args:
            dados (list[list[int]]): Lista de listas com os dados das trajetórias a serem plotadas.
                                     Cada lista interna representa uma trajetória.
        """
        # Cores predefinidas para as linhas
        cores = ['red', 'green', 'blue', 'orange', 'purple', 'brown', 'cyan', 'magenta', 'gray', 'pink']

        # Configura o gráfico de linhas
        plt.figure(figsize=(10, 6))

        for i, caminho in enumerate(dados):
            x = list(range(1, len(caminho) + 1))  # Eixo X: etapas da trajetória
            y = caminho  # Eixo Y: valores da trajetória
            cor = cores[i % len(cores)]  # Seleção de cor cíclica para as trajetórias

            # Desenha a linha conectando os pontos
            plt.plot(x, y, color=cor, linewidth=1)

            # Marca os pontos da linha
            plt.scatter(x, y, color=cor, s=20)

            # Marca o ponto inicial de cada trajetória
            plt.scatter(x[0], y[0], color=cor, s=60)

        # Configurações dos eixos
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
        plt.xlabel("Etapas", fontsize=12)
        plt.ylabel("Valor", fontsize=12)
        plt.title("Evolução de valores por trajetória", fontsize=14)
        plt.grid(True, linestyle='--', alpha=0.3)

        # Ajuste final do layout
        plt.tight_layout()
        plt.show()  # Exibe o gráfico
