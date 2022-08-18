import requests
import random
import time
import sys
import re


def random_mail():
    for get_rand_mail in requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1}").json():
        return get_rand_mail.split('@')


def get_domain():
    get_domain_lists = requests.get(
        'https://www.1secmail.com/api/v1/?action=getDomainList').json()
    return random.choice(get_domain_lists)


def chkreg(answer):
    return re.search("yes|1|yep|sure|True|yess|hellyeah|yeah|r|refresh", f'{answer}', flags=re.IGNORECASE)


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
    return loop()


def loop():
    while True:
        check_mail()
        time.sleep(10)


def check_mail():
    global count_mails
    incom_mail = requests.get(
        f"https://www.1secmail.com/api/v1/?action=getMessages&login={username}&domain={domain_name}").json()
    if count_mails := len(incom_mail):
        print(f"You have received {count_mails} mail\n")
        get_content(incom_mail)
        refresh()
    else:
        print("No mail received!")


def refresh():
    ask = input("Do you want to refresh your mail? ")
    if chkreg(ask):
        loop()
    else:
        sys.exit(1)


def get_id(mail):
    return [dict(k)['id'] for k in mail]


def get_content(incom_mail):
    for unq_id in get_id(incom_mail):
        url = requests.get(
            f'https://www.1secmail.com/api/v1/?action=readMessage&login={username}&domain={domain_name}&id={unq_id}').json()
        save_dict = dict(url)
        if not save_dict['attachments']:
            count_mail(content(save_dict))
            print(content(save_dict))
        else:
            count_mail(content(save_dict) + attachments(url, unq_id))
            print(content(save_dict) + attachments(url, unq_id))


def content(data):
    string = (f"Attachments of the Message ID: " if data['attachments']
              else f"\n----<<<<<<<<<<<<<<<<<<<<<<<<<<< -- Divider of Mails -- >>>>>>>>>>>>>>>>>>>>>>>>>>>----\n\n")
    info = f"Unique Message ID: {data['id']}\n"
    info += f"Email from: {data['from']}\n"
    info += f"Subject: {data['subject']}\n"
    info += f"Body: {data['textBody']}\n"
    info += f"Date: {data['date']}\n"
    info += f"{string}"
    return info


def attachments(data, uniq_id):
    attachment = data['attachments']
    for content in attachment:
        info = f"{uniq_id}\n"
        info += f"File Name: {content['filename']}\n"
        info += f"Content Type: {content['contentType']}\n"
        info += f"Download Link: https://www.1secmail.com/api/v1/?action=download&login={username}&domain={domain_name}&id={uniq_id}&file={content['filename']}\n"
        info += f"Size:{content['size']}\n"
        info += "\n----<<<<<<<<<<<<<<<<<<<<<<<<<<< -- Divider of Mails -- >>>>>>>>>>>>>>>>>>>>>>>>>>>----\n\n"
    return info


def count_mail(item):
    if count_mail == 1:
        return write_mail(item, 'w')
    else:
        return write_mail(item, 'a+')


def write_mail(item, mode):
    with open('testone.txt', f'{mode}') as note:
        note.write(item)


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
        print("Exiting from the script....")
        sys.exit(1)
    except requests.exceptions.ConnectionError:
        print("Please check your internet connection!")
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
