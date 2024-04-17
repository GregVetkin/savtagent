import psycopg2

from .basedb         import Database
from dataclasses    import dataclass
from src.collectors   import RamMemoryData, SwapMemoryData


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

        self.dev_id = 5
    
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

    
    def save_ram_data(self, ram: RamMemoryData):
        if not self.connection:
            self.connect()
        with self.connection:
            with self.connection.cursor() as cursor:
                sql = """
                DELETE FROM 
                agent.memory_ram WHERE dev_id = %s;
                """
                cursor.execute(sql, (self.dev_id, ))

                sql = """
                INSERT INTO 
                agent.memory_ram (dev_id, total, available, used, percent)
                VALUES (%s, %s, %s, %s, %s);
                """
                cursor.execute(sql, (self.dev_id, ram.total, ram.available, ram.used, ram.percent))
        

    def save_swap_data(self, swap: SwapMemoryData):
        if not self.connection:
            self.connect()
        with self.connection:
            with self.connection.cursor() as cursor:
                sql = """
                DELETE FROM 
                agent.memory_swap WHERE dev_id = %s;
                """
                cursor.execute(sql, (self.dev_id, ))
                sql = """
                INSERT INTO 
                agent.memory_swap (dev_id, total, free, used, percent)
                VALUES (%s, %s, %s, %s, %s);
                """
                cursor.execute(sql, (self.dev_id, swap.total, swap.free, swap.used, swap.percent))