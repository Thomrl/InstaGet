#! python3.5
import bs4 as bs, requests, sys, os

uInput = sys.argv[1] #instagram link please

sauce = requests.get(uInput) #python looks up the link
print("Given url: " +uInput) #python tells you which link it looks at
#sauce.raise_for_status()
soup = bs.BeautifulSoup(sauce.text, "lxml") #making the sauce into soup

find = soup.find("meta", property="og:image") #python looks for this in the source code
findstr = str(find) 
imageurl = findstr[15:-23]
filename = imageurl[57:]
username =  uInput.split("=", 1)[1]
print("imageurl = " + imageurl)
print("filename = " + filename)
print("username = " + username)
print("saved as = " + username+"_"+filename)

instaimg = requests.get(imageurl)
#instaimg.status_code
os.chdir("E:\\instagram") #Where you want i saved
curpath = os.getcwd() #passing the directory to a variable so python can print it later
file = open(username+"_"+filename, "wb")
for chunk in instaimg.iter_content(100000):
    file.write(chunk)
file.close()
print("File should be saved to: " + curpath)
