# Inspired in https://www.instagram.com/p/CCi43d8gq_t/

import pyshorteners

shortener = pyshorteners.Shortener()

url = input("Enter the url: ")

short_url = shortener.tynyurl.short(url)

print(short_url)
