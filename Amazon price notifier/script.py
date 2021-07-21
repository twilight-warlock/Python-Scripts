import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
from time import sleep

link = input("Enter product page url: ")

while True:
    r = requests.get(link)
    content = r.content
    toast = ToastNotifier()
    soup = BeautifulSoup(content, "html.parser")
    price_type = "regular price"
    try:
        try:
            price = soup.find("span",{"id":"priceblock_ourprice"}, text=True)
            price = price.text.split()[1]
            price = price.replace(",","")
            toast.show_toast("Product Notification", "Product available at Regular price")
        except:
            price = soup.find("span",{"id":"priceblock_dealprice"})
            price = price.text.split()[1]
            price = price.replace(",","")
            price_type = "Offer price"
            toast.show_toast("Product Notification", "Product available at Offer price")

    except:
        price_type = "Product not available"

    print(price_type)
    sleep(10)

