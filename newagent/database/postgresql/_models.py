from dataclasses import dataclass


@dataclass
class PostgresConfig:
    database:   str = "postgres"
    username:   str = "postgres"
    passowrd:   str = "postgres"
    host:       str = "localhost"
    port:       int = 5432

