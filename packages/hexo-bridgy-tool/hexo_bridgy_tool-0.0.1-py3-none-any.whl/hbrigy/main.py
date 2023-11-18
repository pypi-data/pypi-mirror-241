import argparse

import bs4
import lxml.html

parser = argparse.ArgumentParser()

parser.add_argument('name')
parser.add_argument('image')

#args = parser.parse_args()

class args:
    name = "sonyakun"
    image = "https://github.com/sonyakun.png"

with open('index.html', mode='rt', encoding='utf-8') as f:
    soup = bs4.BeautifulSoup(f.read(), 'lxml')

links = soup.find_all('a')

h_card = soup.new_tag('span', **{'class': 'h-card'})
u_url = soup.new_tag('a', rel="me", href="/",**{'class': 'u-url'})
u_url.string = args.name
soup.find('span', **{'class': 'h-card'}).append(u_url)
u_photo = soup.new_tag('a', src=args.image,**{'class': 'u-photo'})
soup.find('span', **{'class': 'h-card'}).append(u_photo)
soup.find('head').append(h_card)

with open("index.html", "w", encoding='utf-8') as index:
    index.write(str(soup))