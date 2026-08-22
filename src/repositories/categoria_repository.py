from src.database.conexao import conectar
from src.schemas.categoria import Categoria
from typing import List


def consultar_todos() -> List[Categoria]:
    #with garante que as coisas que precisam ser abertas sejam fechadas sem pecisar de close() independente se deu erro ou não
    #isso evita que requisções deixem conexões abertas
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                "SELECT id, nome FROM categorias"
            )
            
            registros = cursor.fetchall()
        
        categorias = []
        
        for registro in registros:
            categoria = Categoria(id=registro["id"], nome=registro["nome"])
            categorias.append(categoria)
        return categorias
