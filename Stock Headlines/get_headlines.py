from urllib.request import urlopen
from bs4 import BeautifulSoup




web_page = 'https://www.marketwatch.com/investing/index/djia?mod=home-page'
web_page_html = urlopen(web_page)
page = web_page_html.read()

soup = BeautifulSoup(page,'html.parser')
Stock_price = soup.find(‘div’, attrs={‘class’:’intraday__data’})


#price_box = soup.find(‘sup’, attrs={‘class’:’character’})
