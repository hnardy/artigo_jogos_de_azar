from Roleta import Roleta
import time 

inicio = time.time()

for x in range (0,1000000):   
  print(f'rodada {x}')
  r1 = Roleta()
  i = r1.girar()
  print(f'{i[0]} casa {i[1]}')


fim =  time.time() - inicio
print(f" tempo de execução {fim:.2f} segundos")
print ("finalizado")




aposta1 = 
