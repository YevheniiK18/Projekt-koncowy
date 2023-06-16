import json

data = {'klucz': 'wartość'}

def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

file_path = 'plik.json'
save_json(data, file_path)
