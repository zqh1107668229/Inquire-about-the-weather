import re
import requests
from bs4 import BeautifulSoup
import json


filename = "city_message.txt"
error_message = "未找到该城市"

def city_message():
    with open(filename,'r') as file_object:
        dict = json.loads(file_object.read())
        return dict

dict = city_message()

def city(city):

    for key,value in dict.items():
        if city==key:
            # print(value)
            return value
            break
        else:
            continue
    return error_message


while True:
    city_id = input("请输入需要查询的城市: ")
    return_city_id = city(city_id)
    if return_city_id==error_message:
        print(error_message)
        continue
    else:
        break


url = "http://www.weather.com.cn/weather/{}.shtml".format(return_city_id)
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}


def get_page_index(url,headers):
    response = requests.get(url,headers = headers)
    response.encoding = 'utf-8'
    return response.text


def parse_html(html):
    soup = BeautifulSoup(html,'lxml')
    soup.prettify()
    for li in soup.select('#7d .t li'):
        print(li.find('h1').get_text())
        if li.select('.tem span'):
            print(li.find('p').get_text() +' '+ li.select('.tem span')[0].get_text()+'/'+li.select('.tem i')[0].get_text())
            continue
        print(li.find('p').get_text() +' '+ li.select('.tem i')[0].get_text())


def main():
    html = get_page_index(url,headers)
    parse_html(html)


if __name__ == '__main__':
    main()
