import csv
from Graficos import *  # Importa o módulo de gráficos 

class Estatisticas(Graficos):
    def __init__(self):
        # Inicializa listas que armazenam informações históricas sobre o jogo.
        self.historicoPremios = []  # Armazena os prêmios pagos ao longo do tempo
        self.valorApostasRecebidas = []  # Armazena os valores das apostas recebidas pela casa
        self.valorPremiosPagos = []  # Armazena os prêmios pagos pela casa
        self.historicoSaldosCasa = []  # Armazena o histórico de saldos da casa

        # Listas específicas para informações sobre os jogadores
        self.tiposJogadores = []  # Armazena o tipo de cada jogador (provavelmente do tipo "Jogador" ou "Bot")
        self.historicoGanhosJogador = []  # Armazena os ganhos históricos de cada jogador
        self.historicoApostasJogador = []  # Armazena as apostas históricas de cada jogador
        self.historicoSaldosJogador = []  # Armazena os saldos históricos de cada jogador
        self.rodadasVivoJogador = []  # Armazena quantas rodadas cada jogador participou
        self.historicoTotalApostajogador = []  # Armazena o total de apostas feitas por cada jogador
        pass

    def coletarDados(self, jogadores, casa, roleta):
        """
        Método para coletar e organizar os dados do jogo, incluindo informações sobre os jogadores, a casa e a roleta.
        
        Args:
            jogadores (list): Lista de objetos jogadores.
            casa (object): Objeto que representa a casa do jogo, com saldos e valores de apostas.
            roleta (object): Objeto que contém o histórico de prêmios pagos pela roleta.
        """
        
        self.jogadores = jogadores  # Armazena os jogadores
        self.casa = casa  # Armazena a casa
        self.roleta = roleta  # Armazena a roleta

        # Extende os históricos com as informações recebidas dos objetos (roleta e casa)
        self.historicoPremios.extend(self.roleta.historicoPremios)
        self.valorApostasRecebidas.extend(self.casa.valorApostasRecebidas)
        self.valorPremiosPagos.extend(self.casa.valorPremiosPagos)
        self.historicoSaldosCasa.extend(self.casa.historicoDeSaldos)

        # Loop para coletar e organizar os dados de cada jogador
        for i, k in enumerate(self.jogadores):
            # Adiciona o tipo de jogador à lista 'tiposJogadores'
            self.tiposJogadores.append([f"player{i}", k.tipo])
            

            # Adiciona os históricos de ganhos, apostas e saldos de cada jogador
            self.historicoGanhosJogador.append([f'player{i}', k.historicoGanhos])   
            self.historicoApostasJogador.append([f'player{i}', k.historicoApostas])
            self.historicoSaldosJogador.append([f'player{i}', k.historicoSaldos]) 
          

            # Adiciona a quantidade de rodadas que o jogador esteve ativo
            self.rodadasVivoJogador.append([f'player{i}', len(k.historicoApostas)])  
            

            
            valoresApostasSomados = [sum(sublista) for sublista in k.historicoApostas]  # Soma as apostas de cada jogador
            self.historicoTotalApostajogador.append([f'player{i}', valoresApostasSomados])



        # Aqui, os dados de saldos dos jogadores e da casa são combinados para exibição
        # Garantimos que a casa seja adicionada de forma que tenha o mesmo formato dos jogadores.
        # Cada jogador e a casa são apresentados como uma lista onde o primeiro valor é o nome (player0, player1, etc.), 
        # e o segundo valor é a lista de saldos históricos.
        
        print(f"saldos casa {self.historicoSaldosCasa}")
        
        
        saldos_combinados = self.historicoSaldosJogador + [['casa', self.historicoSaldosCasa]]

        # Imprime a lista combinada para depuração
        #print(saldos_combinados)  # Isso ajudará a verificar se os dados estão corretos.

        # Passa a lista combinada para o método 'linhas()' para gerar o gráfico
        self.linhas(saldos_combinados)  # Chama o método 'linhas()' para gerar o gráfico com os saldos combinados
