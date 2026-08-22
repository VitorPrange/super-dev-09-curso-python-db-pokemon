from mysql.connector import connect
from mysql.connector.abstracts import MySQLConnectionAbstract

from src.settings.settings import settings


def conectar() -> MySQLConnectionAbstract:
    """Abre uma conexão nova. Quem chama é responsavel por fechar (use `with`)."""
    
    return connect(
        host=settings.db_host,
        port=settings.db_port,
        user=settings.db_user,
        password=settings.db_password,
        database=settings.db_name,
    )
