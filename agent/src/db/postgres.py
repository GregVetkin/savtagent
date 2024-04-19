import psycopg2

from typing             import List
from .basedb            import Database
from dataclasses        import dataclass
from ..data             import CpuUsage, Memory, Disk, Process, NetInterfaceIO


@dataclass
class PostgresConfig:
    host:      str      = 'localhost'
    port:      int      =  5432
    user:      str      = 'postgres'
    password:  str      = 'postgres'
    dbname:    str      = 'postgres'



class PostgresDatabase(Database):
    def __init__(self, config: PostgresConfig):
        self.__dbname     = config.dbname
        self.__user       = config.user
        self.__password   = config.password
        self.__host       = config.host
        self.__port       = config.port
        self.connection   = None
        self.cursor       = None

        self.dev_id       = 5
    
    def connect(self):
        try:
            self.connection = psycopg2.connect(
                dbname=     self.__dbname,
                user=       self.__user,
                password=   self.__password,
                host=       self.__host,
                port=       self.__port
            )
            self.cursor = self.connection.cursor()
        except psycopg2.Error as e:
            pass
    
    def disconnect(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()

    def save_memory_data(self, memory: Memory):
        if not self.connection:
            self.connect()
        with self.connection:
            with self.connection.cursor() as cursor:
                sql = """
                DELETE FROM 
                agent.memory WHERE dev_id = %s;
                """
                cursor.execute(sql, (self.dev_id, ))
                sql = """
                INSERT INTO 
                agent.memory (dev_id, 
                ram_total, ram_available, ram_used, ram_percent,
                swap_total, swap_free, swap_used, swap_percent)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
                """
                cursor.execute(sql, (self.dev_id,
                                     memory.ram.total, memory.ram.available, memory.ram.used, memory.ram.percent,
                                     memory.swap.total, memory.swap.free, memory.swap.used, memory.swap.percent))


    
    # def save_ram_data(self, ram: RamMemoryData):
    #     if not self.connection:
    #         self.connect()
    #     with self.connection:
    #         with self.connection.cursor() as cursor:
    #             sql = """
    #             DELETE FROM 
    #             agent.memory WHERE dev_id = %s;
    #             """
    #             cursor.execute(sql, (self.dev_id, ))

    #             sql = """
    #             INSERT INTO 
    #             agent.memory_ram (dev_id, total, available, used, percent)
    #             VALUES (%s, %s, %s, %s, %s);
    #             """
    #             cursor.execute(sql, (self.dev_id, ram.total, ram.available, ram.used, ram.percent))
        

    # def save_swap_data(self, swap: SwapMemoryData):
    #     if not self.connection:
    #         self.connect()
    #     with self.connection:
    #         with self.connection.cursor() as cursor:
    #             sql = """
    #             DELETE FROM 
    #             agent.memory_swap WHERE dev_id = %s;
    #             """
    #             cursor.execute(sql, (self.dev_id, ))
    #             sql = """
    #             INSERT INTO 
    #             agent.memory_swap (dev_id, total, free, used, percent)
    #             VALUES (%s, %s, %s, %s, %s);
    #             """
    #             cursor.execute(sql, (self.dev_id, swap.total, swap.free, swap.used, swap.percent))

    
    def save_cpu_usage_data(self, cpu: CpuUsage):
        if not self.connection:
            self.connect()
        with self.connection:
            with self.connection.cursor() as cursor:
                sql = """
                DELETE FROM 
                agent.cpu_usage WHERE dev_id = %s;
                """
                cursor.execute(sql, (self.dev_id, ))

                sql = """
                INSERT INTO 
                agent.cpu_usage (dev_id, cores, mean)
                VALUES (%s, %s, %s);
                """
                cursor.execute(sql, (self.dev_id, cpu.cores, cpu.mean))


    def save_disks_data(self, disks: List[Disk]):
        if not self.connection:
            self.connect()
        with self.connection:
            with self.connection.cursor() as cursor:
                sql = """
                DELETE FROM 
                agent.disks WHERE dev_id = %s;
                """
                cursor.execute(sql, (self.dev_id, ))

                sql = """
                INSERT INTO agent.disks (dev_id, device, mountpoint, total_usage, used_usage, free_usage, percent_usage, read_count, write_count, read_bytes, write_bytes)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                vars_list = [
                    (   
                        self.dev_id,
                        disk.device,
                        disk.mountpoint,
                        disk.usage.total,
                        disk.usage.used,
                        disk.usage.free,
                        disk.usage.percent,
                        disk.io.read_count,
                        disk.io.write_count,
                        disk.io.read_bytes,
                        disk.io.write_bytes
                    ) for disk in disks
                ]
                cursor.executemany(sql, vars_list)
    

    def save_processes_data(self, processes: List[Process]):
        if not self.connection:
            self.connect()
        with self.connection:
            with self.connection.cursor() as cursor:
                sql = """
                DELETE FROM 
                agent.processes WHERE dev_id = %s;
                """
                cursor.execute(sql, (self.dev_id, ))

                sql = """
                INSERT INTO agent.processes (dev_id, pid, name, username, status, memory_usage, cpu_usage)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                vars_list = [
                    (   
                        self.dev_id,
                        p.pid,
                        p.name,
                        p.user,
                        p.status,
                        p.memory_usage,
                        p.cpu_usage,
                    ) for p in processes
                ]
                cursor.executemany(sql, vars_list)

    
    def save_net_io_data(self, net_io: List[NetInterfaceIO]):
        if not self.connection:
            self.connect()
        with self.connection:
            with self.connection.cursor() as cursor:
                sql = """
                DELETE FROM 
                agent.net_io WHERE dev_id = %s;
                """
                cursor.execute(sql, (self.dev_id, ))

                sql = """
                INSERT INTO agent.net_io (dev_id, interface, bytes_sent, bytes_recv, packets_sent, packets_recv)
                VALUES (%s, %s, %s, %s, %s, %s)
                """
                vars_list = [
                    (   
                        self.dev_id,
                        io.interface,
                        io.bytes_sent,
                        io.bytes_recv,
                        io.packets_sent,
                        io.packets_recv,
                    ) for io in net_io
                ]
                cursor.executemany(sql, vars_list)


