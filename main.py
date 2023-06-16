def write_json_file(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
    print("Data saved to JSON file.")

write_json_file(json_data, output_file)
