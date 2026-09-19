import json

json_data = '{"name": "Иван", "age": 30, "is_student": false}'
parsed_data = json.loads(json_data)  # Преобразуем JSON-строку в Python-объект (dict)

print(parsed_data["name"])  # Выведет: Иван

with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)  # Загружаем JSON из файла
    print(data)

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)  # Сохраняем JSON в файл
