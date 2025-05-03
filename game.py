from Roleta import *
from Apostas import *
from Apostador import *
from Graficos import *
from Casa import *
from Estatisticas import *
import time 
import os

def limparTerminal():
    os.system('cls')  # limpa o terminal no início da execução

# inicia o timer da execução
inicio = time.time()

# limpar terminal para nova execução
limparTerminal()

# iniciar objetos
r1 = Roleta()  # sorteia números
a1 = Apostas()  # processa apostas
j1 = ApostadorPadrao()  # realiza apostas
c1 = Casa()  # simula a banca da casa
e1 = Estatisticas()  # armazena e processa dados

# controle de progresso
taskbar = 0  # progresso da execução

# controles de jogo
iteracoes = 1  # quantidade de jogos (1 por padrão)
numJogadores = 100  # quantidade de jogadores

# histórico de jogadores ativos armazena [iteração, ativos]
historicoJogadoresAtivos = []

# quantidade de iterações
for j in range(0, iteracoes):
    # Exibir progresso a cada 1%
    if j % (iteracoes / 100) == 0:  
        print(f'task {j // (iteracoes / 100):.0f}%')
        print(f'tempo decorrido {time.time() - inicio:.2f}s')

    # definir jogadores
    jogadores = []
    for j in range(0, numJogadores):
        # aqui devem ser implementadas diferentes estratégias 
        jogadores.append(ApostadorPadrao())

    # iniciar jogos
    for i in range(0, 300):  # 300 é um número de segurança para evitar estratégias imortais
        # listar jogadores ativos
        jogadoresAtivos = []
        for at in jogadores:
            if at.estaAtivo():  
                jogadoresAtivos.append(at)  # apenas jogadores ativos farão apostas
        
        # se não houver jogadores ativos
        if not jogadoresAtivos:
            break

        # apostar
        apostados = []  # recebe as apostas dos jogadores ativos
        for player in jogadoresAtivos:
            ap = player.apostar()  # o jogador faz a aposta
            apostados.append((player, ap))  # guardamos os dados do jogador e aposta feita

        # sortear
        giro = r1.girar()
    
        # conferir e pagar
        for player, ap in apostados:
            c1.receberApostas(sum(ap))  # informa a casa de apostas quanto ela recebeu do jogador

            premio = a1.aposta(*ap, giro[0])  # calcula o prêmio
            player.receberPremio(premio)  # paga o jogador 
            c1.pagarPremio(premio)  # informa a casa de aposta quanto ela pagou ao jogador

        # Coleta de dados para estatísticas
        dados_iteracao = {
            'historicoPremios': [giro[0] for player, ap in apostados],
            'historicoDeSorteios': [giro[1] for player, ap in apostados],
            'historicoGanhos': [player.saldo for player in jogadoresAtivos],
            'historicoApostas': [ap for player, ap in apostados],
            'historicoSaldos': [player.saldo for player in jogadores],
            'rodadasAteFalha': [player.rodadasAteFalha() for player in jogadores],
            'valorApostasRecebidas': [sum(ap) for player, ap in apostados],
            'valorPremiosPagos': [premio for player, ap in apostados],
            'historicoJogadoresAtivos': [player.estaAtivo() for player in jogadores]
        }

        # Passa os dados coletados para a classe Estatisticas
        e1.coletarDados(dados_iteracao)

    # Exportar dados ao final da iteração
    # Após coletar todos os dados ao longo das iterações, gerar gráficos ou relatórios

    e1.gerarRelatorio()  # Gera um relatório das estatísticas coletadas
    e1.gerarGraficoSaldos()  # Gera o gráfico de saldos dos jogadores
    e1.gerarGraficoApostas()  # Gera o gráfico de apostas feitas
    e1.gerarGraficoPremios()  # Gera o gráfico de prêmios pagos

# Finalizar programa
fim = time.time() - inicio
print(f"tempo de execução {fim:.2f} segundos")
print("finalizado")

# Notas:
# - Jogadores apostam -> número sorteado -> prêmio pago
# - Banca da casa, central de gráficos, multiplicidade de jogadores
