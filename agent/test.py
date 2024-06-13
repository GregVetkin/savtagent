from agent._models          import HandlerData, DataSender
from agent._handler         import Handler
from database.postgresql    import PostgreSQL, PostgresConfig
 


class MemorySender(DataSender):
    def __init__(self, database):
        self._db = database

    def send(self, data):
        self._db._connect()
        # Запись в нужную таблцицу данные
        print(data["ram"])
        print(data["swap"])
        self._db._close()




db_config = PostgresConfig()
pgdb = PostgreSQL(db_config)

PORT = 8081

class HandlerFactory:
    def __init__(self) -> None:
        pass

    def get_handler(self, route: str):
        return HandlerData(
            url = "http://127.0.0.1:" + PORT + route,
            active = True,
        )


memory = HandlerData(
    url     = "http://127.0.0.1:8081/memory",
    active  = True,
    sender  = MemorySender(pgdb),
)



memory_handler = Handler(memory)
memory_handler.handle()
