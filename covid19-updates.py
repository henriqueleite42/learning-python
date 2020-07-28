# Inspired in https://www.instagram.com/p/CC7r6FJAXvk/

from bs4 import BeautifulSoup
import requests

def get_info(url):
  data = requests.get(url)
  soup = BeautifulSoup(data.text, 'html.parser')
  total = soup.find('div', class_='maincounter-number').text
  other = soup.find_all('span', class_='number-table')
  recovered = other[2].text
  deaths = other[3].text
  deaths = deaths[1:]

  ans = {
    'Total Cases': total,
    'Recovered Cases': recovered,
    'Total Deaths': deaths
  }

  return ans

URL = "https://www.worldometers.info/coronavirus/"

ans = get_info(URL)

for i, j in ans.items():
  print(i + " : " + j)
