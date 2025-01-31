from .basecollector     import DataCollector
from ..data             import DiskIO, Disk, DiskUsage
from psutil             import disk_io_counters, disk_partitions, disk_usage
from typing             import List


class DisksCollector(DataCollector):
    def collect() -> List[Disk]:
        disksdata   = []
        partitions  = disk_partitions(all=False)
        io          = disk_io_counters(perdisk=True)

        for partition in partitions:
            partition_usage     = disk_usage(partition.mountpoint)
            partition_device    = partition.device.rsplit("/")[-1]
            partition_io        = io.get(partition_device)

            data_usage = DiskUsage(
                total   = partition_usage.total,
                used    = partition_usage.used,
                free    = partition_usage.free,
                percent = partition_usage.percent
            )
            data_io = DiskIO(
                read_count  = partition_io.read_count   if partition_io else 0,
                write_count = partition_io.write_count  if partition_io else 0,
                read_bytes  = partition_io.read_bytes   if partition_io else 0,
                write_bytes = partition_io.write_bytes  if partition_io else 0,
            )
            disksdata.append(
                Disk(
                    device      = partition_device,
                    mountpoint  = partition.mountpoint,
                    usage       = data_usage,
                    io          = data_io,
                )
            )
        return disksdata