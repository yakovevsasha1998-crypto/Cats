import requests

url = 'https://catfact.ninja/fact'

try:
    req = requests.get(url)
    if req.status_code == 200:
        info_json = req.json()
        fact = info_json['fact']
        #открываем  файл после успешного взятия факта
        with open('fact.txt','a',encoding='utf-8') as file:
            file.write(fact + '\n')
        print('Успешно') # успешная запись в файл
    else:
        print('Ошибка при получении факта')
except Exception:
    print('Не удалось получить fact')