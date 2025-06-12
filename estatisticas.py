import csv
import os
from datetime import datetime
from Graficos import *  # Importa o módulo de gráficos 
import mysql.connector
from mysql.connector import Error


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



    def GraficoSaldosCasaJogador(self):

        if self.historicoSaldosJogador == []:
            print("sem dados")    
            return
        else:
        # print(f"self.tiposJogadores: {self.tiposJogadores}")
            saldos_combinados = self.historicoSaldosJogador + [['casa', self.historicoSaldosCasa]]
            self.histograma(self.historicoPremios)
            self.linhas(saldos_combinados,"histórico de saldos casa e jogadores")  
            return
        


    def exportar_csv(self, pasta_base="dados_exportados4"):
        """
        Exporta todas as tabelas em subpastas organizadas por tipo de dado.
        Os dados são acrescentados aos arquivos existentes, mantendo um índice único crescente.
        
        Args:
            pasta_base (str): Pasta base para armazenar todas as subpastas
        """
        # Criar pasta base se não existir
        os.makedirs(pasta_base, exist_ok=True)
        
        # Mapeamento de tipos de dados para suas pastas e arquivos
        pastas_arquivos = {
            'dados_gerais_casa': ("dadosGerais", "dados_gerais_casa.csv"),
            'tipos_jogadores': ("tiposJogadores", "tipos_jogadores.csv"),
            'historico_ganhos_jogadores': ("historicoGanhos", "historico_ganhos_jogadores.csv"),
            'historico_apostas_jogadores': ("historicoApostas", "historico_apostas_jogadores.csv"),
            'historico_saldos_jogadores': ("historicoSaldos", "historico_saldos_jogadores.csv"),
            'rodadas_ativas_jogadores': ("rodadasAtivas", "rodadas_ativas_jogadores.csv"),
            'total_apostado_jogadores': ("totalApostado", "total_apostado_jogadores.csv"),
            'ultimo_saldo_casa': ("ultimoSaldoCasa", "ultimo_saldo_casa.csv")
        }
        
        # Criar todas as subpastas e inicializar índices
        indices = {}
        for subpasta, arquivo in pastas_arquivos.values():
            caminho_pasta = os.path.join(pasta_base, subpasta)
            caminho_arquivo = os.path.join(caminho_pasta, arquivo)
            os.makedirs(caminho_pasta, exist_ok=True)
            
            # Verificar se arquivo existe e obter último índice
            ultimo_indice = 0
            if os.path.exists(caminho_arquivo):
                with open(caminho_arquivo, 'r', newline='') as f:
                    reader = csv.reader(f)
                    next(reader)  # Pular cabeçalho
                    for linha in reader:
                        if linha:  # Evitar linhas vazias
                            ultimo_indice = max(ultimo_indice, int(linha[0]))
            
            indices[(subpasta, arquivo)] = ultimo_indice
        
        # Função auxiliar para adicionar dados ao arquivo com índice
        def adicionar_dados(caminho, cabecalho, dados):
            escrever_cabecalho = not os.path.exists(caminho)
            with open(caminho, 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                if escrever_cabecalho:
                    writer.writerow(['id'] + cabecalho)
                
                for dado in dados:
                    indices[(subpasta, arquivo)] += 1
                    writer.writerow([indices[(subpasta, arquivo)]] + list(dado))
        
        # 1. Tabela de Dados Gerais da Casa
        subpasta, arquivo = pastas_arquivos['dados_gerais_casa']
        caminho = os.path.join(pasta_base, subpasta, arquivo)
        cabecalho = ['Rodada', 'Premio', 'ApostasRecebidas', 'PremiosPagos', 'SaldoCasa']
        dados = []
        for i in range(len(self.historicoPremios)):
            dados.append([
                i + 1,
                self.historicoPremios[i],
                self.valorApostasRecebidas[i],
                self.valorPremiosPagos[i],
                self.historicoSaldosCasa[i]
            ])
        adicionar_dados(caminho, cabecalho, dados)
        
        # 2. Tabela de Tipos de Jogadores
        subpasta, arquivo = pastas_arquivos['tipos_jogadores']
        caminho = os.path.join(pasta_base, subpasta, arquivo)
        cabecalho = ['Jogador', 'Tipo']
        dados = []
        for jogador in self.tiposJogadores:
            dados.append(jogador)
        adicionar_dados(caminho, cabecalho, dados)
        
        # 3. Tabela de Histórico de Ganhos dos Jogadores
        subpasta, arquivo = pastas_arquivos['historico_ganhos_jogadores']
        caminho = os.path.join(pasta_base, subpasta, arquivo)
        cabecalho = ['Jogador', 'Rodada', 'Ganho']
        dados = []
        for jogador in self.historicoGanhosJogador:
            jogador_id = jogador[0]
            for rodada, ganho in enumerate(jogador[1]):
                dados.append([jogador_id, rodada + 1, ganho])
        adicionar_dados(caminho, cabecalho, dados)
        
        # 4. Tabela de Histórico de Apostas dos Jogadores
        subpasta, arquivo = pastas_arquivos['historico_apostas_jogadores']
        caminho = os.path.join(pasta_base, subpasta, arquivo)
        cabecalho = ['Jogador', 'Rodada', 'x1', 'x2', 'x5', 'x10', 'azul', 'rosa', 'verde', 'vermelho']
        dados = []
        for jogador in self.historicoApostasJogador:
            jogador_id = jogador[0]
            for rodada, apostas in enumerate(jogador[1]):
                dados.append([jogador_id, rodada + 1] + list(apostas))
        adicionar_dados(caminho, cabecalho, dados)
        
        # 5. Tabela de Histórico de Saldos dos Jogadores
        subpasta, arquivo = pastas_arquivos['historico_saldos_jogadores']
        caminho = os.path.join(pasta_base, subpasta, arquivo)
        cabecalho = ['Jogador', 'Rodada', 'Saldo']
        dados = []
        for jogador in self.historicoSaldosJogador:
            jogador_id = jogador[0]
            for rodada, saldo in enumerate(jogador[1]):
                dados.append([jogador_id, rodada, saldo])
        adicionar_dados(caminho, cabecalho, dados)
        
        # 6. Tabela de Rodadas Ativas dos Jogadores
        subpasta, arquivo = pastas_arquivos['rodadas_ativas_jogadores']
        caminho = os.path.join(pasta_base, subpasta, arquivo)
        cabecalho = ['Jogador', 'RodadasAtivas']
        dados = []
        for jogador in self.rodadasVivoJogador:
            dados.append(jogador)
        adicionar_dados(caminho, cabecalho, dados)
        
        # 7. Tabela de Total Apostado por Rodada
        subpasta, arquivo = pastas_arquivos['total_apostado_jogadores']
        caminho = os.path.join(pasta_base, subpasta, arquivo)
        cabecalho = ['Jogador', 'Rodada', 'TotalApostado']
        dados = []
        for jogador in self.historicoTotalApostajogador:
            jogador_id = jogador[0]
            for rodada, total in enumerate(jogador[1]):
                dados.append([jogador_id, rodada + 1, total])
        adicionar_dados(caminho, cabecalho, dados)
        
        # 8. Tabela com Último Saldo da Casa
        subpasta, arquivo = pastas_arquivos['ultimo_saldo_casa']
        caminho = os.path.join(pasta_base, subpasta, arquivo)
        cabecalho = ['UltimoSaldoCasa']
        dados = []
        if self.historicoSaldosCasa:
            dados.append([self.historicoSaldosCasa[-1]])
        else:
            dados.append([0])
        adicionar_dados(caminho, cabecalho, dados)
        
        return pasta_base







    def exportar_mysql(self, host='localhost', user='root', password='', database='jogosdeazar', port=3306):
        """
        Exporta todos os dados para o banco MySQL com estrutura relacional completa
        """
        conn = None
        try:
            # Conectar ao banco de dados
            conn = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                port=port
            )
            cursor = conn.cursor()
            
            # 1. Tabela historico_premios
            dados = [(i+1, premio) for i, premio in enumerate(self.historicoPremios)]
            if dados:
                query = """
                INSERT IGNORE INTO historico_premios (rodada, premio)
                VALUES (%s, %s)
                """
                cursor.executemany(query, dados)
            
            # 2. Tabela valor_apostas_recebidas
            dados = [(i+1, valor) for i, valor in enumerate(self.valorApostasRecebidas)]
            if dados:
                query = """
                INSERT IGNORE INTO valor_apostas_recebidas (rodada, valor)
                VALUES (%s, %s)
                """
                cursor.executemany(query, dados)
            
            # 3. Tabela valor_premios_pagos
            dados = [(i+1, valor) for i, valor in enumerate(self.valorPremiosPagos)]
            if dados:
                query = """
                INSERT IGNORE INTO valor_premios_pagos (rodada, valor)
                VALUES (%s, %s)
                """
                cursor.executemany(query, dados)
            
            # 4. Tabela historico_saldos_casa
            dados = [(i+1, saldo) for i, saldo in enumerate(self.historicoSaldosCasa)]
            if dados:
                query = """
                INSERT IGNORE INTO historico_saldos_casa (rodada, saldo)
                VALUES (%s, %s)
                """
                cursor.executemany(query, dados)
            
            # 5. Tabela tipos_jogadores (base para relacionamentos)
            dados = [(jogador[0], jogador[1]) for jogador in self.tiposJogadores]
            if dados:
                query = """
                INSERT IGNORE INTO tipos_jogadores (jogador, tipo)
                VALUES (%s, %s)
                """
                cursor.executemany(query, dados)
            
            # 6. Tabela historico_ganhos_jogador
            dados = []
            for jogador_data in self.historicoGanhosJogador:
                jogador = jogador_data[0]
                for rodada, ganho in enumerate(jogador_data[1]):
                    dados.append((jogador, rodada+1, ganho))
            if dados:
                query = """
                INSERT IGNORE INTO historico_ganhos_jogador (jogador, rodada, ganho)
                VALUES (%s, %s, %s)
                """
                cursor.executemany(query, dados)
            
            # 7. Tabela historico_apostas_jogador
            dados = []
            for jogador_data in self.historicoApostasJogador:
                jogador = jogador_data[0]
                for rodada, apostas in enumerate(jogador_data[1]):
                    dados.append((
                        jogador,
                        rodada+1,
                        apostas[0],  # x1
                        apostas[1],  # x2
                        apostas[2],  # x5
                        apostas[3],  # x10
                        apostas[4],  # azul
                        apostas[5],  # rosa
                        apostas[6],  # verde
                        apostas[7]   # vermelho
                    ))
            if dados:
                query = """
                INSERT IGNORE INTO historico_apostas_jogador 
                    (jogador, rodada, x1, x2, x5, x10, azul, rosa, verde, vermelho)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.executemany(query, dados)
            
            # 8. Tabela historico_saldos_jogador
            dados = []
            for jogador_data in self.historicoSaldosJogador:
                jogador = jogador_data[0]
                for rodada, saldo in enumerate(jogador_data[1]):
                    dados.append((jogador, rodada+1, saldo))
            if dados:
                query = """
                INSERT IGNORE INTO historico_saldos_jogador (jogador, rodada, saldo)
                VALUES (%s, %s, %s)
                """
                cursor.executemany(query, dados)
            
            # 9. Tabela rodadas_vivo_jogador
            dados = [(jogador[0], jogador[1]) for jogador in self.rodadasVivoJogador]
            if dados:
                query = """
                INSERT IGNORE INTO rodadas_vivo_jogador (jogador, rodadas_vivo)
                VALUES (%s, %s)
                """
                cursor.executemany(query, dados)
            
            # 10. Tabela historico_total_apostas_jogador
            dados = []
            for jogador_data in self.historicoTotalApostajogador:
                jogador = jogador_data[0]
                for rodada, total in enumerate(jogador_data[1]):
                    dados.append((jogador, rodada+1, total))
            if dados:
                query = """
                INSERT IGNORE INTO historico_total_apostas_jogador (jogador, rodada, total_apostado)
                VALUES (%s, %s, %s)
                """
                cursor.executemany(query, dados)



             # 11. Tabela Último Saldo da Casa
                if self.historicoSaldosCasa:
                    ultimo_saldo = self.historicoSaldosCasa[-1]
                else:
                    ultimo_saldo = 0

                dados = [(ultimo_saldo,)]

                query = """
                INSERT INTO ultimo_saldo_casa (saldo)
                VALUES (%s)
                """
                cursor.executemany(query, dados)


            # 12. Tabela Último Saldo por Jogador por Rodada
            dados = []

            # Determinar a rodada atual (baseado no histórico da casa)
            rodada_atual = len(self.historicoSaldosCasa) if self.historicoSaldosCasa else 0

            # Processar cada jogador
            for jogador_info in self.historicoSaldosJogador:
                nome_jogador = jogador_info[0]
                saldos = jogador_info[1]
                
                # Obter último saldo do jogador
                ultimo_saldo = saldos[-1] if saldos else 0
                
                # Adicionar à lista de dados
                dados.append((rodada_atual, nome_jogador, ultimo_saldo))

            # Inserir no banco de dados
            if dados:
                query = """
                INSERT INTO ultimo_saldo_jogador (rodada, jogador, saldo)
                VALUES (%s, %s, %s)
                """
                cursor.executemany(query, dados)            



            conn.commit()
            return "Dados exportados com sucesso para todas as tabelas MySQL!"
        
        except Error as e:
            print(f"Erro MySQL: {e}")
            if conn:
                conn.rollback()
            return f"Erro na exportação: {str(e)}"
        
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()