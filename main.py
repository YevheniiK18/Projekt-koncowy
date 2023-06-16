def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Błąd odczytu pliku JSON: {e}")
        return None

json_data = read_json_file(input_file)
if json_data is None:
    sys.exit(1)
