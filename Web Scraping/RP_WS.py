import re 
from urllib.request import urlopen
from bs4 import BeautifulSoup

# we will open the url
url = 'http://olympus.realpython.org/profiles/dionysus'
page = urlopen(url)
html = page.read().decode('utf-8')

# We will write pattern to find title in html
pattern = '<title.*?>.*?</title.*?>'
match_result = re.search(pattern, html, re.IGNORECASE)
title = match_result.group()
# now we will remove html tags
title = re.sub("<.*?>", "", title)
# print(f'Title is : {title}\n')

# Now we will find more tags
for strg in ['Name: ', 'Favorite Color: ']:
    strg_index = html.find(strg)
    text_start_index = strg_index + len(strg)

    end_strg = html[text_start_index:].find('<')
    tex_end = text_start_index + end_strg

    raw_text = html[text_start_index:tex_end]
    clean_text = raw_text.strip('\r\n\t')
    print(clean_text)


#* Above work can be done by Beautiful Soup like this
soup = BeautifulSoup(html, "html.parser")
print(soup.get_text())

#* Finding tags using Beautiful Soup, find_all returns a list
#* it will return <img src="/static/dionysus.jpg"/>
#* src is a attribute and to deal with it, we do this.
for i in soup.find_all('img'):
    print(i['src'])

#* ALSO WE CAN USE CRETAIN TAGS DIRECTLY
print(soup.title)
#* TO FILTER OUT TAGS 
print(soup.title.string)

