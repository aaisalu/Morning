import requests
from pathlib import Path
from termcolor import cprint
import colorama
import pyperclip
import helper_func
colorama.init()


def read_data(data):
    if data['status']:
        full_url = data['data']['file']["url"]['full']
        shrink_url = helper_func.shrink_it(full_url)
        unique_id = data['data']['file']["metadata"]['id']
        file_name = data['data']['file']["metadata"]['name']
        file_size = data['data']['file']["metadata"]['size']['readable']
        pyperclip.copy(full_url)
        table = [[unique_id, file_name, shrink_url, file_size]]
        headers = ["Unique ID", "File Name",
                   "Download Link", "Size"]
        helper_func.tabuate_it(table, headers, 'green')
    else:
        error_read(data)


def error_read(data):
    error_code = data['error']['code']
    error_message = data['error']['message']
    error_type = data['error']['type']
    table = [[error_code, error_type, error_message]]
    headers = ["Error Code", "Type",
               "Message"]
    return helper_func.tabuate_it(table, headers, 'red')


def connect_cloud():
    file_paths = input(
        'Provide the absolute path of file: ').strip('"').split("|")
    try:
        for filepath in file_paths:
            abs_path = Path(filepath).absolute()
            file_size = round(Path(abs_path).stat().st_size / (1024 * 1024))
            if abs_path.is_file():
                if file_size <= 4999:
                    url = f"https://api.anonfiles.com/upload"
                    open_file = open(abs_path, "rb")
                    files = {'file': open_file}
                    raw_data = requests.post(url, files=files).json()
                    read_data(raw_data)
                else:
                    return cprint(f"Oops!.. The file is too large...Max file size is 5 GiB so, trim your extra {abs(5000-file_size)} MB from your file to upload", 'red')
            else:
                return cprint("Please provide the absolute path of the file to upload", 'red')
    except (FileNotFoundError, OSError):
        return cprint("The system couldn't find the file that you specified", 'red')


connect_cloud()
