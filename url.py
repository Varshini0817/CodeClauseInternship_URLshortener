import pyshorteners

url = input('Enter URL:')

def shorten(url):
    s=pyshorteners.Shortener()
    print(s.tinyurl.short(url))

shorten(url)
