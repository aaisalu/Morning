import requests
from pathlib import Path
import os


def read_data(data):
    if data['status']:
        full_url = data['data']['file']["url"]['full']
        unique_id = data['data']['file']["metadata"]['id']
        file_name = data['data']['file']["metadata"]['name']
        file_size = data['data']['file']["metadata"]['size']['readable']
        print(full_url, unique_id, file_name, file_size)
    else:
        error_message = data['error']['message']
        error_type = data['error']['type']
        error_code = data['error']['code']
        print(error_code, error_message, error_type)


def connect_cloud():
    file_path = input('Provide the absolute path of file: ')
    abs_path = Path(file_path).absolute()
    if abs_path.is_file():
        url = f"https://api.anonfiles.com/upload"
        open_file = open(abs_path, "rb")
        files = {'file': open_file}
        raw_data = requests.post(url, files=files).json()
        return read_data(raw_data)
    else:
        return print("Please provide the absolute path of the file: ")


connect_cloud()
