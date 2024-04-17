import sys
sys.path.append("src")

from src.collectors import SwapMemoryDataCollector, RamMemoryDataCollector
from src.db         import PostgresConfig, PostgresDatabase
from src.senders    import SwapMemoryDataSender, RamMemoryDataSender

from time import sleep, perf_counter






pgconfig = PostgresConfig(dbname="savt")
pg = PostgresDatabase(pgconfig)

while True:
    swap_sender = SwapMemoryDataSender.send(SwapMemoryDataCollector.collect(), pg)
    ram_sender = RamMemoryDataSender.send(RamMemoryDataCollector.collect(), pg)
    sleep(60)