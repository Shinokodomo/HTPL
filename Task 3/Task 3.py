#Задание делалось на основе документации .json, не доводилось пользоваться ранее
#Для удобства запуска txt файлы находятся в той же директории, что и код
# Чтение данных из tests.json
import json
import sys

def read_json_file(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def write_json_file(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

def update_values(test, values_dict):
    if 'id' in test and test['id'] in values_dict:
        test['value'] = values_dict[test['id']]
    if 'values' in test:
        for sub_test in test['values']:
            update_values(sub_test, values_dict)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <tests_file> <values_file> <report_file>")
        sys.exit(1)

    tests_file = sys.argv[1]
    values_file = sys.argv[2]
    report_file = sys.argv[3]

    # Чтение данных из файлов
    tests_data = read_json_file(tests_file)
    values_data = read_json_file(values_file)

    # Создание словаря значений из values.json
    values_dict = {item['id']: item['value'] for item in values_data['values']}

    # Обновление значений в структуре tests_data
    for test in tests_data['tests']:
        update_values(test, values_dict)

    # Запись обновленных данных в report.json
    write_json_file(report_file, tests_data)

    print("Данные успешно обновлены и сохранены в", report_file)
