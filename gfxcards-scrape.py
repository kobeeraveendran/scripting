from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=grpahics%20cards'

# open connection to webpage
urlClient = urlopen(url)

# reads page html data into variable
page_html = urlClient.read()

# close connection to html page
urlClient.close()

page_soup = soup(page_html, 'html.parser')

containers = page_soup.findAll("div", {"class": "item-container"})

filename = 'product-list.csv'
file = open(filename, "w")

headers = 'brand, card name, card price, shipping_cost\n'

file.write(headers)

for curr_item in containers:
    brand = curr_item.div.div.a.img["title"]

    # finds the containers with class name item-title
    title_container = curr_item.findAll("a", {"class": "item-title"})
    card_name = title_container[0].text

    # graphics card price
    price_container = curr_item.findAll("li", {"class": "price-current"})
    card_price_base = price_container[0].strong.text
    card_price_super = price_container[0].sup.text

    # shipping price with extraneous whitespace removed
    shipping_container = curr_item.findAll("li", {"class": "price-ship"})
    shipping_cost = shipping_container[0].text.strip()

    # used for testing correctness of scrapes
    print("brand: " + brand)
    print("card name: " + card_name)
    print("shipping cost: " + shipping_cost)
    print("card price: " + card_price_base + card_price_super)

    card_name = card_name.replace(",", "|")

    file.write(brand + ", " + card_name + ", " + "$" + card_price_base + card_price_super + ", " + shipping_cost + "\n")

file.close()
