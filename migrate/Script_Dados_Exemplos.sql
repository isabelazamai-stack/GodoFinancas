INSERT INTO `bolso_furado`.`tb_usuarios` (`usuario`, `senha`) VALUES ('Godofredo', 'GODO');
INSERT INTO `bolso_furado`.`tb_usuarios` (`usuario`, `senha`) VALUES ('Felizberta', 'FEFE');

INSERT INTO `bolso_furado`.`tb_categoria` (`id_usuario`, `nome`) VALUES ('1', 'LAZER');
INSERT INTO `bolso_furado`.`tb_categoria` (`id_usuario`, `nome`) VALUES ('1', 'ALIMENTAÇÃO');
INSERT INTO `bolso_furado`.`tb_categoria` (`id_usuario`, `nome`) VALUES ('1', 'CONTAS');
INSERT INTO `bolso_furado`.`tb_categoria` (`id_usuario`, `nome`) VALUES ('1', 'TRANSPORTE');
INSERT INTO `bolso_furado`.`tb_categoria` (`id_usuario`, `nome`) VALUES ('2', 'LAZER');
INSERT INTO `bolso_furado`.`tb_categoria` (`id_usuario`, `nome`) VALUES ('2', 'ALIMENTAÇÃO');
INSERT INTO `bolso_furado`.`tb_categoria` (`id_usuario`, `nome`) VALUES ('2', 'CONTAS');
INSERT INTO `bolso_furado`.`tb_categoria` (`id_usuario`, `nome`) VALUES ('2', 'TRANSPORTE');

INSERT INTO `bolso_furado`.`tb_despesas` (`id_usuario`, `valor`, `data_despesa`, `descricao`, `id_categoria`) VALUES ('1', '80', '2026-10-06 13:23:44', 'Saida para o shopping', '1');
INSERT INTO `bolso_furado`.`tb_despesas` (`id_usuario`, `valor`, `data_despesa`, `descricao`, `id_categoria`) VALUES ('1', '120', '2026-10-06 13:23:44', 'Restaurante', '2');
INSERT INTO `bolso_furado`.`tb_despesas` (`id_usuario`, `valor`, `data_despesa`, `descricao`, `id_categoria`) VALUES ('1', '300', '2026-10-06 13:23:44', 'Contas de luz/Água e internet', '3');
INSERT INTO `bolso_furado`.`tb_despesas` (`id_usuario`, `valor`, `data_despesa`, `descricao`, `id_categoria`) VALUES ('2', '90', '2026-10-06 13:23:44', 'Saida para o shopping', '5');
INSERT INTO `bolso_furado`.`tb_despesas` (`id_usuario`, `valor`, `data_despesa`, `descricao`, `id_categoria`) VALUES ('2', '89', '2026-10-06 13:23:44', 'Restaurante', '6');
INSERT INTO `bolso_furado`.`tb_despesas` (`id_usuario`, `valor`, `data_despesa`, `descricao`, `id_categoria`) VALUES ('2', '200', '2026-10-06 13:23:44', 'Contas de luz/Água e internet', '7');