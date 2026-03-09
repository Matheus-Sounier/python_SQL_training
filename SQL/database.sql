CREATE DATABASE IF NOT EXISTS flex_treino
DEFAULT CHARACTER SET utf8mb4
DEFAULT COLLATE utf8mb4_general_ci;

USE flex_treino;

CREATE TABLE IF NOT EXISTS fornecedores (
    id    INT AUTO_INCREMENT PRIMARY KEY,
    nome  VARCHAR(100) NOT NULL,
    pais  VARCHAR(50)  NOT NULL,
    ativo TINYINT      DEFAULT 1
) DEFAULT charset = utf8mb4;

CREATE TABLE IF NOT EXISTS setores (
    id   INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL
) DEFAULT charset = utf8mb4;

CREATE TABLE IF NOT EXISTS produtos (
    id             INT AUTO_INCREMENT PRIMARY KEY,
    codigo         VARCHAR(20)  NOT NULL UNIQUE,
    descricao      VARCHAR(100) NOT NULL,
    categoria      VARCHAR(50)  NOT NULL,
    preco_unitario DECIMAL(10,2) NOT NULL,
    fornecedor_id  INT,
    FOREIGN KEY (fornecedor_id) REFERENCES fornecedores(id)
) DEFAULT charset = utf8mb4;

CREATE TABLE IF NOT EXISTS estoque (
    id         INT AUTO_INCREMENT PRIMARY KEY,
    produto_id INT NOT NULL,
    setor_id   INT NOT NULL,
    quantidade INT NOT NULL DEFAULT 0,
    minimo     INT NOT NULL DEFAULT 50,
    atualizado DATE DEFAULT (CURRENT_DATE),
    FOREIGN KEY (produto_id) REFERENCES produtos(id),
    FOREIGN KEY (setor_id)   REFERENCES setores(id)
) DEFAULT charset = utf8mb4;

CREATE TABLE IF NOT EXISTS pedidos (
    id            INT AUTO_INCREMENT PRIMARY KEY,
    produto_id    INT         NOT NULL,
    fornecedor_id INT         NOT NULL,
    quantidade    INT         NOT NULL,
    status        VARCHAR(20) DEFAULT 'pendente',
    data_pedido   DATE        DEFAULT (CURRENT_DATE),
    data_entrega  DATE,
    FOREIGN KEY (produto_id)    REFERENCES produtos(id),
    FOREIGN KEY (fornecedor_id) REFERENCES fornecedores(id)
) DEFAULT charset = utf8mb4;

CREATE TABLE IF NOT EXISTS producao (
    id        INT AUTO_INCREMENT PRIMARY KEY,
    setor_id  INT        NOT NULL,
    data      DATE       NOT NULL,
    meta      INT        NOT NULL,
    realizado INT        NOT NULL,
    turno     VARCHAR(10) NOT NULL,
    FOREIGN KEY (setor_id) REFERENCES setores(id)
) DEFAULT charset = utf8mb4;

CREATE TABLE IF NOT EXISTS alunos(
	id     INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	nome   VARCHAR(100) NOT NULL,
	status VARCHAR(100) NOT NULL DEFAULT 'desconhecido'
) DEFAULT charset = utf8mb4;

CREATE TABLE IF NOT EXISTS professores (
	id         INT          NOT NULL AUTO_INCREMENT PRIMARY KEY,
	nome       VARCHAR(100) NOT NULL DEFAULT 'desconhecido',
	quantidade INT          NULL
) DEFAULT charset = utf8mb4;

INSERT INTO professores (id, nome, quantidade) VALUES
    (DEFAULT, 'matheus', 10),
    (DEFAULT, 'salomão', 20),
    (DEFAULT, 'silas',   30),
    (DEFAULT, 'paulo',   32),
    (DEFAULT, 'isaac',   12),
    (DEFAULT, 'joão',    54),
    (DEFAULT, 'pedro',   23),
    (DEFAULT, 'jorge',   12);

INSERT INTO alunos (id, nome, status) VALUES
    (DEFAULT, 'matheus', 'vivo'),
    (DEFAULT, 'salomão', 'morto'),
    (DEFAULT, 'silas',   'morto'),
    (DEFAULT, 'paulo',   'vivo'),
    (DEFAULT, 'isaac',   'morto'),
    (DEFAULT, 'pedro',   'morto'),
    (DEFAULT, 'joão',    'vivo'),
    (DEFAULT, 'jorge',   'vivo'),
    (DEFAULT, 'joão',    'vivo'),
    (DEFAULT, 'jorge',   'vivo'),
    (DEFAULT, 'joão',    'vivo'),
    (DEFAULT, 'jorge',   'vivo');

