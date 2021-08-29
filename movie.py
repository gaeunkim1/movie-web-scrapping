import requests
from bs4 import BeautifulSoup

all_url = "https://auto.naver.com/index.nhn"
all_page = requests.get(all_url)
all_soup = BeautifulSoup(all_page.text, "html.parser")

#URL 추출하기
result1 = all_soup.find('div', class_="article_maker")
result2 = result1.find('ul')
result3 = result2.find_all('a')

#car_url : 추출한 자동차 url 저장
car_url = []
for i in result3:
    car_url.append("http://auto.naver.com" + i.attrs['href'])



