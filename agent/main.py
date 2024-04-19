import sys
sys.path.append("src")

from src.collectors import NetInterfacesesIOCollector
from src.db         import PostgresConfig, PostgresDatabase
from src.senders    import NetInterfacesesIOSender

from time import sleep






pgconfig = PostgresConfig(dbname="savt")
pg = PostgresDatabase(pgconfig)

