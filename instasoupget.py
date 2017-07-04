import bs4 as bs
import requests, webbrowser
import sys, os

curpath = os.getcwd()


sauce = requests.get("<HERE - instagram post url - HERE>")
sauce.raise_for_status()
soup = bs.BeautifulSoup(sauce.text, "lxml")

#find = soup.select("meta")
#print(find)
#for meta in find:
 #   if meta.endswith("og:image\"/>"):
  #      print(meta)

find = soup.find("meta", property="og:image")
print(find)
#title = soup.find("meta",  property="og:title")
findstr = str(find)
slice1 = findstr[15:]
imageurl = slice1[:-23]
filename = imageurl[57:]
print("imageurl is = " + imageurl)
print("filename = " + filename)

instaimg = requests.get(imageurl)
instaimg.status_code
#len(instaimg.text)
file = open(filename, "wb")
for chunk in instaimg.iter_content(100000):
    file.write(chunk)
file.close()
print("File should be saved to: " + curpath)
#webbrowser.open(imageurl)
