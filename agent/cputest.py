import sys
sys.path.append("src")

from src.collectors import CpuUsageDataCollector
from src.db         import PostgresConfig, PostgresDatabase
from src.senders    import CpuUsageDataSender

from time import sleep






pgconfig = PostgresConfig(dbname="savt")
pg = PostgresDatabase(pgconfig)

while True:
    cpu_sender = CpuUsageDataSender.send(CpuUsageDataCollector.collect(), pg)
    sleep(5)