import requests
from bs4 import BeautifulSoup
from hw_3.scrapper_handlers.data_handlers import createExcel, map_quote_data

URL = 'http://quotes.toscrape.com/'

if __name__ == '__main__':
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, features='html.parser')

quotes_block = soup.find_all('div', {'class': 'col-md-8'})[1]
quotes = quotes_block.findAll('div', {'class': 'quote'})

quotes_dict = map_quote_data(quotes)

createExcel(quotes_dict)
