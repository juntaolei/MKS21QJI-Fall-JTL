import re
import csv
from requests import get
from bs4 import BeautifulSoup


def scrape(static_dir):
    website_url = get(
        'https://en.wikipedia.org/wiki/Template:2019-20_coronavirus_pandemic_data').text
    soup = BeautifulSoup(website_url, 'lxml')
    table = [['Countries and territories', 'Cases', 'Deaths', 'Recoveries']]

    for data in soup.find('table', {'class': 'wikitable'}).findAll('tr', attrs={'class': None}):
        if data:
            country = [a.string for a in data.findAll(
                'a', attrs={'title': True})]
            country += [int(float(re.findall('\d+\n', str(td))[0].strip()))
                        for td in list(data.findAll('td')) if re.findall('\d+\n', str(td))]
            if len(country) < len(table[0]) and len(country) != 0:
                country += '-'
            if country:
                table.append(country)

    with open(f'{static_dir}/covid19.csv', 'w', newline='') as f:
        wr = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        wr.writerows(table)
