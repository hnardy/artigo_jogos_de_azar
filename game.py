from Roleta import Roleta
from Apostas import Apostas
from Apostador import *
import time 
import os

os.system('cls') #limpa o teminal no inicio da execução

inicio = time.time()


r1 = Roleta()
a1 = Apostas()
j1 = apostadorPadrao()

for i in range(0,300):
   
    print(f"saldo anterior: {j1.saldo:.2f}")
   
    ap = j1.apostaCega()
    print(f"apostas: {ap}")

    giro = r1.girar()
    print(f"sorteado:{giro}")

    ad = a1.aposta(ap[0],ap[1],ap[2],ap[3],ap[4],ap[5],ap[6],ap[7],giro[0])
    print(f"premio: {ad}")
    j1.receberPremio(ad)
    
    print(f"saldo novo: {j1.saldo:.2f}")

    if(j1.saldo == 0):
        print(f"saldo zerado em {i} rodadas")
        break

    print("")

print("============")
j1.exbirHistorico()







fim =  time.time() - inicio
print(f" tempo de execução {fim:.2f} segundos")
print ("finalizado")



# jogadores apostam -> numero sorteado -> premio pago 
