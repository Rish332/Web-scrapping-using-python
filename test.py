from bs4 import BeautifulSoup
import urllib2
url = "http://blog.aiesec.in/"
u = urllib2.urlopen(url).read()
soup=BeautifulSoup(u)
print "#######################"
print soup.title
print "#######################"
print soup.title.string
print "#######################"
print soup.find_all("a")
print "#######################"
print soup.a.text
print "#######################"
all_links = soup.find_all("a")
for link in all_links:
    print link.get("href")
print "#######################"
print soup.find_all("img")
print "#######################"
img_links = soup.find_all("img")
for link in img_links:
    print link.get("src")
print "#######################"
date = soup.find_all('span',{'class' : 'date'})
for d in date:
    print d.text
print "#######################"
comment = soup.find_all('span',{'class' : 'custom_listing_comments'})
for c in comment:
    print c.text
print "END"
