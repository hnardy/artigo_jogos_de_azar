from random import randint

# Classe que representa um apostador com uma estratégia padrão.
# Aposta em todas as categorias igualmente, se possível.
# Mantém históricos de saldo, apostas e ganhos.

class ApostadorPadrao:
  

    def __init__(self, saldo=1000):
        """
        Inicializa o jogador com um saldo definido.

        Args:
            saldo (int): saldo inicial do jogador (padrão 1000)
        """

        self.historicoGanhos =[]    # Guarda todos os prêmios recebidos
        self.historicoApostas=[]    # Guarda todas as apostas realizadas
        self.historicoSaldos =[saldo]    # Guarda o saldo antes de cada aposta                                   
        self.saldo = saldo          #saldo variavel
        self.tipo = "padrao"

    def estaAtivo(self):
        """
        Verifica se o jogador ainda possui saldo.

        Returns:
            bool: True se o saldo for maior que 0, False caso contrário
        """
        return self.saldo > 0

    def receberPremio(self, premio):
        """
        Atualiza o saldo do jogador com o valor do prêmio recebido e registra no histórico.

        Args:
            premio (int): valor a ser adicionado ao saldo
        """
        self.saldo += premio
        self.historicoGanhos.append(premio)

    def apostar(self):
        """
        Realiza uma aposta com parte do saldo disponível, dividindo igualmente entre as categorias,
        se possível. Se o saldo for menor que 8, aposta tudo em x1.

        Returns:
            tuple: valores apostados em cada categoria
        """
        
        montanteAposta = randint(1, int(self.saldo))

        if 1 <= montanteAposta < 8:
            x1 = montanteAposta
            x2 = x5 = x10 = azul = rosa = verde = vermelho = 0
            self.saldo -= montanteAposta

        elif montanteAposta >= 8:
            aposta_unitaria = montanteAposta // 8
            x1 = x2 = x5 = x10 = azul = rosa = verde = vermelho = aposta_unitaria
            total_apostado = aposta_unitaria * 8
            self.saldo -= total_apostado

        else:
            # Aposta nula se o saldo não permite nem 1 de aposta
            x1 = x2 = x5 = x10 = azul = rosa = verde = vermelho = 0

        self.historicoApostas.append([x1, x2, x5, x10, azul, rosa, verde, vermelho])
        self.historicoSaldos.append(self.saldo)
        return x1, x2, x5, x10, azul, rosa, verde, vermelho




##################################################################################



class apostadorAleatorio(ApostadorPadrao):

    def __init__(self, saldo=1000):
        """
        Inicializa o jogador com um saldo definido.

        Args:
            saldo (int): saldo inicial do jogador (padrão 1000)
        """

        self.historicoGanhos =[]    # Guarda todos os prêmios recebidos
        self.historicoApostas=[]    # Guarda todas as apostas realizadas
        self.historicoSaldos =[saldo]    # Guarda o saldo antes de cada aposta                                   
        self.saldo = saldo          #saldo variavel
        self.saldo_inicial = saldo
        self.firstTime = True
        self.tipo = "aleatorio"


    def estaAtivo(self):
    # Desativa se ultrapassar 100% de lucro
        if self.saldo > self.saldo_inicial * 2:
            self.ativo = False
            if (self.firstTime == True):
                    self.historicoSaldos.append(self.saldo)
                    self.firstTime = False
        else:
            self.ativo = True
        return self.saldo > 0 and self.ativo



    def apostar(self):
        """
    Jogador aleatório: sorteia um percentual do saldo (0% a 100%) para apostar,
    e divide aleatoriamente esse valor entre as 8 categorias.

    Returns:
        tuple: valores apostados em cada categoria
    """
       

        if self.saldo < 1:
            # Sem saldo para apostar
            x1 = x2 = x5 = x10 = azul = rosa = verde = vermelho = 0
        else:
            # Sorteia quanto será apostado (até 100% do saldo)
            montanteAposta = randint(1, int(self.saldo))

            # Cria 8 valores aleatórios que somam exatamente montanteAposta
            distribuicao = [randint(0, montanteAposta) for _ in range(8)]
            total = sum(distribuicao)
            if total == 0:
                distribuicao = [0]*8
            else:
                distribuicao = [int(montanteAposta * val / total) for val in distribuicao]

                # Corrige diferença por arredondamento (ajusta a 1ª posição)
                diferenca = montanteAposta - sum(distribuicao)
                distribuicao[0] += diferenca

            x1, x2, x5, x10, azul, rosa, verde, vermelho = distribuicao
            self.saldo -= montanteAposta

        self.historicoApostas.append([x1, x2, x5, x10, azul, rosa, verde, vermelho])
        self.historicoSaldos.append(self.saldo)
