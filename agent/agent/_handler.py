from database._database     import Database
from dataclasses            import dataclass
from ._sender               import DataSender, ROUTE_TO_SENDER
import requests



@dataclass
class HandlerData:
    url:        str
    sender:     DataSender
    data:       str         = ""
    error:      str         = ""




class Handler:
    def __init__(self, data: HandlerData) -> None:
        self._data = data


    def _collect_data(self):
        response = requests.get(self._data.url)
        if response.status_code == 200:
            self._data.data = response.json()
        else:
            self._data.error = response.json()
        

    def handle(self):
        self._collect_data()
        if not self._data.error:
            self._data.sender.send(self._data.data)
        else:
            raise Exception(self._data.error)




class HandlerFactory:
    def __init__(self, database: Database, api: str) -> None:
        self._db        = database
        self._api_url   = api


    def get_handler(self, route: str):
        return Handler(self._get_handler_data(route))


    def _get_handler_data(self, route: str) -> HandlerData:
        return HandlerData(
            url     = self._api_url + route,
            sender  = self._get_sender(route),
        )
    

    def _get_sender(self, route: str):
        if route in ROUTE_TO_SENDER:
            return ROUTE_TO_SENDER[route](self._db)