import json


def load_data(filepath):
    with open(filepath, encoding='UTF-8') as file:
        data = json.load(file)
    print(data)


if __name__ == '__main__':
    load_data('ads.json')
