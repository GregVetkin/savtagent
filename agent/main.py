import sys
sys.path.append("src")

from src.collectors import NetInterfacesesIODataCollector as NetIoCollector
from src.db         import PostgresConfig, PostgresDatabase
from src.senders    import NetInterfacesesIODataSender as NetIoSender

from time import sleep






pgconfig = PostgresConfig(dbname="savt")
pg = PostgresDatabase(pgconfig)

while True:
    NetIoSender.send(NetIoCollector.collect(), pg)
    sleep(20)