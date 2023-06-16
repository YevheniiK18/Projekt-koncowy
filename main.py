import asyncio
import threading

def load_file_async(file_path):
    # Symulacja operacji wczytywania pliku
    # Można użyć wcześniej przedstawionych funkcji wczytywania
    data = {'klucz': 'wartość'}
    return data

def save_file_async(data, file_path):
    # Symulacja operacji zapisu pliku
    # Można użyć wcześniej przedstawionych funkcji zapisu
    print(f'Zapisano dane do pliku: {file_path}')

async def async_file_operations(file_path):
    loop = asyncio.get_event_loop()

    # Wczytywanie pliku asynchronicznie
    load_task = loop.run_in_executor(None, load_file_async, file_path)
    data = await load_task

    # Zapis pliku asynchronicznie
    save_task = loop.run_in_executor(None, save_file_async, data, file_path)
    await save_task

file_path = 'plik.json'
asyncio.run(async_file_operations(file_path))