INSERT INTO fornecedores (nome, pais) VALUES
    ('Samsung Electronics',  'Coreia do Sul'),
    ('Foxconn',              'Taiwan'),
    ('Molex',                'EUA'),
    ('TE Connectivity',      'Suica'),
    ('Murata Manufacturing', 'Japao'),
    ('TDK Corporation',      'Japao'),
    ('Amphenol',             'EUA'),
    ('Vishay',               'EUA');

INSERT INTO setores (nome) VALUES
    ('SMT'),
    ('Montagem'),
    ('Teste'),
    ('Logistica'),
    ('Qualidade');

INSERT INTO produtos (codigo, descricao, categoria, preco_unitario, fornecedor_id) VALUES
    ('COMP-001', 'Resistor 10k',           'Passivo',   0.05,  8),
    ('COMP-002', 'Capacitor 100uF',        'Passivo',   0.12,  5),
    ('COMP-003', 'Transistor NPN BC547',   'Ativo',     0.30,  8),
    ('COMP-004', 'Conector USB-C',         'Conector',  1.20,  3),
    ('COMP-005', 'Microcontrolador STM32', 'CI',        4.50,  1),
    ('COMP-006', 'LED RGB 5mm',            'Ativo',     0.08,  6),
    ('COMP-007', 'Modulo WiFi ESP8266',    'CI',        2.80,  2),
    ('COMP-008', 'Cabo Flat 20 vias',      'Conector',  0.75,  7),
    ('COMP-009', 'Indutor 47uH',           'Passivo',   0.22,  6),
    ('COMP-010', 'Cristal 16MHz',          'Passivo',   0.45,  5),
    ('COMP-011', 'Conector RJ45',          'Conector',  0.90,  4),
    ('COMP-012', 'Regulador 7805',         'Ativo',     0.60,  8),
    ('COMP-013', 'Display OLED 0.96',      'Display',   3.20,  2),
    ('COMP-014', 'Sensor Temperatura',     'Sensor',    1.80,  5),
    ('COMP-015', 'Fusivel 2A',             'Protecao',  0.10,  7);

INSERT INTO estoque (produto_id, setor_id, quantidade, minimo) VALUES
    (1,  1, 5000, 1000),
    (2,  1,  800,  500),
    (3,  1,  120,  200),
    (5,  1,   45,  100),
    (6,  1, 2200,  500),
    (9,  1,  300,  200),
    (10, 1,   30,  100),
    (4,  2,  150,   50),
    (7,  2,   80,  100),
    (8,  2,  400,  100),
    (11, 2,  220,   50),
    (13, 2,   15,   30),
    (14, 3,   60,   50),
    (15, 3,  500,  200),
    (1,  4, 10000, 2000),
    (2,  4, 3000,  500),
    (4,  4,  600,  100),
    (12, 4,  180,  100),
    (3,  5,   25,   50),
    (6,  5,  100,  100),
    (15, 5,  300,  100);

INSERT INTO pedidos (produto_id, fornecedor_id, quantidade, status, data_pedido, data_entrega) VALUES
    (5,  1, 500,  'entregue',   '2024-11-01', '2024-11-10'),
    (7,  2, 300,  'entregue',   '2024-11-05', '2024-11-18'),
    (3,  8, 1000, 'entregue',   '2024-11-10', '2024-11-20'),
    (13, 2, 100,  'em_transito','2024-12-01', '2024-12-15'),
    (5,  1, 200,  'em_transito','2024-12-03', '2024-12-18'),
    (10, 5, 500,  'pendente',   '2024-12-05', NULL),
    (3,  8, 800,  'pendente',   '2024-12-06', NULL),
    (4,  3, 400,  'pendente',   '2024-12-07', NULL),
    (14, 5, 200,  'cancelado',  '2024-11-15', NULL),
    (1,  8, 5000, 'entregue',   '2024-10-20', '2024-10-30');

INSERT INTO producao (setor_id, data, meta, realizado, turno) VALUES
    (1, '2024-12-01', 1000,  980, 'manha'),
    (1, '2024-12-01',  900,  870, 'tarde'),
    (1, '2024-12-02', 1000, 1020, 'manha'),
    (1, '2024-12-02',  900,  750, 'tarde'),
    (2, '2024-12-01',  500,  490, 'manha'),
    (2, '2024-12-01',  500,  510, 'tarde'),
    (2, '2024-12-02',  500,  430, 'manha'),
    (2, '2024-12-02',  500,  500, 'tarde'),
    (3, '2024-12-01',  300,  295, 'manha'),
    (3, '2024-12-01',  300,  310, 'tarde'),
    (3, '2024-12-02',  300,  280, 'manha'),
    (3, '2024-12-02',  300,  300, 'tarde'),
    (1, '2024-12-03', 1000,  960, 'manha'),
    (2, '2024-12-03',  500,  520, 'manha'),
    (3, '2024-12-03',  300,  290, 'manha');