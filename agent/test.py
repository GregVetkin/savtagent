import sys
sys.path.append("src")

from src.collectors import ProcessesCollector, CpuUsageCollector, MemoryCollector, NetInterfacesesIOCollector, DisksCollector, DataCollector, NetConnectionsCollector
from src.db         import PostgresConfig, PostgresDatabase
from src.senders    import ProcessesSender, CpuUsageSender, MemorySender, NetInterfacesesIOSender, DisksSender, DataSender, NetConnectionsSender

from time import sleep
from dataclasses import dataclass


@dataclass
class Handler:
    name:       str
    collector:  DataCollector
    sender:     DataSender
    active:     bool

handlers = [
    Handler("Memory",       MemoryCollector,            MemorySender,               True),
    Handler("CpuUsage",     CpuUsageCollector,          CpuUsageSender,             True),
    Handler("Disks",        DisksCollector,             DisksSender,                True),
    Handler("Processes",    ProcessesCollector,         ProcessesSender,            True),
    Handler("NetIO",        NetInterfacesesIOCollector, NetInterfacesesIOSender,    True),
    Handler("Connections",  NetConnectionsCollector,    NetConnectionsSender,       True),
]


pgconfig    = PostgresConfig(dbname="savt")
pg          = PostgresDatabase(pgconfig)

while True:
    print("Сбор данных")
    print("_"*40)

    for h in handlers:
        if h.active:
            print(f"Сбор данных в {h.name}")
            h.sender.send(h.collector.collect(), pg)
            print(f"Данные {h.name} переданы")
            
    print("_"*40)
    print("Сбор данных закончен")
    sleep(20)