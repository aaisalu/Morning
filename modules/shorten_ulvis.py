import requests
import helper_func
import sys


def extract_data(get_data):
    uniq_id = get_data['data']['id']
    short_url = get_data['data']['url']
    full_url = get_data['data']['full']
    print(uniq_id, short_url, full_url)


def connect_cloud(data):
    mode = data["mode"]
    long_url = data["long_url"]
    custom_name = data["custom_name"]
    lockit = data["lockit"]
    limit_url = data['limit_url']
    get_data = get_cloud_data(long_url, custom_name, lockit, limit_url)
    if get_data['success']:
        if mode:
            if "status" not in get_data['data']:
                extract_data(get_data)
            elif "custom-taken" in get_data['data']['status']:
                extract_data(get_cloud_data(
                    long_url, None, lockit, limit_url))
            else:
                return extract_data(default_action(long_url))
        else:
            # print(get_data['success']['error'])
            return extract_data(default_action(long_url))
    else:
        print(get_data)


def default_action(long_url):
    return requests.get(f"https://ulvis.net/API/write/get?url={long_url}").json()


def get_cloud_data(long_url, custom_name, lockit, limit_url):
    if not custom_name:
        return requests.get(
            f'https://ulvis.net/API/write/get?url={long_url}{lockit}{limit_url}').json()
    return requests.get(
        f'https://ulvis.net/API/write/get?url={long_url}{custom_name}{lockit}{limit_url}').json()


def ask_user():
    data = dict()
    get_link = input("Enter the url that you want to shrink:  ")
    if get_link:
        data.update({"long_url": get_link})
        adv_mode = input("Do you want to activate advanced mode ?")
        if helper_func.chkreg(adv_mode):
            data.update({"mode": adv_mode})
            custom_name = input("Enter your own custom username: ")
            lockit = input("Enter the password to link: ")
            limit_url = input("Type the limit to the url:")
            data.update({"custom_name": f"&custom={custom_name}"})
            data.update({"lockit": f"&password={lockit[:10]}"})
            print(f"Your password is: {lockit[:10]}")
            try:
                if int(limit_url):
                    data.update({"limit_url": f"&uses={limit_url}"})
            except ValueError:
                data.update({"limit_url": f"&uses={2}"})
            return connect_cloud(data)
        return extract_data(default_action(get_link))

    sys.exit(1)


def main():
    try:
        ask_user()
    except KeyboardInterrupt:
        print("Exiting from the script....")
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
