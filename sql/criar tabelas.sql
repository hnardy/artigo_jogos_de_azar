CREATE TABLE `historico_apostas_jogador` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `jogador` varchar(50) NOT NULL,
  `rodada` int(11) NOT NULL,
  `x1` decimal(15,2) NOT NULL,
  `x2` decimal(15,2) NOT NULL,
  `x5` decimal(15,2) NOT NULL,
  `x10` decimal(15,2) NOT NULL,
  `azul` decimal(15,2) NOT NULL,
  `rosa` decimal(15,2) NOT NULL,
  `verde` decimal(15,2) NOT NULL,
  `vermelho` decimal(15,2) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `historico_ganhos_jogador` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `jogador` varchar(50) NOT NULL,
  `rodada` int(11) NOT NULL,
  `ganho` decimal(15,2) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `historico_premios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rodada` int(11) NOT NULL,
  `premio` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `historico_saldos_casa` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rodada` int(11) NOT NULL,
  `saldo` decimal(15,2) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `historico_saldos_jogador` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `jogador` varchar(50) NOT NULL,
  `rodada` int(11) NOT NULL,
  `saldo` decimal(15,2) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `historico_total_apostas_jogador` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `jogador` varchar(50) NOT NULL,
  `rodada` int(11) NOT NULL,
  `total_apostado` decimal(15,2) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `rodadas_vivo_jogador` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `jogador` varchar(50) NOT NULL,
  `rodadas_vivo` int(11) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `tipos_jogadores` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `jogador` varchar(50) NOT NULL,
  `tipo` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `ultimo_saldo_casa` (
  `rodada` int(11) NOT NULL AUTO_INCREMENT,
  `saldo` decimal(15,2) NOT NULL,
  PRIMARY KEY (`rodada`)
);

CREATE TABLE `ultimo_saldo_jogador` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rodada` int(11) NOT NULL,
  `jogador` varchar(50) NOT NULL,
  `saldo` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `valor_apostas_recebidas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rodada` int(11) NOT NULL,
  `valor` decimal(15,2) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `valor_premios_pagos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rodada` int(11) NOT NULL,
  `valor` decimal(15,2) NOT NULL,
  PRIMARY KEY (`id`)
);