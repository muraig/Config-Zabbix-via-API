import json
import requests


def zbx_auth(auth_file):
    """Аутентификация на Zabbix-сервере"""

    # загрузить из json
    with open(auth_file, 'r', encoding='utf-8') as af:  # открываем файл на чтение
        zbx = json.load(af)  # загружаем из файла данные в словарь data

    url = f'http://{zbx["ip"]}/api_jsonrpc.php'
    headers = {'content-type': 'application/json-rpc'}
    request_json = f"""
        {{
            "jsonrpc": "2.0",
            "method": "user.login",
            "params": {{
                "user": "{zbx["login"]}",
                "password": "{zbx["password"]}"
            }},
            "id": 1,
            "auth": null
        }}
    """
    r = requests.post(url, headers=headers, data=request_json)
    return json.loads(r.content)["result"]


print(zbx_auth('zabbix.json'))
