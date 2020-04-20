import re
import csv
from requests import get
from bs4 import BeautifulSoup


def scrape(static_dir):
    website_url = get(
        'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_the_United_States').text
    soup = BeautifulSoup(website_url, 'lxml')
    table = [['U.S. state or territory', 'Cases',
              'Deaths', 'Recoveries', 'Hospitalizations']]

    for data in soup.find('div', {'id': 'covid19-container'}).findAll('tr', attrs={'class': None}):
        if data.findAll('th', attrs={'scope': 'row'}):
            state = [a.string for a in data.findAll(
                'a', attrs={'title': True})]
            for td in list(data.findAll('td')):
                if re.search('\d+\n', str(td)):
                    try:
                        state += [int(float(re.sub('<.*?>', '',
                                                   str(td)).strip().replace(',', '')))]
                    except:
                        pass
            while len(state) < len(table[0]) and len(state) != 0:
                state += '-'
            if state:
                table.append(state)

    with open(f'{static_dir}/covid19.csv', 'w', newline='') as f:
        wr = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        wr.writerows(table)

    return table
