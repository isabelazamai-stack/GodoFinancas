CREATE database if NOT EXISTS bd_godofin;

USE bd_godofin;

CREATE TABLE if NOT EXISTS tb_usuarios (
 id_usuario INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
 usuario VARCHAR(30) UNIQUE,
 senha VARCHAR(200)
);


CREATE TABLE if NOT EXISTS tb_categoria (
 id_categoria INT NOT NULL AUTO_INCREMENT,
 id_usuario INT NOT NULL,
 nome VARCHAR(40),

 PRIMARY KEY (id_categoria,id_usuario),

 FOREIGN KEY (id_usuario) REFERENCES tb_usuarios (id_usuario)
);


CREATE TABLE if NOT EXISTS tb_despesas (
 id_despesa INT NOT NULL AUTO_INCREMENT,
 id_usuario INT NOT NULL,
 valor DECIMAL(30,2),
 data_despesa DATE,
 descricao VARCHAR(100),
 id_categoria INT,

 PRIMARY KEY (id_despesa,id_usuario),

 FOREIGN KEY (id_usuario) REFERENCES tb_usuarios (id_usuario),
 FOREIGN KEY (id_categoria,id_usuario) REFERENCES tb_categoria (id_categoria,id_usuario)
);


