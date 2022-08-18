import requests
import random
import time
import sys


def random_mail():
    for get_rand_mail in requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1}").json():
        return get_rand_mail.split('@')


def get_domain():
    get_domain_lists = requests.get(
        'https://www.1secmail.com/api/v1/?action=getDomainList').json()
    return random.choice(get_domain_lists)


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
    username = f'{archives[0][0]}'
    domain_name = f'{archives[0][1]}'
    return check_mail()


def ask_user():
    cust_domain = input("Do you want to use domain names on your temp_mail? ")
    if cust_domain:
        ask_custom = input("Enter the custom username: ")
        return archived(cust_domain, ask_custom)
    else:
        return archived(None, None)


def loop():
    while True:
        check_mail()
        time.sleep(10)


def content(data):
    saveit = dict(data)
    info = f"Unique email ID: {saveit['id']}\n"
    info += f"Email from: {saveit['from']}\n"
    info += f"Subject: {saveit['subject']}\n"
    info += f"Body: {saveit['textBody']}\n"
    info += f"Date: {saveit['date']}\n\n"
    return info


def attachments(data, uniq_id):
    attachment = data['attachments']
    for content in attachment:
        info = f"____ Attachments of {uniq_id} ____\n"
        info += f"File Name: {content['filename']}\n"
        info += f"Content Type: {content['contentType']}\n"
        info += f"Download Link: https://www.1secmail.com/api/v1/?action=download&login=mama&domain=oosln.com&id={uniq_id}&file={content['filename']}\n"
        info += f"Size:{content['size']}\n"
    return info


def verify_content(data, uniq_id):
    saveit = dict(data)
    if not saveit['attachments']:
        count_mail(data, content(data))
        print(content(data))
    else:
        count_mail(data, content(data) + attachments(data, uniq_id))
        print(content(data) + attachments(data, uniq_id))


def write_mail(info, mode):
    with open('testone.txt', f'{mode}') as note:
        note.write(info)


def count_mail(mail, item):
    if not len(mail) > 1:
        return write_mail(item, 'w')
    else:
        return write_mail(item, 'a+')


def get_id(mail):
    return [dict(k)['id'] for k in mail]


def get_content(incom_mail):
    for unq_id in get_id(incom_mail):
        url = requests.get(
            f'https://www.1secmail.com/api/v1/?action=readMessage&login={username}&domain={domain_name}&id={unq_id}').json()
        return verify_content(url, unq_id)


def check_mail():
    print(f'{username}@{domain_name}')
    incom_mail = requests.get(
        f"https://www.1secmail.com/api/v1/?action=getMessages&login={username}&domain={domain_name}").json()
    if mails := len(incom_mail):
        print(f"You have received {mails} mail")
        get_content(incom_mail)
    else:
        print("No mail received!")


def main():
    try:
        ask_user()
    except KeyboardInterrupt:
        print("Exiting from the script....")
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
