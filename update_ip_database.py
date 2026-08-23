import json
import requests

# Загружаем базу IP
response = requests.get('https://ipapi.co/json/')
data = response.json()

# Сохраняем в JSON файл
with open('ip_data.json', 'w') as f:
    json.dump(data, f, indent=2)

# Генерируем JavaScript файл
with open('ip_data.js', 'w') as f:
    f.write(f"const IP_DATA = {json.dumps(data)};")
