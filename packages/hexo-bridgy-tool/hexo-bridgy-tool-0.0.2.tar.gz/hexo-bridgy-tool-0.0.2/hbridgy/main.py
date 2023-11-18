import argparse
import time

import bs4
import lxml.html

parser = argparse.ArgumentParser()

parser.add_argument("name")
parser.add_argument("image")

args = parser.parse_args()

def main():
    start = time.time()
    with open("_redirects", "w", encoding="utf-8") as fp:
        fp.write(
            ".well-known/webfinger?resource=acct:blog-aqc.pages.dev@blog-aqc.pages.dev https://fed.brid.gy/.well-known/webfinger?resource=acct:blog-aqc.pages.dev@blog-aqc.pages.dev"
        )
    with open("index.html", mode="rt", encoding="utf-8") as f:
        soup = bs4.BeautifulSoup(f.read(), "lxml")

    h_card = soup.new_tag("span", style="display:none;", **{"class": "h-card"})
    u_url = soup.new_tag("a", rel="me", href="/", **{"class": "u-url"})
    u_url.string = args.name
    h_card.append(u_url)
    u_photo = soup.new_tag("a", src=args.image, **{"class": "u-photo"})
    h_card.append(u_photo)
    soup.find("head").append(h_card)

    with open("index.html", "w", encoding="utf-8") as index:
        index.write(str(soup.prettify()))

    end = time.time()
    print("Done✨ in {}s.".format(end - start))
