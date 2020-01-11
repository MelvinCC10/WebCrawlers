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
        headlines = soup.find_all('a', attrs={'class':'link'})
        for head_line in headlines:
            print(head_line.text.strip())





tesla_stock = stock('tsla')
print(tesla_stock.headlines())
