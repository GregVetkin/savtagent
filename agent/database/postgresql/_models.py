from dataclasses import dataclass


@dataclass
class PostgresConfig:
    """Класс данных для подключения к Postgresql"""

    database:   str = "postgres"
    username:   str = "postgres"
    passowrd:   str = "postgres"
    host:       str = "localhost"
    port:       int = 5432

