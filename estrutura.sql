DROP DATABASE IF EXISTS poke_battle;

CREATE DATABASE poke_battle;

USE poke_battle;

CREATE TABLE categorias(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(20) NOT NULL
);

CREATE TABLE pokemons (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(40) NOT NULL,
    descricao TEXT,
    numero CHAR(4) NOT NULL,
    id_categoria INT,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id),

    vida FLOAT NOT NULL,
    forca_ataque FLOAT NOT NULL,
    registro_ativo BIT NOT NULL DEFAULT(1)
);