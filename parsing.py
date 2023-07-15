import requests
from bs4 import BeautifulSoup
import datetime

now = datetime.datetime.now()
month_str = (
    'january', 'february',
    'march', 'april', 'may',
    'june', 'jule', 'august', 'september',
    'october', 'november', 'december '
)
date_rating = datetime.date.today()

if date_rating.weekday() != 0:
    date_rating -= datetime.timedelta(days=date_rating.weekday())

date_rating = str(date_rating).split('-')
date_rating = f'{date_rating[0]}/{month_str[int(date_rating[1]) - 1]}/{date_rating[2]}'


url = f'https://www.hltv.org/ranking/teams/{date_rating}'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
teams = soup.find_all('span', class_='name')[:10]
points = soup.find_all('span', class_='points')[:10]

massage_rating = ''
for i in range(len(teams)):
    massage_rating += f'№{i + 1} {teams[i].text} {points[i].text}\n'

print(massage_rating)



