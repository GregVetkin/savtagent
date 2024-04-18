import sys
sys.path.append("src")

from src.collectors import DisksDataCollector
from src.db         import PostgresConfig, PostgresDatabase
from src.senders    import CpuUsageDataSender

from time import sleep






pgconfig = PostgresConfig(dbname="savt")
pg = PostgresDatabase(pgconfig)

while True:
    for disk in DisksDataCollector.collect():
        print(disk)
    sleep(20)