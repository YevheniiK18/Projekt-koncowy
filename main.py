def write_json_file(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print("Dane zapisane do pliku JSON.")
    except IOError as e:
        print(f"Błąd zapisu do pliku JSON: {e}")

write_json_file(json_data, output_file)
