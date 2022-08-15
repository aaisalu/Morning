import requests
from configparser import ConfigParser
from termcolor import cprint
import colorama
colorama.init()


def get_token():
    try:
        config = ConfigParser()
        config.read('../config.ini')
        data = config['API']['Cash_token']
        return data.strip()
    except KeyError:
        return None


source = '''
                                                        WELCOME TO THE
                                               CENTRA BANK OF PROJECT MORNING
 [1] Kuwaiti Dinar      [13] Chinese Yuan           [25] United Arab Emirates [37] Romanian Leu       [49] Jamaican Dollar
 [2] Sri Lankan Rupee   [14] Czech Republic Koruna  [26] Afghan Afghani       [38] Russian Ruble      [50] Japanese Yen
 [3] Mongolian Tugrik   [15] Egyptian Pound         [27] Netherlands Guilder  [39] Saudi Riyal        [51] Cambodian Riel
 [4] Mexican Peso       [16] Ethiopian Birr         [28] Argentine Peso       [40] Sudanese Pound     [52] North Korean Won
 [5] Malaysian Ringgit  [17] Euro                   [29] Australian Dollar    [41] Swedish Krona      [53] South Korean Won
 [6] Nigerian Naira     [18] British Pound Sterling [30] Barbadian Dollar     [42] Singapore Dollar   [54] United States Dollar
 [7] Norwegian Krone    [19] Hong Kong Dollar       [31] Bangladeshi Taka     [43] Syrian Pound       [55] Vietnamese Dong
 [8] Nepalese Rupee     [20] Indonesian Rupiah      [32] Bulgarian Lev        [44] Tajikistani Somoni [56] South African Rand
 [9] New Zealand Dollar [21] Israeli New Sheqel     [33] Brazilian Real       [45] Tunisian Dinar     [57] Zambian Kwacha
 [10] Philippine Peso   [22] Indian Rupee           [34] Bhutanese Ngultrum   [46] Turkish Lira       [58] Zimbabwean Dollar
 [11] Pakistani Rupee   [23] Iraqi Dinar            [35] Canadian Dollar      [47] New Taiwan Dollar
 [12] Qatari Rial       [24] Iranian Rial           [36] Swiss Franc          [48] Ukrainian Hryvnia
'''
cprint(source, 'green')


