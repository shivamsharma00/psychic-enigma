#* This script contains the tutorial of mechanical soup.
# https://mechanicalsoup.readthedocs.io/en/stable/
import mechanicalsoup

# we will create a browser of mechanical soup
browser = mechanicalsoup.Browser()

url  = "http://olympus.realpython.org/login"
# url = 'https://www.instagram.com/'
#* we will request a page by browser
page = browser.get(url)
login_html = page.soup  

# We will input the id and password in the form
form = login_html.select("form")[0]
form.select("input")[0]['value'] = 'zeus'
form.select("input")[1]['value'] = 'ThunderDude'

#* pressing the submit button
#* we will send form object and URL of the login page.
profile_pages = browser.submit(form, page.url)
profile_soup = profile_pages.soup

print(profile_soup.title)
# if it will print next page of profile meaning successful login.