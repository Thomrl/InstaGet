#! python3.5
import bs4 as bs
import sys, os, requests, re

url = "instagram link"

sE = re.compile("display_url")
sep = str(sE)


sauce = requests.get(url)
sauce.raise_for_status()
soup = bs.BeautifulSoup(sauce.text[3300:], "lxml")

found = re.findall(r"display_url\S+\s\S+", str(soup))
strfound = str(found)
#print(strfound)
slam = re.findall(r"http\S+\jpg", str(strfound))
print(slam)
print(len(slam))

for i in range(len(slam)):
    print("Slam nummer "+str(i)+" : "+slam[i])
    imgurl = requests.get(slam[i])
    file = open("image"+str(i)+".jpg", "wb")
    print("Saved as = " + "image"+str(i)+".jpg")
    for chunk in imgurl.iter_content(100000):
        file.write(chunk)
    file.close()

#if

#for i in found():
#    print(i)

#print(found[0])
#for i in found():
#    print(i)
#print(soup)
