import requests
import bs4
res=requests.get('https://en.wikipedia.org/wiki/Indian_Institute_of_Technology_Patna')
type(res)
res.text
soup= bs4.BeautifulSoup(res.text,'lxml')
type(soup)
#hi=soup.select('.href')

for link in soup.find_all('a', href=True):
    if '#' in link['href']:
        pass
    else:
        print(link['href'])
