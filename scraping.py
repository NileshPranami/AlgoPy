from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('cms_scrape.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline','summary','video_link'])
source= requests.get('http://coreyms.com').text
soup = BeautifulSoup(source,'lxml')

for article in soup.find_all('article'):
    
    headline = article.h2.a.text
    print(headline)
    summary = article.find('div',class_='entry-content').p.text
    print(summary)
    try:
        src = article.find('iframe',class_='youtube-player')['src']
        vid_id = src.split('/')[4]
        vid_id = vid_id.split('?')[0]
        vid_link = f'https://youtube.com/watch?v={vid_id}'
    
    except Exception as e:
        vid_link = None

    print(vid_link)

    csv_writer.writerow([headline,summary,vid_link])
    print('\n')

csv_file.close()