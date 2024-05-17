import requests
import json
from datetime import datetime





def json_data_wrapper(url):
    url = "http://localhost:8081" + url

    response = requests.get(url)

    metadata = {
        "url":  url,
        "statuscode": response.status_code,
        "time": datetime.now().isoformat(),
    }

    if response.status_code == 200:
        data = response.json()
    else:
        data = None

    wrapped_data = {
        "metadata": metadata,
        "data": data
    }
    return wrapped_data


url = "/memory"

wrapped_data = json_data_wrapper(url)
#print(json.dumps(wrapped_data, indent=4))


from agent.src.data.memorydata import Memory,RamMemory, SwapMemory


# Создание экземпляра датакласса из словаря
data_instance = Memory(ram=RamMemory(**wrapped_data["data"]["ram"]), swap=SwapMemory(**wrapped_data["data"]["swap"]))

print(data_instance)  # Вывод: MyDataClass(field1='value1', field2=42)
print(data_instance.ram.available)