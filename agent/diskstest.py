import sys
sys.path.append("src")

from src.collectors import DisksDataCollector
from src.db         import PostgresConfig, PostgresDatabase
from src.senders    import DisksDataSender

from time import sleep






pgconfig = PostgresConfig(dbname="savt")
pg = PostgresDatabase(pgconfig)

while True:
    DisksDataSender.send(DisksDataCollector.collect(), pg)
    sleep(20)