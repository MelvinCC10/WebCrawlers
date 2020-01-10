from urllib.request import urlopen
from bs4 import BeautifulSoup


class stock():

    def __init__(self,ticker):
        self.url = 'https://www.marketwatch.com/investing/stock/' + ticker

    def price(self):
        page = urlopen(self.url)
        soup = BeautifulSoup(page,'html.parser')
        find_price = soup.find('bg-quote', attrs={'class':'value'})
        price = find_price.text.strip()

        return price

    def headlines(self):
        page = urlopen(self.url)
        soup = BeautifulSoup(page,'html.parser')
        find_price = soup.find('h3', attrs={'class':'article_headline'})
        print(find_price)
        price = find_price.text.strip()





tesla_stock = stock('tsla')
print(tesla_stock.headlines())
