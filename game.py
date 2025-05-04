
from Roleta import *
from Apostas import *
from Apostador import *
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
numJogadores = 2  # quantidade de jogadores
rodadas = 300 #quantidade de jogos
# histórico de jogadores ativos armazena [iteração, ativos]
historicoJogadoresAtivos = []

# quantidade de iterações
for j in range(0, iteracoes):

    # Exibir progresso a cada 1% (para debug)
    #if j % (iteracoes / 100) == 0:  
    #    print(f'task {j // (iteracoes / 100):.0f}%')
    #    print(f'tempo decorrido {time.time() - inicio:.2f}s')

    # definir jogadores
    jogadores = []
    for j in range(0, numJogadores):
        # aqui devem ser implementadas diferentes estratégias 
        jogadores.append(ApostadorPadrao())

    # iniciar jogos
    for i in range(0, rodadas):  # 300 é um número de segurança para evitar estratégias imortais
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
        pot = []#saldo pago pela casa
        for player, ap in apostados:
            c1.receberApostas(sum(ap))  # informa a casa de apostas quanto ela recebeu do jogador

            premio = a1.aposta(*ap, giro[0])  # calcula o prêmio
         
            player.receberPremio(premio)  # paga o jogador 
            c1.pagarPremio(premio)  # informa a casa de aposta quanto ela pagou ao jogador
        
            pot.append(premio)#atualizar saldo na casa
        c1.deduzirPremio(sum(pot))

 
    # Exportar dados ao final da iteração
    e1.coletarDados(jogadores,c1,r1)

    # Após coletar todos os dados ao longo das iterações, gerar gráficos ou relatórios



#e1.exportarCSV(nome_arquivo="relatório")    









# Finalizar programa
fim = time.time() - inicio
print(f"tempo de execução {fim:.2f} segundos")
print("finalizado")

# Notas:
# - Jogadores apostam -> número sorteado -> prêmio pago
# - Banca da casa, central de gráficos, multiplicidade de jogadores