#        print(f'apostas aleatórias {x1, x2, x5, x10, azul, rosa, verde, vermelho}')
        return x1, x2, x5, x10, azul, rosa, verde, vermelho




##################################################################################
class ApostadorEstrategia25(ApostadorPadrao):

    def __init__(self, saldo=1000):
        super().__init__(saldo)
        self.tipo = "estratégia dos 25"
        self.saldo_inicial = saldo
        self.initial_aposta = int(saldo * 0.1)  # 10% do saldo inicial
        self.aposta_atual = self.initial_aposta
        self.ativo = True
        self.firstTime = True


    def estaAtivo(self):
        # Desativa se ultrapassar 25% de lucro
        if self.saldo > self.saldo_inicial * 1.25:
            self.ativo = False
            if (self.firstTime == True):
                    self.historicoSaldos.append(self.saldo)
                    self.firstTime = False
        else:
            self.ativo = True
        return self.saldo > 0 and self.ativo

    def apostar(self):
        
        if self.estaAtivo() and self.saldo >= 1:
            montanteAposta = min(self.aposta_atual, self.saldo)
            
            # Escolhe uma posição aleatória (0-7) para a aposta especial
            posicao_escolhida = random.randint(0, 7)
            
            # Calcula 1-15% do montante para a posição escolhida
            percentual = random.randint(1, 15)
            valor_especial = max(1, int(montanteAposta * percentual / 100))
            
            # Ajusta se o valor exceder o saldo disponível
            valor_especial = min(valor_especial, montanteAposta)
            
            # Subtrai o valor especial do montante total
            montante_restante = montanteAposta - valor_especial
            
            # Distribui o restante conforme a estratégia original
            apostas = [0, 0, 0, 0, 1, 1, 1, 1]
            total_last_four = 4
            remaining = montante_restante - total_last_four

            # Ajuste para montantes insuficientes nas últimas 4 posições
            if remaining < 0:
                deficit = -remaining
                for i in range(7, 3, -1):
                    if apostas[i] > 0 and deficit > 0:
                        apostas[i] -= 1
                        deficit -= 1
                remaining = 0

            # Distribui o restante nas posições 1-3
            if remaining > 0:
                part, resto = divmod(remaining, 3)
                apostas[1] = part
                apostas[2] = part
                apostas[3] = part
                if resto >= 1:
                    apostas[1] += 1
                if resto >= 2:
                    apostas[2] += 1

            # Adiciona o valor especial à posição escolhida
            apostas[posicao_escolhida] += valor_especial

            # Garante que o total não ultrapasse o montante
            total_apostado = sum(apostas)
            if total_apostado > montanteAposta:
                excesso = total_apostado - montanteAposta
                for i in range(7, -1, -1):
                    if excesso <= 0:
                        break
                    if apostas[i] > 0:
                        reducao = min(apostas[i], excesso)
                        apostas[i] -= reducao
                        excesso -= reducao

            # Atualiza saldo e histórico
            self.saldo -= sum(apostas)
            self.historicoApostas.append(apostas)
            self.historicoSaldos.append(self.saldo)
            return tuple(apostas)
        else:
            self.historicoSaldos.append(self.saldo)
            return (0, 0, 0, 0, 0, 0, 0, 0)

    def atualizarAposta(self, resultado):
        if resultado:
            self.aposta_atual = self.initial_aposta  # Reset para 10% do saldo inicial após vitória
        else:
            self.aposta_atual *= 2  # Dobra a aposta após derrota

############################################################################################################

import random

