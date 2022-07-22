from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup as BS
import time, json

def get_html(url, ua):
    path = r'C:\Users\Валик\Documents\GitHub\chromedriver.exe'

    options = webdriver.ChromeOptions()
    options.add_argument(f'user-agent={ua}')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.binary_location = 'C:\Program Files\Google\Chrome Beta\Application\chrome.exe'

    service = Service(path)
    driver = webdriver.Chrome(service=service, options=options)
    try:
        driver.maximize_window()
        driver.get(url)
        time.sleep(30)

        with open('index.html', 'w', encoding='utf-8') as file:
            file.write(driver.page_source)

    except Exception as ex:
        print(ex)
    finally:
        driver.stop_client()
        driver.close()
        driver.quit()

def get_data():
    data = []
    with open('index.html', encoding='utf-8') as file:
        html = file.read()

    soup = BS(html, 'lxml')
    all_posts = soup.find_all('p', class_='text-content with-meta')

    for post in all_posts:
        one_publish = post.text.replace("Here's the latest on the war in Ukraine:", '')\
                               .replace("Here’s what we’re following right now", '')
        hrefs = post.find_all('a')

        href_list = []
        for href in hrefs:
            href_list.append(href.get('href'))

        try:
            str1 = one_publish.split(href_list[0])
            info1 = str1[0].strip()
            data.append({
                'post': info1,
                'href': href_list[0]
            })
        except Exception as ex:
            print(ex)
        try:
            str2 = str1[1].split(href_list[1])
            info2 = str2[0].strip()
            data.append({
                'post': info2,
                'href': href_list[1]
            })
        except Exception as ex:
            print(ex)
        try:
            str3 = str2[1].split(href_list[2])
            info3 = str3[0].strip()
            data.append({
                'post': info3,
                'href': href_list[2]
            })
        except Exception as ex:
            print(ex)
        try:
            str4 = str3[1].split(href_list[3])
            info4 = str4[0].strip()
            data.append({
                'post': info4,
                'href': href_list[3]
            })
        except Exception as ex:
            print(ex)
        try:
            str5 = str4[1].split(href_list[4])
            info5 = str5[0].strip()
            data.append({
                'post': info5,
                'href': href_list[4]
            })
        except Exception as ex:
            print(ex)

    with open('test_data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def fix_bug():
    data_list = []
    with open('test_data.json', encoding='utf-8') as file:
        JSON = json.load(file)

    for data in JSON:
        data_list.append({
            'post': data['post'].replace(' ', ' ').replace('  ', ' '),
            'href': data['href']
        })

    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(data_list, file, indent=4, ensure_ascii=False)

def main():
    url = 'https://web.telegram.org/z/#-1488156064'
    ua = UserAgent().random
    headers = {'user-agent': ua}

    # get_html(url, headers)
    get_data()
    fix_bug()

if __name__ == '__main__':
    main()
