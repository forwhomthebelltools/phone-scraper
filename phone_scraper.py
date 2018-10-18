import urllib2
from bs4 import BeautifulSoup
import string
 
name=raw_input('Enter the name of the owner - ')
owner = str.replace(name, " ", "+")

url = "http://www.paginebianche.it/ricerca?qs=" + owner + "&dv="
html=urllib2.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
print (" ")
print ("Take a look at your results for each " + name + ":")
 
street = soup.find_all('span', attrs={'itemprop':'streetAddress'})
tel = soup.find_all('span', attrs={'itemprop':'telephone'})
city = soup.find_all('span', attrs={'itemprop':'addressLocality'})

for x,y,z in zip(street,tel,city):
    print x.text, " - ", y.text, " - ", z.text




