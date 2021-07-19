from pyshorteners import Shortener

link = input("Enter the link: ")

shortener = Shortener()

shortenedLink = shortener.tinyurl.short(link)

print(shortenedLink)