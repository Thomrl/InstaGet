#! python3.5
import bs4 as bs
import requests, webbrowser
import sys, os

uInput = sys.argv[1] #instagram link please

sauce = requests.get(uInput) #python looks up the link
print(uInput) #python tells you which link it looks at
#sauce.raise_for_status()
soup = bs.BeautifulSoup(sauce.text, "lxml") #making the sauce into soup

find = soup.find("meta", property="og:image") #python looks for this the source code
print(find) #python is proud that it found it and tells you so you can be proud with it
findstr = str(find) 
slice1 = findstr[15:]
imageurl = slice1[:-23]
filename = imageurl[57:]
print("imageurl is = " + imageurl)
print("filename = " + filename)

instaimg = requests.get(imageurl)
instaimg.status_code
os.chdir("e:\\test") #image gets saved here
curpath = os.getcwd()
file = open(filename, "wb")
for chunk in instaimg.iter_content(100000):
    file.write(chunk)
file.close()
print("File should be saved to: " + curpath)
