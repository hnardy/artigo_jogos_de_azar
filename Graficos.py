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

    def histograma(self, dados, passo_y=5, nome="histograma discreto"):
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
        plt.close()



    def linhas(self, dados, titulo="Evolução de valores por trajetória", xlabel="Etapas", ylabel="Valor"):
        """
        Gera um gráfico de linha para uma ou várias trajetórias, com valores exibidos acima de cada ponto.

        Args:
            dados (list[list[int]] | list[int] | list[tuple[str, list[int]]]): Lista de listas com os dados das trajetórias,
                uma única lista de valores (trajetória única), ou uma lista de tuplas/listas com rótulo e trajetória.
            titulo (str): Título do gráfico.
            xlabel (str): Rótulo do eixo X.
            ylabel (str): Rótulo do eixo Y.
        """
        # Se for uma trajetória simples
        if isinstance(dados[0], (int, float)):
            dados = [dados]
            nomes = [f"Traj 1"]
        # Se o primeiro item for uma string, assume que é nome + dados
        elif isinstance(dados[0], list) and isinstance(dados[0][0], str):
            nomes = [linha[0] for linha in dados]
            dados = [linha[1] for linha in dados]
        else:
            nomes = [f"Traj {i+1}" for i in range(len(dados))]

        # Verificação de integridade
        if not all(isinstance(traj, list) for traj in dados):
            raise ValueError("Cada trajetória deve ser uma lista de números.")
        if not all(isinstance(val, (int, float)) for traj in dados for val in traj):
            raise ValueError("Os valores das trajetórias devem ser inteiros ou floats.")

        cores = ['red', 'green', 'blue', 'orange', 'purple', 'brown', 'cyan', 'magenta', 'gray', 'pink']

        plt.figure(figsize=(10, 6))

        for i, caminho in enumerate(dados):
            x = list(range(1, len(caminho) + 1))
            y = caminho
            cor = cores[i % len(cores)]

            plt.plot(x, y, color=cor, linewidth=1, label=nomes[i])
            plt.scatter(x, y, color=cor, s=20)
            plt.scatter(x[0], y[0], color=cor, s=60)  # Ponto inicial

            # Exibe os valores acima de cada ponto
            for xi, yi in zip(x, y):
                plt.text(xi, yi + 5, str(yi), ha='center', va='bottom', fontsize=8)

        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
        plt.xlabel(xlabel, fontsize=12)
        plt.ylabel(ylabel, fontsize=12)
        plt.title(titulo, fontsize=14)
        plt.grid(True, linestyle='--', alpha=0.3)
        plt.legend(fontsize=8)
        plt.tight_layout()
        plt.show()
        plt.close()
