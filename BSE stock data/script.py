from bsedata.bse import BSE
from time import sleep
from win10toast import ToastNotifier

hr = ToastNotifier()
b = BSE()

scriptCode = input("Enter company script code: ")
cp = int(input("Enter cost price: "))
lowerBound = int(input("Enter give up price: "))
upperBound = int(input("Enter notifier price: "))

while True:
    data = b.getQuote(scriptCode)
    price = data["currentValue"]
    print(price)
    
    if(price < lowerBound):
        print("Sell now")
    elif(price>lowerBound and price>cp and price<upperBound):
        print("Profittt")
    elif(price >= upperBound):
        print("Target hit, current price is",price)
        hr.show_toast("Target hit, current price is",str(price))

    sleep(2)