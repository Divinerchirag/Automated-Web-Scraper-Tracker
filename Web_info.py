from selenium import webdriver

DIRECTORY = 'reports'
NAME = input("Enter the Product name :- ")
CURRENCY = '₹'
MIN_PRICE = input("Enter the Minimun value amount :- ")
MAX_PRICE = input("Enter the Maximun value amount :- ")
FILTERS = {
    'min': MIN_PRICE,
    'max': MAX_PRICE
}
BASE_URL = "https://www.amazon.in/"


def get_chrome_web_driver(options):
    return webdriver.Chrome( options=options)


def get_web_driver_options():
    return webdriver.ChromeOptions()


def set_ignore_certificate_error(options):
    options.add_argument('--ignore-certificate-errors')


def set_browser_as_incognito(options):
    options.add_argument('--incognito')


def set_automation_as_head_less(options):
    options.add_argument('--headless')
