import sys
sys.path.append("src")

from src.collectors import ProcessesCollector, CpuUsageCollector, MemoryCollector, NetInterfacesesIOCollector, DisksCollector, DataCollector
from src.db         import PostgresConfig, PostgresDatabase
from src.senders    import ProcessesSender, CpuUsageSender, MemorySender, NetInterfacesesIOSender, DisksSender, DataSender

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
    Handler("CpuUsage",     CpuUsageCollector,          CpuUsageSender,             False),
    Handler("Disks",        DisksCollector,             DisksSender,                True),
    Handler("Processes",    ProcessesCollector,         ProcessesSender,            False),
    Handler("NetIO",        NetInterfacesesIOCollector, NetInterfacesesIOSender,    True),
]


pgconfig    = PostgresConfig(dbname="savt")
pg          = PostgresDatabase(pgconfig)

while True:
    print("Сбор данных")
    for h in handlers:
        if h.active:
            h.sender.send(h.collector.collect(), pg)
    print("Сбор данных закончен")
    sleep(20)