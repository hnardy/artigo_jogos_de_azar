import csv
import matplotlib.pyplot as plt
from collections import Counter

class Estatisticas:
    def __init__(self):
        """
        Inicializa a classe de estatísticas.
        Contém listas para armazenar os dados coletados de cada iteração do jogo.
        """
        self.historicoPremios = []           # Todos os prêmios sorteados
        self.historicoDeSorteios = []       # Números sorteados
        self.historicoGanhos = []           # Ganhos individuais dos jogadores
        self.historicoApostas = []          # Apostas feitas pelos jogadores
        self.historicoSaldos = {}           # Saldos por tipo de apostador: {tipo: [saldos...]}
        self.rodadasAteFalha = {}           # Rodadas até falha por tipo de apostador: {tipo: [rodadas...]}
        self.valorApostasRecebidas = []     # Valores totais apostados
        self.valorPremiosPagos = []         # Valores totais pagos em prêmios
        self.historicoJogadoresAtivos = []  # Quantidade de jogadores ativos por rodada

    def coletarDados(self, dados, jogadores):
        """
        Coleta os dados das outras classes e armazena nas listas.

        Args:
            dados (dict): Dicionário com chaves:
                'historicoPremios', 'historicoDeSorteios', 'historicoGanhos',
                'historicoApostas', 'valorApostasRecebidas', 'valorPremiosPagos',
                'historicoJogadoresAtivos'
            jogadores (list): lista de objetos de jogador utilizados nesta iteração.
        """
        self.historicoPremios.extend(dados['historicoPremios'])
        self.historicoDeSorteios.extend(dados['historicoDeSorteios'])
        self.historicoGanhos.extend(dados['historicoGanhos'])
        self.historicoApostas.extend(dados['historicoApostas'])
        self.valorApostasRecebidas.extend(dados['valorApostasRecebidas'])
        self.valorPremiosPagos.extend(dados['valorPremiosPagos'])
        self.historicoJogadoresAtivos.extend(dados['historicoJogadoresAtivos'])

        # Agrupa saldos e rodadas por tipo de apostador
        for j in jogadores:
            tipo = j.tipo
            # Inicializa listas se não existirem
            self.historicoSaldos.setdefault(tipo, []).append(j.saldo)
            self.rodadasAteFalha.setdefault(tipo, []).append(j.rodadasAteFalha())

    def gerarRelatorio(self):
        """
        Gera um relatório resumido das estatísticas coletadas.
        """
        total_apostas = sum(self.valorApostasRecebidas)
        total_premios = sum(self.valorPremiosPagos)
        saldo_geral = sum([sum(lst) for lst in self.historicoSaldos.values()])
        num_entradas = sum([len(lst) for lst in self.historicoSaldos.values()])
        media_saldo = saldo_geral/num_entradas if num_entradas else 0

        print("===== RELATÓRIO GERAL =====")
        print(f"Total Apostas Recebidas: {total_apostas}")
        print(f"Total Prêmios Pagos: {total_premios}")
        print(f"Saldo Médio dos Jogadores: {media_saldo:.2f}")

        # Ranking de quem foi mais longe
        distancias = {tipo: max(rodadas) for tipo, rodadas in self.rodadasAteFalha.items()}
        ranking = sorted(distancias.items(), key=lambda x: x[1], reverse=True)
        print("\nRanking de Apostadores por Maior Número de Rodadas: ")
        for tipo, rodadas in ranking:
            print(f" - {tipo}: {rodadas} rodadas")
        print("===========================\n")

    def gerarGraficoBarras(self, data_dict, titulo, xlabel, ylabel):
        """
        Gera um gráfico de barras legível, exibindo o valor de cada barra no topo.

        Args:
            data_dict (dict): mapeia categorias a valores numéricos
            titulo (str): título do gráfico
            xlabel (str): rótulo do eixo X
            ylabel (str): rótulo do eixo Y
        """
        categorias = list(data_dict.keys())
        valores = list(data_dict.values())

        plt.figure(figsize=(10, 6))
        barras = plt.bar(categorias, valores, edgecolor='black', alpha=0.8)
        plt.title(titulo, fontsize=14)
        plt.xlabel(xlabel, fontsize=12)
        plt.ylabel(ylabel, fontsize=12)
        plt.grid(axis='y', linestyle='--', alpha=0.4)

        # Escrever valor de cada barra no topo
        for bar in barras:
            altura = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, altura, f'{altura}',
                     ha='center', va='bottom', fontsize=10)

        plt.tight_layout()
        plt.show()

    def gerarGraficoSaldosPorTipo(self):
        """
        Gera um gráfico de barras mostrando o saldo médio final por tipo de apostador.
        """
        media_saldos = {tipo: (sum(lst)/len(lst)) for tipo, lst in self.historicoSaldos.items()}
        self.gerarGraficoBarras(media_saldos,
                                "Saldo Médio Final por Tipo de Apostador",
                                "Tipo de Apostador", "Saldo Médio")

    def gerarGraficoRodadasPorTipo(self):
        """
        Gera um gráfico de barras com a maior quantidade de rodadas alcançadas por cada tipo de apostador.
        """
        max_rodadas = {tipo: max(lst) for tipo, lst in self.rodadasAteFalha.items()}
        self.gerarGraficoBarras(max_rodadas,
                                "Maior Rodadas por Tipo de Apostador",
                                "Tipo de Apostador", "Rodadas")

    def gerarGraficoDistribuicaoPremios(self):
        """
        Gera um histograma discreto da distribuição de prêmios sorteados.
        """
        self.gerarGraficoBarras(Counter(self.historicoPremios),
                                "Distribuição de Prêmios Sorteados",
                                "Prêmio", "Frequência")

    def gerarGraficoDistribuicaoApostas(self):
        """
        Gera um histograma da distribuição dos valores apostados.
        """
        apostas_tot = [sum(ap) for ap in self.historicoApostas]
        self.histograma(apostas_tot, passo_y=max(apostas_tot)//10 or 1,
                        nome="Distribuição de Valores Apostados")

    def histograma(self, dados, passo_y=5000, nome="histograma discreto"):
        """
        Gera um histograma discreto baseado nos dados fornecidos.

        Args:
            dados (list[int]): Lista de dados a serem plotados.
            passo_y (int): Intervalo de unidades no eixo Y.
            nome (str): Título do gráfico.
        """
        contagem = Counter(dados)
        x = sorted(contagem.keys())
        y = [contagem[val] for val in x]

        plt.figure(figsize=(12, 6))
        barras = plt.bar(x, y, color='skyblue', edgecolor='black', alpha=0.8)

        # Escrever valores no topo das barras
        for xi, yi in zip(x, y):
            plt.text(xi, yi, str(yi), ha='center', va='bottom', fontsize=8)

        plt.xticks(x, rotation=90)
        plt.yticks(range(0, max(y) + passo_y, passo_y))
        plt.title(nome)
        plt.xlabel('Valor')
        plt.ylabel('Frequência')
        plt.grid(axis='y', linestyle='--', alpha=0.4)
        plt.tight_layout()
        plt.show()

    def exportarCSV(self, nome_arquivo='estatisticas_completo.csv'):
        """
        Exporta todas as estatísticas coletadas para um CSV por rodada,
        incluindo dados gerais, sorteios e saldos por tipo de apostador.

        Args:
            nome_arquivo (str): Nome do arquivo CSV a ser gerado.
        """
        num_rodadas = len(self.valorApostasRecebidas)

        # Descobre todos os tipos de apostadores
        tipos_apostadores = sorted(set(self.historicoSaldos.keys()))

        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            # Cabeçalho
            cabecalho = [
                "Rodada",
                "Apostas Recebidas",
                "Prêmios Pagos",
                "Jogadores Ativos",
                "Total Apostado",
                "Total Ganhado",
                "Prêmio Sorteado",
                "Número Sorteado"
            ]

            # Acrescenta colunas por tipo de apostador
            for tipo in tipos_apostadores:
                cabecalho.append(f"Saldo Médio ({tipo})")
            for tipo in tipos_apostadores:
                cabecalho.append(f"Rodadas até Falha ({tipo})")

            writer.writerow(cabecalho)

            for i in range(num_rodadas):
                total_apostado = sum(self.historicoApostas[i]) if i < len(self.historicoApostas) else 0
                total_ganho = self.historicoGanhos[i] if i < len(self.historicoGanhos) else 0


                premio = self.historicoPremios[i] if i < len(self.historicoPremios) else ''
                sorteio = self.historicoDeSorteios[i] if i < len(self.historicoDeSorteios) else ''

                linha = [
                    i + 1,
                    self.valorApostasRecebidas[i] if i < len(self.valorApostasRecebidas) else 0,
                    self.valorPremiosPagos[i] if i < len(self.valorPremiosPagos) else 0,
                    self.historicoJogadoresAtivos[i] if i < len(self.historicoJogadoresAtivos) else 0,
                    total_apostado,
                    total_ganho,
                    premio,
                    sorteio
                ]

                # Saldos por tipo até a rodada atual
                for tipo in tipos_apostadores:
                    saldos = self.historicoSaldos.get(tipo, [])
                    media = sum(saldos[:i+1]) / (i+1) if len(saldos) > i else ''
                    linha.append(round(media, 2) if media != '' else '')

                # Rodadas até falha por tipo
                for tipo in tipos_apostadores:
                    rodadas = self.rodadasAteFalha.get(tipo, [])
                    media = sum(rodadas[:i+1]) / (i+1) if len(rodadas) > i else ''
                    linha.append(round(media, 2) if media != '' else '')

                writer.writerow(linha)

        print(f"Arquivo CSV COMPLETO exportado como '{nome_arquivo}'.")
