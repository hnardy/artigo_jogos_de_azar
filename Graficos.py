import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

class Graficos:
    def __init__(self):  
        pass


class Graficos:
    def __init__(self):  
        pass

    import matplotlib.pyplot as plt
from collections import Counter

class Graficos:
    def __init__(self):  
        pass

    def histograma(self, dados, passo_y=5000,nome = "histograma discreto"):
        contagem = Counter(dados)
        x = sorted(contagem.keys())
        y = [contagem[val] for val in x]

        plt.figure(figsize=(20, 6))
        barras = plt.bar(x, y, color='skyblue', edgecolor='black', alpha=0.8)

        # Escreve os valores no topo das barras
        for xi, yi in zip(x, y):
            if yi > 0:
                plt.text(xi, yi, str(yi), ha='center', va='bottom', fontsize=7)

        # Mostrar TODOS os valores no eixo X
        plt.xticks(x, rotation=90, fontsize=6)
        plt.yticks(range(0, max(y)+passo_y, passo_y))

        plt.title(nome, fontsize=14)
        plt.xlabel('Valores', fontsize=12)
        plt.ylabel('Frequência', fontsize=12)
        plt.grid(axis='y', linestyle='--', alpha=0.4)
        plt.tight_layout()
        plt.show()





   

    def linhas(self,dados):
    
        cores = ['red', 'green', 'blue', 'orange', 'purple', 'brown', 'cyan', 'magenta', 'gray', 'pink']

        plt.figure(figsize=(10, 6))

        for i, caminho in enumerate(dados):
            x = list(range(1, len(caminho)+1))
            y = caminho
            cor = cores[i % len(cores)]

            # Linha conectando os pontos
            plt.plot(x, y, color=cor, linewidth=1)

            # Pontos marcados
            plt.scatter(x, y, color=cor, s=20)

            # Ponto inicial destacado
            plt.scatter(x[0], y[0], color=cor, s=60)

        # Configurações dos eixos
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
        plt.xlabel("Etapas", fontsize=12)
        plt.ylabel("Valor", fontsize=12)
        plt.title("Evolução de valores por trajetória", fontsize=14)
        plt.grid(True, linestyle='--', alpha=0.3)

        plt.tight_layout()
        plt.show()