class ApostadorConservador(ApostadorPadrao):

    def __init__(self, saldo=1000):
        super().__init__(saldo)
        self.tipo = "conservador"
        self.saldo_inicial = saldo
        self.ativo = True
        self.firstTime = True
        # Aposta inicial entre 5% e 10% do saldo atual
        self.aposta_atual = self.calcular_aposta_inicial()

    def calcular_aposta_inicial(self):
        return max(1, int(self.saldo * random.uniform(0.05, 0.10)))

    def estaAtivo(self):
        # Desativa ao atingir 10% de lucro ou se saldo zerar
        if self.saldo >= self.saldo_inicial * 1.10:
            self.ativo = False
            if (self.firstTime == True):
                self.historicoSaldos.append(self.saldo)
                self.firstTime = False

        return self.saldo > 0 and self.ativo

    def apostar(self):
        if self.estaAtivo() and self.saldo >= 1:
            # Calcula valor da aposta garantindo mínimo 1 e máximo saldo disponível
            montante = min(self.aposta_atual, self.saldo)
            montante = max(montante, 1)
            
            # Aloca toda a aposta na posição 4 (x1)
            apostas = [0] * 8
            apostas[0] = montante
            
            # Atualiza saldo
            self.saldo -= montante
            self.historicoApostas.append(apostas.copy())
            self.historicoSaldos.append(self.saldo)
            return tuple(apostas)
        
        self.historicoSaldos.append(self.saldo)
        return (0, 0, 0, 0, 0, 0, 0, 0)

    def atualizarAposta(self, resultado):
        if resultado:
            # Reset para 5-10% do saldo atual após vitória
            self.aposta_atual = max(1, int(self.saldo * random.uniform(0.05, 0.10)))
        else:
            # Dobra a aposta mantendo entre 5-10% do saldo atual
            doubled = self.aposta_atual * 2
            min_val = max(1, int(self.saldo * 0.05))
            max_val = max(1, int(self.saldo * 0.10))
            self.aposta_atual = min(doubled, max_val)
            self.aposta_atual = max(self.aposta_atual, min_val)


############################################################################################################           
import random

class ApostadorArrojado(ApostadorPadrao):

    def __init__(self, saldo=1000):
        super().__init__(saldo)
        self.tipo = "arrojado"
        self.saldo_inicial = saldo
        # Começa com 10% do saldo, mas em cada perda dobra sem nunca voltar ao original
        self.aposta_atual = max(1, int(saldo * 0.1))
        self.ativo = True
        self.firstTime= True

    def estaAtivo(self):
        # Fica inativo ao dobrar o saldo inicial (100% de lucro)
        if self.saldo >= self.saldo_inicial * 2:
            self.ativo = False
            if (self.firstTime == True):
                self.historicoSaldos.append(self.saldo)
                self.firstTime = False

        return self.saldo > 0 and self.ativo

    def apostar(self):
        self.historicoSaldos.append(self.saldo)

        if not self.estaAtivo() or self.saldo < 1:
            return (0,)*8

        # Define limites garantidos
        min_p = max(1, int(self.saldo * 0.1))
        max_p = max(1, int(self.saldo * 0.3))
        # Se max menor que min, corrige
        if max_p < min_p:
            max_p = min_p

        # Montante é a aposta atual, mas dentro dos limites e do que sobra no saldo
        montanteAposta = min(max(self.aposta_atual, min_p), max_p, self.saldo)

        apostas = [0]*8

        if montanteAposta < 5:
            # Se não dá para distribuir entre 5 casas, joga tudo no x10
            apostas[3] = montanteAposta
        else:
            # Divide igualmente entre x10, azul, rosa, verde, vermelho (índices 3-7)
            parte, resto = divmod(montanteAposta, 5)
            for i in range(3, 8):
                apostas[i] = parte
            for i in range(resto):
                apostas[3 + i] += 1

        total_apostado = sum(apostas)
        self.saldo -= total_apostado
        self.historicoApostas.append(apostas.copy())
        return tuple(apostas)

    def atualizarAposta(self, resultado):
        if not resultado:
            # Dobra a aposta atual, sem redução posterior
            self.aposta_atual *= 2

#########################################################################################################
