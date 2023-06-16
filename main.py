import argparse
import json
import yaml
import xml.etree.ElementTree as ET
import tkinter as tk
import asyncio
import threading


def parse_arguments():
    parser = argparse.ArgumentParser(description='Opis programu.')
    parser.add_argument('--option1', help='Opis opcji 1')
    parser.add_argument('--option2', help='Opis opcji 2')
    args = parser.parse_args()

    if args.option1:
        print(f'Opcja 1: {args.option1}')
    if args.option2:
        print(f'Opcja 2: {args.option2}')


def load_json(file_path):
    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
            return data
        except json.JSONDecodeError as e:
            print(f'Błąd parsowania pliku JSON: {e}')
            return None


def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def load_yaml(file_path):
    with open(file_path, 'r') as file:
        try:
            data = yaml.safe_load(file)
            return data
        except yaml.YAMLError as e:
            print(f'Błąd parsowania pliku YAML: {e}')
            return None


def save_yaml(data, file_path):
    with open(file_path, 'w') as file:
        yaml.dump(data, file)


def load_xml(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        return root
    except ET.ParseError as e:
        print(f'Błąd parsowania pliku XML: {e}')
        return None


def save_xml(data, file_path):
    tree = ET.ElementTree(data)
    with open(file_path, 'wb') as file:
        tree.write(file)


def on_button_click():
    print('Kliknięto przycisk')


def create_ui():
    root = tk.Tk()
    button = tk.Button(root, text='Kliknij mnie', command=on_button_click)
    button.pack()
    root.mainloop()


def load_file_async(file_path):
    data = {'klucz': 'wartość'}
    return data


def save_file_async(data, file_path):
    print(f'Zapisano dane do pliku: {file_path}')


async def async_file_operations(file_path):
    loop = asyncio.get_event_loop()
    load_task = loop.run_in_executor(None, load_file_async, file_path)
    data = await load_task
    save_task = loop.run_in_executor(None, save_file_async, data, file_path)
    await save_task


def main():
    parse_arguments()
    json_data = load_json('plik.json')
    if json_data:
        print(json_data)
    data_to_save = {'klucz': 'wartość'}
    save_json(data_to_save, 'nowy_plik.json')
    yaml_data = load_yaml('plik.yml')
    if yaml_data:
        print(yaml_data)
    data_to_save = {'klucz': 'wartość'}
    save_yaml(data_to_save, 'nowy_plik.yml')
    xml_data = load_xml('plik.xml')
    if xml_data:
        print(xml_data)
    data_to_save = ET.Element('root')
    child = ET.SubElement(data_to_save, 'child')
    child.text = 'Tekst'
    save_xml(data_to_save, 'nowy_plik.xml')
    create_ui()
    file_path = 'plik.json'
    asyncio.run(async_file_operations(file_path))


if __name__ == '__main__':
    main()
