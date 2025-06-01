from Roleta import *               # Módulo para gerenciar a roleta e sorteios
from Apostas import *              # Módulo para processar apostas e calcular prêmios
from Apostador import *            # Módulo com implementações de estratégias de apostadores
from Casa import *                 # Módulo para gerenciar o caixa da casa
from Estatisticas import *         # Módulo para coletar e exportar dados estatísticos
import time                        # Para medição de tempo de execução
import os                          # Para operações de sistema e limpeza de terminal
import sys                         # Para finalização e reinício do programa
import keyboard                    # Para captura de atalhos de teclado

def reset():
    """Reinicia o programa executando novamente o script 'game.py'."""
    limparTerminal()
    python = sys.executable
    script_path = os.path.join(os.path.dirname(__file__), 'game.py')  # caminho absoluto para 'game.py'
    os.execl(python, python, script_path)  # reinicia com 'game.py'

def finalizar():
    """Finaliza o programa exibindo o tempo total de execução."""
    fim = time.time() - inicio
    print(f"tempo de execução {fim:.2f} segundos")
    print("finalizado")        
    sys.exit()

def limparTerminal():
    """Limpa o console/terminal."""
    os.system('cls')  # limpa o terminal no início da execução

# Configurar atalhos de teclado
#keyboard.add_hotkey('space', reset)    # Espaço: reinicia o programa
#keyboard.add_hotkey('esc', finalizar)  # Esc: finaliza o programa

# Iniciar contagem de tempo global
inicio = time.time()

# =============================================================================
#                       CONFIGURAÇÕES DE SIMULAÇÃO
# =============================================================================
iteracoes = 100000         # Quantidade total de simulações a serem executadas
numJogadores = 1         # Quantidade de jogadores por simulação
rodadas = 300            # Quantidade máxima de rodadas por simulação
# =============================================================================

# Lista para histórico de jogadores ativos (não utilizado no código atual)
historicoJogadoresAtivos = []

# Loop principal de simulações
for j in range(0, iteracoes):
# =========================================================================
#               INICIALIZAÇÃO DE OBJETOS PARA CADA SIMULAÇÃO
# =========================================================================
    r1 = Roleta()        # Controla sorteios da roleta
    a1 = Apostas()       # Processa cálculos de apostas e prêmios
    c1 = Casa()          # Gerencia o caixa da casa (banca)
    e1 = Estatisticas()  # Coleta dados estatísticos da simulação

    # Exibir progresso a cada 1% das iterações
    if j % (iteracoes / 100) == 0: 
        limparTerminal() 
        print(f'task {j // (iteracoes / 100):.0f}%')
        print(f'tempo decorrido {time.time() - inicio:.2f}s')

# =========================================================================
#                      CONFIGURAÇÃO DOS JOGADORES
# =========================================================================
    jogadores = []
    # Adiciona diferentes estratégias de apostadores
    for _ in range(0, numJogadores):
        jogadores.append(ApostadorPadrao())        # Estratégia padrão
        jogadores.append(apostadorAleatorio())     # Estratégia aleatória
        jogadores.append(ApostadorConservador())   # Estratégia conservadora
        jogadores.append(ApostadorEstrategia25())  # Estratégia de 25% de lucro
        jogadores.append(ApostadorArrojado())      # Estratégia arrojada
       

 # =========================================================================
                     # EXECUÇÃO DAS RODADAS
 # =========================================================================
    for i in range(0, rodadas):
        # Identificar jogadores ativos (com saldo positivo)
        jogadoresAtivos = [at for at in jogadores if at.estaAtivo()]
        
        # Encerrar simulação se não houver jogadores ativos
        if not jogadoresAtivos:
            break

        # Coletar apostas dos jogadores
        apostados = []
        for player in jogadoresAtivos:
            ap = player.apostar()
            apostados.append((player, ap))

        # Realizar sorteio
        giro = r1.girar()
    
        # Processar prêmios
        pot = []
        for player, ap in apostados:
            # Registrar aposta na casa
            c1.receberApostas(sum(ap))

            # Calcular prêmio
            premio = a1.aposta(*ap, giro[0])
            
            # Pagar prêmio ao jogador
            player.receberPremio(premio)
            
            # Registrar pagamento na casa
            c1.pagarPremio(premio)
        
            # Acumular valor total de prêmios
            pot.append(premio)
        
        # Atualizar saldo da casa
        c1.deduzirPremio(sum(pot))

# ========================================================================
                    # COLETA E EXPORTAÇÃO DE DADOS
#=========================================================================
    e1.coletarDados(jogadores, c1, r1)
    #e1.GraficoSaldosCasaJogador()
    #e1.exportar_csv() 
    e1.exportar_mysql()
    
    jogadores.clear()
# Finalizar programa após todas as simulações
finalizar()