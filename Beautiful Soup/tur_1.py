from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://olympus.realpython.org"
f_url = url+'/profiles'
page = urlopen(f_url)
html = page.read().decode('utf-8')

soup = BeautifulSoup(html, "html.parser")

for tags in soup.find_all('a'):
    print(url+tags['href'])