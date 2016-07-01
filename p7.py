import urllib
from bs4 import BeautifulSoup

data1=urllib.urlopen("http://python-data.dr-chuck.net/known_by_Fikret.html").read()

k1=list()
l1=list()
lst1=list()


soup1=BeautifulSoup(data1,"html.parser")



tags1=soup1('a')

for tag in tags1:
    k1.append(tag.contents[0])
    l1.append(tag.get('href',None))

#print k1[2]
#print l1[2]

data2=urllib.urlopen(l1[2])

k2=list()
l2=list()

soup2=BeautifulSoup(data2,"html.parser")

tags2=soup2('a')

for tag in tags2:
    k2.append(tag.contents[0])
    l2.append(tag.get('href',None))

#print (k2[2])
#print (l2[2])

data3=urllib.urlopen(l2[2])

k3=list()
l3=list()

soup3=BeautifulSoup(data3,"html.parser")

tags3=soup3('a')

for tag in tags3:
    k3.append(tag.contents[0])
    l3.append(tag.get('href',None))

#print (k3[2])
#print (l3[2])

data4=urllib.urlopen(l3[2])

k4=list()
l4=list()

soup4=BeautifulSoup(data4,"html.parser")

tags4=soup4('a')

for tag in tags4:
    k4.append(tag.contents[0])
    l4.append(tag.get('href',None))

print (k4[2])
#print (l4[2])

