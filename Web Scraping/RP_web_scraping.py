# First we will import urllib library

from urllib.request import urlopen

# Now we will save url we want to scrap
url = "http://olympus.realpython.org/profiles/aphrodite"

# we will open the url
page = urlopen(url)
# urlopen() returns a HTTPResponse object

# we will use HTTPResponse object's read method to read html text
html_bytes = page.read()
html = html_bytes.decode("utf-8")

# now we can print html to see html content
# print(html)

# now we will see different ways to extract info from html text

# 1. String method
# we will use find method to find text 
# find() returns index of first occurrence of text
title_index = html.find('<title>')
# print(title_index)
# above line will give index of title tag, we want index of title
start_index = title_index + len('<title>')
# like that we will find end index of title
end_index = html.find('</title>')

# finding html by slicing title from the string
title = html[start_index : end_index]
print(title)



