import matplotlib.pyplot as plt
from collections import Counter

class Estatisticas:
    def __init__(self):
        """
        Inicializa a classe de estatísticas.
        Contém dicionários e listas para armazenar os dados coletados de cada iteração do jogo.
        """
        self.historicoPremios = []  # Armazena todos os prêmios sorteados
        self.historicoDeSorteios = []  # Armazena os números sorteados
        self.historicoGanhos = []  # Armazena os ganhos dos jogadores
        self.historicoApostas = []  # Armazena as apostas feitas
        self.historicoSaldos = []  # Armazena os saldos dos jogadores
        self.rodadasAteFalha = []  # Armazena a quantidade de rodadas até a falha dos jogadores
        self.valorApostasRecebidas = []  # Armazena o total de apostas recebidas pela casa
        self.valorPremiosPagos = []  # Armazena o total de prêmios pagos pela casa
        self.historicoJogadoresAtivos = []  # Armazena os jogadores ativos em cada rodada

    def coletarDados(self, dados):
        """
        Coleta os dados das outras classes e armazena em suas respectivas listas.
        
        Args:
            dados (dict): Dicionário contendo os dados a serem armazenados. As chaves devem ser os nomes
                          dos dados (ex.: 'historicoPremios', 'historicoGanhos', etc.)
        """
        self.historicoPremios.extend(dados['historicoPremios'])
        self.historicoDeSorteios.extend(dados['historicoDeSorteios'])
        self.historicoGanhos.extend(dados['historicoGanhos'])
        self.historicoApostas.extend(dados['historicoApostas'])
        self.historicoSaldos.extend(dados['historicoSaldos'])
        self.rodadasAteFalha.extend(dados['rodadasAteFalha'])
        self.valorApostasRecebidas.extend(dados['valorApostasRecebidas'])
        self.valorPremiosPagos.extend(dados['valorPremiosPagos'])
        self.historicoJogadoresAtivos.extend(dados['historicoJogadoresAtivos'])

    def gerarRelatorio(self):
        """
        Gera um relatório com estatísticas simples dos dados coletados, como total de prêmios pagos,
        saldo médio, etc.
        """
        totalApostasRecebidas = sum(self.valorApostasRecebidas)
        totalPremiosPagos = sum(self.valorPremiosPagos)
        saldoMedioJogadores = sum(self.historicoSaldos) / len(self.historicoSaldos) if self.historicoSaldos else 0
        rodadasMediaFalha = sum(self.rodadasAteFalha) / len(self.rodadasAteFalha) if self.rodadasAteFalha else 0

        print(f"Relatório de Estatísticas:")
        print(f"Total de Apostas Recebidas pela Casa: {totalApostasRecebidas}")
        print(f"Total de Prêmios Pagos pela Casa: {totalPremiosPagos}")
        print(f"Saldo Médio dos Jogadores: {saldoMedioJogadores:.2f}")
        print(f"Média de Rodadas até Falha dos Jogadores: {rodadasMediaFalha:.2f}")

    def gerarGraficoSaldos(self):
        """
        Gera um gráfico de linha da evolução dos saldos dos jogadores ao longo das rodadas.
        """
        if self.historicoSaldos:
            plt.plot(self.historicoSaldos)
            plt.title("Evolução dos Saldos dos Jogadores")
            plt.xlabel("Rodadas")
            plt.ylabel("Saldo")
            plt.grid(True)
            plt.show()
        else:
            print("Nenhum dado de saldo disponível para gerar gráfico.")

    def gerarGraficoApostas(self):
        """
        Gera um gráfico de barras para mostrar a distribuição das apostas feitas nas várias rodadas.
        """
        if self.historicoApostas:
            apostas_totais = [sum(aposta) for aposta in self.historicoApostas]
            plt.hist(apostas_totais, bins=20, color='blue', edgecolor='black', alpha=0.7)
            plt.title("Distribuição das Apostas")
            plt.xlabel("Valor Apostado")
            plt.ylabel("Frequência")
            plt.grid(True)
            plt.show()
        else:
            print("Nenhum dado de apostas disponível para gerar gráfico.")

    def gerarGraficoPremios(self):
        """
        Gera um gráfico de barras para mostrar a distribuição dos prêmios sorteados.
        """
        if self.historicoPremios:
            premios_totais = Counter(self.historicoPremios)
            x = list(premios_totais.keys())
            y = list(premios_totais.values())
            plt.bar(x, y, color='green', edgecolor='black', alpha=0.7)
            plt.title("Distribuição dos Prêmios Sorteados")
            plt.xlabel("Prêmios")
            plt.ylabel("Frequência")
            plt.grid(True)
            plt.show()
        else:
            print("Nenhum dado de prêmios disponível para gerar gráfico.")


