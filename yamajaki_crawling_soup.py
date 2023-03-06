import requests
from bs4 import BeautifulSoup

url = 'https://reserve.suntory.co.jp/regist/is?SMPFORM=ngoe-lenetb-550fe19094a7fbbfd41c49a7ce9cc871&courseNo=00037&eventDate=2022-11-11'
response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    # emp = soup.find_all('tbody')
    #
    # for tag in emp:
    #     string = tag.get("class").pop(0)
    #     print(string)
    data = soup.find("td", class_="emp")
    title = soup.select_one('#calendarTable-body-2 > tr:nth-child(2) > td:nth-child(5)')
    print(data)
else:
    print(response.status_code)
