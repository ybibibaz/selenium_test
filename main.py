import json
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


xpath = '/html/body/div[5]/ymaps/ymaps/ymaps/ymaps[4]/ymaps[1]/ymaps[2]/ymaps[1]/ymaps/ymaps/ymaps[1]/ymaps[1]/ymaps/ymaps[2]/ymaps/ymaps/ymaps'


def field_loaded(browser):
    return browser.find_elements("xpath", xpath) and 'балл' in browser.find_elements("xpath", xpath)[0].text


def main():
    uri = 'http://www.probki-online.ru/probki-online.php?city='
    cities = ['sankt-peterburg', 'moscow', 'ekaterinburg']
    data = {}
    browser = webdriver.Chrome()
    for city in cities:
        browser.get(f'{uri}{city}')
        WebDriverWait(browser, timeout=10).until(field_loaded)
        elem = browser.find_elements("xpath", xpath)
        data[city] = elem[0].text.split()[0]
    with open('data.json', 'w') as f:
        json.dump(data, f)


if __name__ == '__main__':
    main()
