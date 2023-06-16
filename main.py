import json

def load_json(file_path):
    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
            return data
        except json.JSONDecodeError as e:
            print(f'Błąd parsowania pliku JSON: {e}')
            return None

file_path = 'plik.json'
data = load_json(file_path)
if data:
    # Przetwarzanie danych
    print(data)
