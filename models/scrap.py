from bs4 import BeautifulSoup
import requests

class Scrap:

    def get_stocks(self):

        url = 'https://www.screener.in/screens/2142247/sc202401/'

        result = requests.get(url)

        content = result.text

        soup = BeautifulSoup(content, 'lxml')

        td = soup.find_all('td', class_='text')

        print(td)

        data = []

        for tex in td:
           
           name = tex.find_all('a', href=True)

           for company in name:
              
                    co = company.get_text()
                    link = company['href']

                    print(company)
          
           
    


scrap = Scrap()

scrap.get_stocks()
