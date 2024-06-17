from database.postgresql    import PostgreSQL, PostgresConfig
from agent._handler         import HandlerFactory







db_config   = PostgresConfig()
pgdb        = PostgreSQL(db_config)



factory = HandlerFactory(pgdb, "http://127.0.0.1:8081")



memory_handler = factory.get_handler("/memory")
memory_handler.handle()
# обработчик получит данные по запросу /memory и передаст их дальше на обработку (запись в бд или запись в файл директории)