import json
#Задание делалось на основе документации .json, не доводилось пользоваться ранее
# Чтение данных из tests.json
with open('tests.json', 'r') as f:
    tests_data = json.load(f)

# Чтение данных из values.json
with open('values.json', 'r') as f:
    values_data = json.load(f)

# Создание словаря
values_dict = {item['id']: item['value'] for item in values_data['values']}

def update_values(test):
    if 'id' in test and test['id'] in values_dict:
        test['value'] = values_dict[test['id']]
    if 'values' in test:
        for sub_test in test['values']:
            update_values(sub_test)

# Обновление значений в tests_data
for test in tests_data['tests']:
    update_values(test)

# Запись обновленных данных в report.json
with open('report.json', 'w') as f:
    json.dump(tests_data, f, indent=4) # 4 строки, взял с документации

print("Данные успешно обновлены и сохранены в report.json")