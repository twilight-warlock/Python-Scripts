from yahoo_fin import stock_info
from time import sleep

brand = input("Enter company name: ")
cp = int(input("Enter cost price: "))
lowerBound = int(input("Enter sell price: "))
upperBound = int(input("Enter notifier price: "))
while True:
    sleep(2)
    price = stock_info.get_live_price(brand)

    if(price < lowerBound):
        print("Sell now")
    elif(price>lowerBound and price>cp):
        print("Profittt")
    elif(price > upperBound):
        print("Target hit, current price is",price)

