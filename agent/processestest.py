import sys
sys.path.append("src")

from src.collectors import ProcessesDataCollector
from src.db         import PostgresConfig, PostgresDatabase
from src.senders    import ProcessesDataSender

from time import sleep






pgconfig = PostgresConfig(dbname="savt")
pg = PostgresDatabase(pgconfig)

while True:
    ProcessesDataSender.send(ProcessesDataCollector.collect(), pg)
    sleep(20)