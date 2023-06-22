import requests
from bs4 import BeautifulSoup
from lxml import etree

url = "https://www.washingtonpost.com/technology/2020/09/25/privacy-check-blacklight/"

data = requests.get(url=url).text

soup = BeautifulSoup(data,"lxml")

title = soup.find("p",attrs={"class" : "wpds-c-cYdRxM wpds-c-cYdRxM-iPJLV-css overrideStyles font-copy"}).text

dom = etree.HTML(str(soup))

content0 = str(dom.xpath('//*[@id="__next"]/div[6]/main/article/div[2]/div[2]/div[2]/p')[0].text)
content1 = str(dom.xpath('//*[@id="__next"]/div[6]/main/article/div[2]/div[2]/div[2]/p/a')[0].text) 
content2 = str(dom.xpath('//*[@id="__next"]/div[6]/main/article/div[2]/div[2]/div[2]/p/text()[2]')[0])

content = content0 + content1 + content2

data = {
    'title':title,
    'content': content
}

print(data)

