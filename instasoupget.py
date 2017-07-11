#! python3.5
import bs4 as bs, requests, sys, os, pyperclip

if len(sys.argv) > 1:
    uInput = " ".join(sys.argv[1:])
else:
    uInput = pyperclip.paste()

sauce = requests.get(uInput) #python looks up the link
print("Given url: " +uInput) #python tells you which link it looks at
#sauce.raise_for_status()
soup = bs.BeautifulSoup(sauce.text, "lxml") #making the sauce into soup

find = soup.find("meta", property="og:image") #python looks for this in the source code
findstr = str(find) 
imageurl = findstr[15:-23]
filename = imageurl[57:]
username =  uInput.split("=", 1)[1]
print("Imageurl = " + imageurl)
print("Filename = " + filename)
print("Username = " + username)

instaimg = requests.get(imageurl)
#instaimg.status_code
os.chdir("E:\\instagram") #Where you want i saved
curpath = os.getcwd() #passing the directory to a variable so python can print it later
if len(filename) < 2:
    os.chdir("notInstagram")
    curpath = os.getcwd()
    print("Saved as = " + username+"_"+filename+".jpg")
    file = open(username+"_"+filename+".jpg", "wb")
else:
    file = open(username+"_"+filename, "wb")
    print("Saved as = " + username+"_"+filename)

for chunk in instaimg.iter_content(100000):
    file.write(chunk)
file.close()
print("File saved to: " + curpath)
