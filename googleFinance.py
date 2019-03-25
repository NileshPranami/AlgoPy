from bs4 import BeautifulSoup
import requests
import csv

req = requests.get('https://www.google.com/search?safe=off&tbm=fin&ei=jTGYXJLKA7PUz7sPkpGB4A8&stick=H4sIAAAAAAAAAONgecRozi3w8sc9YSm9SWtOXmPU4OIKzsgvd80rySypFJLiYoOyBKT4uHj00_UNM5LKqkwLM3J5AJdqxMA8AAAA&q=NSE%3A+RCOM&oq=re&gs_l=finance-immersive.1.1.81l3.4679.4841.0.11776.2.2.0.0.0.0.183.183.0j1.1.0....0...1.1.64.finance-immersive..1.1.182....0.DbadqiPzKBg#scso=_mTGYXIuAOffUz7sP1ZmIkAw2:0&wptab=COMPARE').text

soup = BeautifulSoup(req,'lxml')
#print(soup.prettify())

section = soup.find('span',class_='CzXipe')

print(type(section))