def read_json_file(file_path):
    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
            return data
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON file: {e}")
            return None

json_data = read_json_file(input_file)
if json_data is None:
    sys.exit(1)
