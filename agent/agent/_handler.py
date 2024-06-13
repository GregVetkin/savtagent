from ._models import HandlerData
import requests




class Handler:
    def __init__(self, data: HandlerData) -> None:
        self._data = data

    def _collect_data(self):
        response = requests.get(self._data.url)
        if response.status_code == 200:
            self._data.data = response.json()
        

    def handle(self):
        if self._data.active:
            self._collect_data()
        if not self._data.error:
            self._data.sender.send(self._data.data)
        else:
            raise Exception(self._data.error)
            # логировать ошибку или передать в верхний обработчик raise исключение, чтобы обработчик верхнего уровня залогировал




