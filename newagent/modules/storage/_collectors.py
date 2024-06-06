from models             import BaseCollector
from ._models           import DiskIO, DiskInfo, DiskUsage
from psutil             import disk_io_counters, disk_partitions, disk_usage
from typing             import List


class DisksInfoCollector(BaseCollector):
    def collect(self) -> List[DiskInfo]:
        disks       = []
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
            disks.append(
                DiskInfo(
                    device      = partition_device,
                    mountpoint  = partition.mountpoint,
                    usage       = data_usage,
                    io          = data_io,
                )
            )
        return disks