import csv
import os
from dotenv import load_dotenv
import pyqrcode
import png


load_dotenv()

link = os.environ.get("link")

link = link.split("&")
newLink = []
for i in link:
    newLink.append(i.split("="))

allLinks = []

with open("./data.csv") as f:
    csv_reader = csv.reader(f, delimiter=',')
    line_count = 0
    os.mkdir("QRcode")
    for row in csv_reader:
        if line_count != 0:
            name = row[0].replace(" ", "+")
            newLink[1][1] = name
            newLink[2][1] = row[1]
            q1 = "=".join(newLink[0])
            q2 = "=".join(newLink[1])
            q3 = "=".join(newLink[2])

            url = q1+"&"+q2+"&"+q3

            qrcode = pyqrcode.create(url)
            qrcode.png(os.path.join(
                "QRcode", str(line_count)+".png"), scale=8)
            allLinks.append(qrcode)
        line_count += 1
print(allLinks)
print("Created QRcodes for all members")
