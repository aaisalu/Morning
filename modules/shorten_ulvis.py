import requests
import helper_func
import sys
import pyperclip
from tabulate import tabulate
from termcolor import cprint
import colorama
import pwinput
colorama.init()

utvis_api = "https://ulvis.net/API/write/get?"


def extract_data(get_data):
    uniq_id = get_data['data']['id']
    short_url = get_data['data']['url']
    full_url = get_data['data']['full']
    pyperclip.copy(short_url)
    table = [[uniq_id, full_url[:45], short_url]]
    headers = ["Unique ID", "Full URL", "Shorten URL"]
    cprint(tabulate(table, headers,  tablefmt="fancy_grid"), 'green')


def connect_cloud(data, mode):
    long_url = data["long_url"]
    default_data = check_error(long_url)
    if default_data:
        if mode:
            custom_name = data["custom_name"]
            lockit = data["lockit"]
            limit_url = data['limit_url']
            adv_data = get_adv_data(long_url, custom_name, lockit, limit_url)
            if "status" not in adv_data['data']:
                return extract_data(adv_data)
            elif "custom-taken" in adv_data['data']['status']:
                cprint(
                    "Looks like your custom username is in use so..processing link with default name", 'yellow')
                return extract_data(get_adv_data(
                    long_url, None, lockit, limit_url))
            else:
                return extract_data(default_data)
    return extract_data(default_data)


def check_error(long_url):
    get_data = requests.get(
        f"{utvis_api}url={long_url}").json()
    if not get_data['success']:
        if get_data['error']['code'] == 1:
            cprint("Please provide valid URL", 'red')
            ask_user()
        elif get_data['error']['code'] == 0:
            cprint("Oops!... This domain is not allowed to shrink", 'red')
            ask_user()
        else:
            print(get_data)
        sys.exit(1)
    return get_data


def get_adv_data(long_url, custom_name, lockit, limit_url):
    if not custom_name:
        return requests.get(
            f'{utvis_api}url={long_url}{lockit}{limit_url}').json()
    return requests.get(
        f'{utvis_api}url={long_url}{custom_name}{lockit}{limit_url}').json()


def get_password():
    lockit = pwinput.pwinput(
        prompt='Enter the password to protect this link [maximum 10 char]: ')
    if len(lockit) >= 10:
        cprint(
            r'Your password is more than 10 chars..so, removing your password from the link', 'red')
        return "&password="
    return f"&password={lockit[:10]}"


def get_uses():
    limit_url = input(
        "How many times do you want this URL to be used? [Only digits]: ")
    try:
        if int(limit_url):
            cprint(
                f'No. of uses for this URL is set to {limit_url}\n', 'green')
            return f"&uses={limit_url}"
    except ValueError:
        cprint('No. of uses for this link is set to default value\n', 'yellow')
        return f"&uses="


def ask_user():
    data = dict()
    get_link = input("Enter the URL that you want to shrink:  ")
    if get_link:
        data.update({"long_url": get_link})
        adv_mode = input("Do you want to activate the advanced mode?: ")
        if helper_func.chkreg("",adv_mode):
            custom_name = input("Enter your custom username: ")
            data.update({"custom_name": f"&custom={custom_name}"})
            data.update({"lockit": f"{get_password()}"})
            data.update({"limit_url": f"&uses={get_uses()}"})
            return connect_cloud(data, adv_mode)
        return connect_cloud(data, None)
    cprint("Please provide the URL!", 'red')
    sys.exit(1)


def main():
    try:
        ask_user()
    except KeyboardInterrupt:
        cprint("Exiting from the script....", 'red')
        sys.exit(1)
    except requests.exceptions.ConnectionError:
        cprint("\nPlease check your internet connection!", 'red')
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