def controller(money):
    if token := get_token():
        try:
            from_country = engine("from")
            to_country = engine("to")
            url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_country}&to_currency={to_country}&apikey={token}'
            data = requests.get(url).json()
            primary_code = data['Realtime Currency Exchange Rate']['1. From_Currency Code']
            primary_name = data['Realtime Currency Exchange Rate']['2. From_Currency Name']
            secondary_code = data['Realtime Currency Exchange Rate']['3. To_Currency Code']
            secondary_name = data['Realtime Currency Exchange Rate']['4. To_Currency Name']
            currency = float(
                data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
            calculator = round(currency * float(money), 6)
            print(
                f"{money} {primary_name}[{primary_code}] equals {calculator} {secondary_name}[{secondary_code}]")
        except KeyError:
            return cprint("Invalid token", 'red')
    return cprint("Please provide the token!", 'red')


def engine(get):
    try:
        ask = int(input(
            f"Enter the corresponding country digits you want to convert {get}: "))
        if ask == 1:
            #  print("Kuwaiti Dinar")
            return "KWD"
        elif ask == 2:
            # print("Sri Lankan Rupee")
            return "LKR"
        elif ask == 3:
            # print("Mongolian Tugrik")
            return "MNT"
        elif ask == 4:
            # print("Mexican Peso")
            return "MXN"
        elif ask == 5:
            # print("Malaysian Ringgit")
            return "MYR"
        elif ask == 6:
            # print("Nigerian Naira")
            return "NGN"
        elif ask == 7:
            # print("Norwegian Krone")
            return "NOK"
        elif ask == 8:
            # print("Nepalese Rupee")
            return "NPR"
        elif ask == 9:
            # print("New Zealand Dollar")
            return "NZD"
        elif ask == 10:
            # print("Philippine Peso")
            return "PHP"
        elif ask == 11:
            # print("Pakistani Rupee")
            return "PKR"
        elif ask == 12:
            # print("Qatari Rial")
            return "QAR"
        elif ask == 13:
            # print("Chinese Yuan")
            return "CNY"
        elif ask == 14:
            # print("Czech Republic Koruna")
            return "CZK"
        elif ask == 15:
            # print("Egyptian Pound")
            return "EGP"
        elif ask == 16:
            # print("Ethiopian Birr")
            return "ETB"
        elif ask == 17:
            # print("Euro")
            return "EUR"
        elif ask == 18:
            # print("British Pound Sterling")
            return "GBP"
        elif ask == 19:
            # print("Hong Kong Dollar")
            return "HKD"
        elif ask == 20:
            # print("Indonesian Rupiah")
            return "IDR"
        elif ask == 21:
            # print("Israeli New Sheqel")
            return "ILS"
        elif ask == 22:
            # print("Indian Rupee")
            return "INR"
        elif ask == 23:
            # print("Iraqi Dinar")
            return "IQD"
        elif ask == 24:
            # print("Iranian Rial")
            return "IRR"
        elif ask == 25:
            # print("    United Arab Emirates Dirham")
            return "AED"
        elif ask == 26:
            # print("Afghan Afghani")
            return "AFN"
        elif ask == 27:
            # print("Netherlands Antillean Guilder")
            return "ANG"
        elif ask == 28:
            # print("Argentine Peso")
            return "ARS"
        elif ask == 29:
            # print("Australian Dollar")
            return "AUD"
        elif ask == 30:
            # print("Barbadian Dollar")
            return "BBD"
        elif ask == 31:
            # print("Bangladeshi Taka")
            return "BDT"
        elif ask == 32:
            # print("Bulgarian Lev")
            return "BGN"
        elif ask == 33:
            # print("Brazilian Real")
            return "BRL"
        elif ask == 34:
            # print("Bhutanese Ngultrum")
            return "BTN"
        elif ask == 35:
            # print("Canadian Dollar")
            return "CAD"
        elif ask == 36:
            # print("Swiss Franc")
            return "CHF"
        elif ask == 37:
            # print("Romanian Leu")
            return "RON"
        elif ask == 38:
            # print("Russian Ruble")
            return "RUB"
        elif ask == 39:
            # print("Saudi Riyal")
            return "SAR"
        elif ask == 40:
            # print("Sudanese Pound")
            return "SDG"
        elif ask == 41:
            # print("Swedish Krona")
            return "SEK"
        elif ask == 42:
            # print("Singapore Dollar")
            return "SGD"
        elif ask == 43:
            # print("Syrian Pound")
            return "SYP"
        elif ask == 44:
            # print("Tajikistani Somoni")
            return "TJS"
        elif ask == 45:
            # print("Tunisian Dinar")
            return "TND"
        elif ask == 46:
            # print("Turkish Lira")
            return "TRY"
        elif ask == 47:
            # print("New Taiwan Dollar")
            return "TWD"
        elif ask == 48:
            # print("Ukrainian Hryvnia")
            return "UAH"
        elif ask == 49:
            # print("Jamaican Dollar")
            return "JMD"
        elif ask == 50:
            # print("Japanese Yen")
            return "JPY"
        elif ask == 51:
            # print("Cambodian Riel")
            return "KHR"
        elif ask == 52:
            # print("North Korean Won")
            return "KPW"
        elif ask == 53:
            # print("South Korean Won")
            return "KRW"
        elif ask == 54:
            # print("United States Dollar")
            return "USD"
        elif ask == 55:
            # print("Vietnamese Dong")
            return "VND"
        elif ask == 56:
            # print("South African Rand")
            return "ZAR"
        elif ask == 57:
            # print("Zambian Kwacha")
            return "ZMW"
        elif ask == 58:
            # print("Zimbabwean Dollar")
            return "ZWL"
        else:
            cprint("Wrong input", 'red')
            return None
    except ValueError:
        return cprint("Please enter the country corresponding digit!", 'red')


try:
    controller(int(input("Enter the amount to convert: ")))
except ValueError:
    cprint("Please! enter the number to be converted!", 'red')
