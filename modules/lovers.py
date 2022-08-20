from termcolor import cprint
import helper_func
import requests
import colorama
import sys
colorama.init()


def calculate(f_name):
    try:
        s_name = input("Please enter the person name you are in love with: ")
        headers = {
            "X-RapidAPI-Key": f"{helper_func.get_token('RapidAPI_token')}",
            "X-RapidAPI-Host": "love-calculator.p.rapidapi.com"
        }
        response = requests.request(
            "GET", "https://love-calculator.p.rapidapi.com/getPercentage", headers=headers, params={"sname": s_name, "fname": f_name}).json()
        percentages = response['percentage']
        results = response['result']
        cprint(
            f"\nPercentage of love between {f_name} & {s_name} is {percentages}%.", 'blue')
        cprint(f'AI message for their love is :> {results}', 'green')
    except KeyError:
        cprint("Looks like your love_token is false just like your love", 'red')
    except requests.exceptions.ConnectionError:
        cprint("We can’t connect to the love_calculator server at the moment due to a network issue!", 'red')


def main():
    try:
        calculate(input("What's your good name? "))
    except KeyboardInterrupt:
        print("Exiting from the script....")
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
