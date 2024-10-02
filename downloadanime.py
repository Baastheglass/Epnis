from selenium import webdriver
from bs4 import BeautifulSoup
import requests

url = "https://ww8.gogoanimes.org/anime-list?page=1" 
driver = webdriver.Chrome()
response = requests.get(url, verify=False)
#print(response.content)
soup = BeautifulSoup(response.content, 'html.parser')
#print(soup)
ul = soup.find(class_='listing')
animeNames = []
# for line in ul.text:
#     print("Done")
#     animeNames.append(line)
li_elements = ul.find_all('li')
for li in li_elements:
    animeNames.append(li.text)
    url = li.text
    url = url.replace("\"", "")
    url = url.replace(":", "")
    url = url.lower()
    new_url = "ww8.gogoanimes.org/watch/" + (url.replace(" ", "-")) + "-episode-1"
    print(new_url)
    driver.get(str(new_url))
    
    
#browser = webdriver.Chrome()

