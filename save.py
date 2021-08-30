import requests
from bs4 import BeautifulSoup

def save_to_file(company, url):
    car_page = requests.get(url)
    car_soup = BeautifulSoup(car_page.text, "html.parser")

    #result_name = 자동차 이름 추출 

    result_name = car_soup.find_all('a', class_="model_name")
    
    #name = 자동차 이름(회사별)
    name = []
    for i in result_name:
        name.append(i.text.lstrip("\n"))

    print(name)