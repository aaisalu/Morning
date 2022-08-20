from tabulate import tabulate
from termcolor import cprint
import helper_func
import webbrowser
import pyperclip
import colorama
import requests
import random
import time
import sys
import re
import os
colorama.init()


def random_mail():
    for get_rand_mail in requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1}").json():
        return get_rand_mail.split('@')


def get_domain():
    get_domain_lists = requests.get(
        'https://www.1secmail.com/api/v1/?action=getDomainList').json()
    return random.choice(get_domain_lists)


def chkreg(answer):
    return re.search("yes|1|yep|sure|True|yess|hellyeah|yeah|r|refresh", f'{answer}', flags=re.IGNORECASE)


def folder(file):
    global Path
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    Path = rf"{desktop}\{file}"
    if not os.path.exists(Path):
        os.makedirs(Path)
    return Path


def archived(first, ask_custom):
    global archives
    rand_domain = get_domain()
    rand_mail = random_mail()
    archives = []
    if first:
        if ask_custom:
            archives.append([ask_custom, rand_domain])
            return saved()
        else:
            archives.append([rand_mail[0], rand_mail[1]])
            return saved()
    else:
        archives.append([rand_mail[0], rand_mail[1]])
        return saved()


def saved():
    global domain_name
    global username
    global email
    username = f'{archives[0][0]}'
    domain_name = f'{archives[0][1]}'
    email = f'{username}@{domain_name}'
    pyperclip.copy(email)
    cprint(
        f"\n -------x        Your temporary email is: {email}       x-------\n", 'green')
    return loop()


def loop():
    while True:
        check_mail()
        time.sleep(3)


def check_mail():
    global count_mails
    incom_mail = requests.get(
        f"https://www.1secmail.com/api/v1/?action=getMessages&login={username}&domain={domain_name}").json()
    if count_mails := len(incom_mail):
        cprint(
            f"\n\n ------x  You have received {count_mails} mails at your inbox of {email}  x------\n", 'cyan')
        distribute_content(incom_mail)
        refresh()
    else:
        cprint(
            f"   --| Your Inbox is currently empty, Refreshing Inbox of {email} in every 3 sec. |-- ", "yellow", end="\r")


def refresh():
    ask = input("Do you want to refresh your inbox? ")
    if chkreg(ask):
        loop()
    else:
        sys.exit(1)


def get_id(mail):
    return [dict(k)['id'] for k in mail]


def distribute_content(incom_mail):
    for unq_id in get_id(incom_mail):
        url = requests.get(
            f'https://www.1secmail.com/api/v1/?action=readMessage&login={username}&domain={domain_name}&id={unq_id}').json()
        tabulate_data(url, unq_id)
        mails_contents(url, unq_id)


def write_mail(contents, unq_id):
    with open(rf'{helper_func.create_folder("Emails")}\{email}_{unq_id}.txt', 'w') as note:
        note.write(contents)
    with open(rf'{helper_func.create_folder("Emails")}\Emails_history.txt', 'a') as note:
        note.write(contents)

    # open notepad with your mails
    # Thanks to Máthé Endre-Botond at stackoverflow.com/a/6178200
    webbrowser.open(f"{helper_func.Path}\{email}_{unq_id}.txt")
    return cprint(f'\nEmails is saved at {helper_func.Path} in txt', 'green')


def tabulate_data(data, uniq_id):
    attachments = data['attachments']
    headers = [f"Message ID {data['id']}", f"Inbox of {email}"]
    table = [["From", f"{data['from']}"], ["Subject", f"{data['subject']}"], [
        "Body", f"{data['textBody']}"], ["Date", f"{data['date']}"]]
    if attachments:
        for content in attachments:
            table.extend([["Attachments", "Is present"], ["File Name", f"{content['filename']}"], ["Content Type", f"{content['contentType']}"], [
                "Donwload Link", f"https://www.1secmail.com/api/v1/?action=download&login={username}&domain={domain_name}&id={uniq_id}&file={content['filename']}"], ["Size", f"{content['size']}"]])
    cprint(tabulate(table, headers,  tablefmt="fancy_grid"), 'green')


def mails_contents(data, uniq_id):
    attachments = data['attachments']
    string = (f"Attachments of the Message ID: " if data['attachments']
              else f"\n----<<<<<<<<<<<<<<<<<<<<<<<<<<< -- Divider of Mails -- >>>>>>>>>>>>>>>>>>>>>>>>>>>----\n\n")
    info = f"Unique Message ID: {data['id']}\n"
    info += f"Email from: {data['from']}\n"
    info += f"Email to: {email}\n"
    info += f"Subject: {data['subject']}\n"
    info += f"Body: {data['textBody']}\n"
    info += f"Date: {data['date']}\n"
    info += f"{string}"
    if attachments:
        for content in attachments:
            info += f"{uniq_id}\n"
            info += f"File Name: {content['filename']}\n"
            info += f"Content Type: {content['contentType']}\n"
            info += f"Download Link: https://www.1secmail.com/api/v1/?action=download&login={username}&domain={domain_name}&id={uniq_id}&file={content['filename']}\n"
            info += f"Size:{content['size']}\n"
            info += "\n----<<<<<<<<<<<<<<<<<<<<<<<<<<< -- Divider of Mails -- >>>>>>>>>>>>>>>>>>>>>>>>>>>----\n\n"
    return write_mail(info, uniq_id)


def ask_user():
    cust_domain = input("Do you want to use domain names on your temp_mail? ")
    if chkreg(cust_domain):
        ask_custom = input("Enter your custom username: ")
        return archived(cust_domain, ask_custom)
    else:
        return archived(None, None)


def main():
    try:
        ask_user()
    except KeyboardInterrupt:
        cprint("\nExiting from the script....", 'red')
        sys.exit(1)
    except requests.exceptions.ConnectionError:
        cprint("\nPlease check your internet connection!", 'red')
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
