import csv

books = []
with open("./names.txt") as f:
    for line in f:
        line = line.strip()
        if(line == "==="):
            break
        elif line == "" or line[0:2] == "!!":
            continue

        books.append([line])

with open("Books.csv", "w", newline='') as f:
    write = csv.writer(f)

    write.writerow(["Name"])
    write.writerows(books)
