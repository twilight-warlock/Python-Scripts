import csv, math
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep


def createStockCsv(name, link, start):
    browser = webdriver.Chrome(
        executable_path="E:\chromedriver_win32\chromedriver.exe")
    browser.get(link)

    sleep(20)

    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')

    text = soup.find_all(text=True)
    output = []
    blacklist = [
        'header',
        'meta',
        'head',
        'input',
        "style"
    ]

    for t in text:
        if t.parent.name not in blacklist and t.strip() != "" and t.strip() != ",":
            output.append(t.strip())

    # print(len(output[start:-20]))
    # print(output[start:-20])

    output = output[start:-20]
    lol = []

    print("Creating file for "+name)

    for i in range(0, len(output), 5):
        percent = "UP "
        res = True
        try:
            float(output[i+3][1:])
        except:
            res = False
        if res:
            if output[i+4][0] == "▼":
                percent = "DN "
            # print([output[i], output[i+1], output[i+2],
            #        output[i+3], percent + output[i+4][1:]])
            lol.append([output[i], output[i+1], output[i+2].split(".")[0],
                        output[i+3], percent + output[i+4][1:]])
        else:
            val = "0"
            # print([output[i], output[i+1], output[i+2], val, val])
            lol.append([output[i], output[i+1], output[i+2], val, val])
            output.insert(i+3, "0")
            output.insert(i+4, "0")

    field = ["Company Name", "Market Cap",
             "Close Price", "Price Change", "Percentage"]

    # print(lol)

    with open(name+'.csv', 'w', newline="") as f:
        write = csv.writer(f)

        write.writerow(field)
        write.writerows(lol)

    print(name+" file created")


data = [
    {
        "name": "Nifty50",
        "link": "https://web.stockedge.com/share/nifty-50/14801?section=all",
        "start": 20
    },
    {
        "name": "Nifty Bank",
        "link": "https://web.stockedge.com/share/nifty-bank/14796?section=all",
        "start": 20
    },
    {
        "name": "Nifty Midcap 100",
        "link": "https://web.stockedge.com/share/nifty-midcap-100/16061?section=all",
        "start": 18
    },
    {
        "name": "Nifty Smallcap 100",
        "link": "https://web.stockedge.com/share/nifty-smallcap-100/16062?section=all",
        "start": 18
    },
    {
        "name": "Nifty Pharma",
        "link": "https://web.stockedge.com/share/nifty-pharma/14820?section=all",
        "start": 18
    },
    {
        "name": "Nifty FMCG",
        "link": "https://web.stockedge.com/share/nifty-fmcg/14816?section=all",
        "start": 18
    },
]

for i in data:
    createStockCsv(i["name"], i["link"], i["start"])
