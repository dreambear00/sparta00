import requests
from bs4 import BeautifulSoup
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=Y',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

chart = soup.select('#body-content > div.newest-list > div > table > tbody > tr.list')
for song in chart:
    
    number = song.select_one('td.number').text[0:3].strip()
    title = song.select_one('td.info > a.title.ellipsis').text.strip()
    artist = song.select_one('td.info > a.artist.ellipsis').text.strip('.')
    result = artist.split('.')

    print(number, title, result)


import requests
from bs4 import BeautifulSoup
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200530&hh=01&rtm=Y&pg=2',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

chart = soup.select('#body-content > div.newest-list > div > table > tbody > tr.list')
for song in chart:
    
    number = song.select_one('td.number').text[0:3].strip()
    title = song.select_one('td.info > a.title.ellipsis').text.strip()
    artist = song.select_one('td.info > a.artist.ellipsis').text.strip('.')
    result = artist.split('.')

    print(number, title, result)