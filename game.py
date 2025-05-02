from Roleta import Roleta
from Apostas import Apostas
from Apostador import *
from Graficos import *
import time 
import os

os.system('cls') #limpa o teminal no inicio da execução

inicio = time.time()


r1 = Roleta()
a1 = Apostas()
j1 = apostadorPadrao()
g1 = Graficos()
g2 = Graficos()
taskbar=0
tempoParaZerar = []
import os
import time

tempoParaZerar = []
saldos = []

iteracoes = 1000

for j in range(0, iteracoes):

    # Exibir progresso a cada 1%
    if j % (iteracoes/100) == 0:
        os.system('cls')  
        print(f'task {j // (iteracoes/100):.0f}%')
        print(f'tempo decorrido {time.time() - inicio:.2f}s')
        

    j1 = apostadorPadrao()
    minisaldo = []   
    for i in range(0,300):
    
        
        minisaldo.append(j1.saldo)
      #  print(f"saldo anterior: {j1.saldo:.2f}")
    
        ap = j1.apostaCega()
       # print(f"apostas: {ap}")

        giro = r1.girar()
        #print(f"sorteado:{giro}")

        ad = a1.aposta(ap[0],ap[1],ap[2],ap[3],ap[4],ap[5],ap[6],ap[7],giro[0])
        #print(f"premio: {ad}")
        j1.receberPremio(ad)
        
       # print(f"saldo novo: {j1.saldo:.2f}")

        if(j1.saldo == 0):
            saldos.append(minisaldo)
            break



print("============")

print(saldos)


g1.linhas(saldos)





# finalizar programa 
fim =  time.time() - inicio
print(f" tempo de execução {fim:.2f} segundos")
print ("finalizado")




 #jogadores apostam -> numero sorteado -> premio pago 
 #banca da casa, central de graficos, multiplicidade de jogadores
