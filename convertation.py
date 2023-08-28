import json
import csv


def convert_csv_to_json(csv_file, json_file):
    with open(csv_file, 'r', encoding='UTF-8') as data_csv:
        data = csv.DictReader(data_csv)

        new_data = [{'fields': {field: row[field] for field in data.fieldnames}} for row in data]

    with open(json_file, 'w', encoding='UTF-8') as file:
        json.dump(new_data, file, ensure_ascii=False)


if __name__ == '__main__':
    csv_f_1 = 'datasets/ads.csv'
    csv_f_2 = 'datasets/categories.csv'
    convert_csv_to_json(csv_f_1, 'ads.json')
    convert_csv_to_json(csv_f_2, 'datasets.json')
