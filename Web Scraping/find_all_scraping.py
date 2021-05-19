# This script contains tutorial of finalall() and find() method of BeautifulSoup
# For reference : https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find
# Created By : Shivam Sharma
# Created On : 6th May 2021

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, features='html.parser')

# we will use findall() methd to find out all the span tags with class name green.
# find_all takes two parameters bsObj.find_all(tagName, tagAttributes)
nameList = bsObj.findAll('span', {'class':'green'})

for name in nameList:
    # get_text() method separates the content from the tags.
    print(name.get_text())
    # if you are working with a large block of text that contains many hyperlinks, 
    # paragraphs, and other tags, all those will be stripped away and you’ll be 
    # left with a tagless block of text.

# find(name, attrs, recursive, string, **kwargs)
# findAll(tag, attributes, recursive, text, limit, keywords)

# Following example will return a list of all the header tags in a document.
# .find_all({'h1', 'h2', 'h3', 'h4', 'h5', 'h6'})

# Followinf function would return both the green and red span tags in the HTML document.
# .find_all("span", {"class" : "green", "class" : "red"})

nameList = bsObj.findAll(text = 'the prince')
# print(len(nameList))

allText = bsObj.findAll(id="text")
# print(allText[0].get_text())
# OR
# allText = bsObj.findAll("", {"id":"text"})
# print(allText.get_text())

a = bsObj.find_all(class_="green")
print(a[0].get_text())


