import sys
sys.path.append("src")

from src.collectors import MemoryDataCollector
from src.db         import PostgresConfig, PostgresDatabase
from src.senders    import MemoryDataSender

from time import sleep



pgconfig = PostgresConfig(dbname="savt")
pg = PostgresDatabase(pgconfig)

while True:
    MemoryDataSender.send(MemoryDataCollector.collect(), pg)
    sleep(60)