CREATE DATABASE IF NOT EXISTS flex_treino;

USE flex_treino;

CREATE TABLE IF NOT EXISTS fornecedores (
    id    INT AUTO_INCREMENT PRIMARY KEY,
    nome  VARCHAR(100) NOT NULL,
    pais  VARCHAR(50)  NOT NULL,
    ativo TINYINT      DEFAULT 1
);

CREATE TABLE IF NOT EXISTS setores (
    id   INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS produtos (
    id             INT AUTO_INCREMENT PRIMARY KEY,
    codigo         VARCHAR(20)  NOT NULL UNIQUE,
    descricao      VARCHAR(100) NOT NULL,
    categoria      VARCHAR(50)  NOT NULL,
    preco_unitario DECIMAL(10,2) NOT NULL,
    fornecedor_id  INT,
    FOREIGN KEY (fornecedor_id) REFERENCES fornecedores(id)
);

CREATE TABLE IF NOT EXISTS estoque (
    id         INT AUTO_INCREMENT PRIMARY KEY,
    produto_id INT NOT NULL,
    setor_id   INT NOT NULL,
    quantidade INT NOT NULL DEFAULT 0,
    minimo     INT NOT NULL DEFAULT 50,
    atualizado DATE DEFAULT (CURRENT_DATE),
    FOREIGN KEY (produto_id) REFERENCES produtos(id),
    FOREIGN KEY (setor_id)   REFERENCES setores(id)
);