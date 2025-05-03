from Roleta import Roleta
from Apostas import Apostas
from Apostador import *
from Graficos import *
from Casa import *
import time 
import os


def limparTerminal():
    os.system('cls') #limpa o teminal no inicio da execução


#inicia timer da execução
inicio = time.time() 

#limpar terminal para nova execução
limparTerminal() 

#iniciar objetos
r1 = Roleta()  #sorteia números 
a1 = Apostas() #processa apostas 
j1 = ApostadorPadrao() # realiza apostas 
c1 = Casa() #simula a banca da casa 
#e1 = Estatisticas() #armazena e processa dados  

#controle de progresso 
taskbar=0 # progresso da execução 

#controles de jogo
iteracoes = 1 # quantidade de jogos (1 por padrão )
numJogadores = 100 #quantidade de jogadores 


#historico de jogadores ativos armazena [iteração, ativos]
historicoJogadoresAtivos = []


#quantidade de iterações
for j in range(0, iteracoes):

    # Exibir progresso a cada 1%
    if j % (iteracoes/100) == 0:  
        print(f'task {j // (iteracoes/100):.0f}%')
        print(f'tempo decorrido {time.time() - inicio:.2f}s')
        




    #definir jogadores 
    jogadores = []
    for j in range  (0,numJogadores):
        #aqui devem ser implementadas diferentes estratégias 
        jogadores.append(ApostadorPadrao())



    #inciar jogos
    for i in range(0,300): #300 é um número de segurança para evitar estratégias imortais
        #listar jogadores ativos 
        jogadoresAtivos = []
        for at in jogadores:
            if at.estaAtivo():  
                jogadoresAtivos.append(at) #apenas jogadores ativos faram apostas
        
        
        #se não houver jogadores ativos
        if jogadoresAtivos == []:
        #   print ("sem jogadores ativos")
            break

        #apostar
        apostados = [] #recebe as apostados dos jogares ativos
        
        for player in jogadoresAtivos:
            ap = player.apostar() #o jogador faz a aposta
            apostados.append((player,ap)) #guardados os dados do jogador e aposta feita [jogador, [x1 x2 x5 x10 azul rosa verde vermelho ]]

        #sortear
        giro = r1.girar() 
    
        #conferir e pagar

        for player, ap in apostados:
            c1.receberApostas(sum(ap)) #informa a casa de apostas quanto ela recebeu do jogador

            player.receberPremio(a1.aposta(*ap, giro[0])) # paga o jogador 
                                                          #"giro" armazena tanto o tipo de premio quanto a casa, por isso giro[0]
            c1.pagarPremio(a1.aposta(*ap, giro[0])) #informa a casa de aposta quanto ela pagou ao jogador
        

    #exportar dados 
    #ao final da iteração os dados são exportados e os jogadores deletados 

    










# finalizar programa 
fim =  time.time() - inicio
print(f" tempo de execução {fim:.2f} segundos")
print ("finalizado")







 #jogadores apostam -> numero sorteado -> premio pago 
 #banca da casa, central de graficos, multiplicidade de jogadores
