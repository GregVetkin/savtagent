import sys
sys.path.append("src")



import json
from src.collectors import MemoryCollector




# Создаем объект класса данных
person = MemoryCollector.collect()



json_string = json.dumps(person.__dict__, default=lambda x: x.__dict__)

# Создаем или открываем файл для записи
with open("person.json", "w") as json_file:
    # Сохраняем объект в JSON-файл
    json.dump(person.__dict__, json_file, default=lambda x: x.__dict__)
