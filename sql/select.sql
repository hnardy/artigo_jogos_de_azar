CREATE DATABASE `jogosdeazar` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
use jogosdeazar;

SELECT * FROM historico_apostas_jogador;
SELECT * FROM historico_ganhos_jogador;
SELECT * FROM historico_premios;
SELECT * FROM historico_saldos_casa;
SELECT * FROM historico_saldos_jogador;
SELECT * FROM historico_total_apostas_jogador;
SELECT * FROM rodadas_vivo_jogador;
SELECT * FROM tipos_jogadores;
SELECT * FROM ultimo_saldo_casa;
SELECT * FROM ultimo_saldo_jogador;
SELECT * FROM valor_apostas_recebidas;
SELECT * FROM valor_premios_pagos;

-- Simulações onde a casa ficou com valor positivo:
select * from ultimo_saldo_casa
where saldo > 0;    -- 79058

-- Simulações onde a casa lucrou 0:
select * from ultimo_saldo_casa   -- 4
where saldo = 0;

-- Simulações onde a casa lucrou 5000:
select * from ultimo_saldo_casa   -- 13465
where saldo = 5000 ; -- (5000 derrota de todos os jogadores)

-- Simulações onde a casa levou prejuízo:
select * from ultimo_saldo_casa -- 20938
where saldo < 0; 

-- lucro liquido da casa
SELECT SUM(saldo) AS total_saldo -- 169909868.00
FROM ultimo_saldo_casa;

-- prejuízo bruto casa 
SELECT SUM(saldo) AS total_saldo_negativo -- -62906285.00
FROM ultimo_saldo_casa
WHERE saldo < 0;

-- lucro bruto casa 
SELECT SUM(saldo) AS total_saldo_negativo -- 232816153.00
FROM ultimo_saldo_casa
WHERE saldo > 0;

-- ####################################################### -- 

-- vezes sorteadas (x1 x2 x5 x10 azul verde rosa vermelho)
SELECT * FROM historico_premios  -- x1 2427423  x2 1503228  x5 809888  x10 461799  azul 462542 verde 231196 rosa 231733 vermelho 115900 
where premio = 'vermelho';


-- soma de valor apostado   (x1 x2 x5 x10 azul verde rosa vermelho)
SELECT SUM(vermelho) AS total_x1
FROM historico_apostas_jogador; -- x1 556033683 x2 390947910 x5 389880426 x10 440067020 azul 357094808 verde 356303388 rosa 356683744 vermelho 355981958

-- tabela de premios e valores 
SELECT vpp.*, hp.premio AS premio_historico
FROM valor_premios_pagos vpp
LEFT JOIN historico_premios hp 
    ON vpp.id = hp.id AND vpp.rodada = hp.rodada
ORDER BY vpp.rodada;

-- valor de cada premio  (x1 x2 x5 x10 azul verde rosa vermelho)
SELECT SUM(vpp.valor) AS soma_valor -- x1 429625818 x2 285452085 x5 333118116 x10 348973537 azul verde rosa vermelho
FROM valor_premios_pagos vpp
LEFT JOIN historico_premios hp 
    ON vpp.id = hp.id AND vpp.rodada = hp.rodada
WHERE hp.premio = 'vermelho';



-- ####################################################### -- 


-- ciclos vividos por jogador 
SELECT sum(rodadas_vivo) FROM rodadas_vivo_jogador
where jogador = 'player4';

-- média de ciclos vividos por jogador
SELECT AVG(rodadas_vivo) AS media_rodadas_vivo
FROM rodadas_vivo_jogador
WHERE jogador = 'player4';

-- ultimos saldos positivos
SELECT * FROM ultimo_saldo_jogador
where jogador = 'player4' and saldo > 0; 

-- saldos zerados
SELECT * FROM ultimo_saldo_jogador
where jogador = 'player4' and saldo = 0; 

-- média de ganhos
select avg(saldo) from ultimo_saldo_jogador
where	jogador ='player4';

-- maior banca final 
SELECT MAX(saldo) AS maior_saldo
FROM ultimo_saldo_jogador
WHERE jogador = 'player4';

-- total jogado
SELECT * FROM historico_total_apostas_jogador
where jogador = 'player0';
