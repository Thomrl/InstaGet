#! python3.5
import bs4 as bs, requests, sys, os, pyperclip, re

#user input - Should be a link to either instagram or a youtube video
if len(sys.argv) > 1:
    uInput = " ".join(sys.argv[1:])
else:
    uInput = pyperclip.paste()

#Save the pictures in this directory  
os.chdir("E:\\instagram")
curpath = os.getcwd()

#Get the website and make it soup
sauce = requests.get(uInput) #python looks up the link
print("Given url: " +uInput) #python tells you which link it looks at
#sauce.raise_for_status()
soup = bs.BeautifulSoup(sauce.text, "lxml") #making the sauce into soup

#Look for meta the image in the soup (source code)
find = soup.find("meta", property="og:image") #python looks for this in the source code
imageurl = str(find)[15:-23]
username =  uInput.split("=", 1)[1]
pic = ".jpg"

#REGEX SEARCHES
filename = re.findall(r"[A-Z]\S\w+",uInput)
filename = str(filename)[2:-2]
imgurl = re.findall(r"display_url\S+\s\S+", str(soup))
imgurl = re.findall(r"http\S+\jpg", str(imgurl))
vidurl = re.findall(r"http\S+.mp4", str(soup))
yt = re.findall(r"youtube", str(soup))

def splitter(detected):
    print(detected)
    print("-------------------------------------------------------------------")
    print("")

def info():
    print("Filename = " + filename)
    print("Imageurl = " + imageurl)

def getthis(ftype):
    file = open(saveas, "wb")
    for chunk in (ftype).iter_content(100000):
        file.write(chunk)
    file.close()
    print("File = " + saveas +" saved to: " + curpath)
#
if len(imgurl) > 1:
    #INSTAGRAM GALLERY
    print("About: Instagram gallery " + "- Images found = " +str(len(imgurl)-1))
    for i in range(1, len(imgurl)):
        splitter("") #-----------------------------------------------------------------
        image = requests.get(imgurl[i])
        print("Filename = " + filename + str(i) + ".jpg")
        print("Imageurl = " + imgurl[i])
        saveas = username + "_" + filename + str(i) + ".jpg"
        getthis(image) # open > DL > Close function
elif len(yt) > 1:
    #YOUTUBE IS SPECIAL
    splitter("Youtube thumbnail") #---------------------------------------------------------------------
    yt = yt[0]
    os.chdir("notInstagram")
    curpath = os.getcwd()
    filename = username
    image = requests.get(imageurl)
    info()
    saveas = username + pic
    getthis(image) # open > DL > Close function
elif len(vidurl) > 1:
    #INSTAGRAM VIDEO
    #print("instagram video detected")
    splitter("Going to get: Instagram video and video ") #---------------------------------------------------------------------
    vidurl = vidurl[0]
    video = requests.get(vidurl)
    print("Filename = " + filename)
    print("Videourl = " + vidurl)
    saveas = username + "_" + filename + ".mp4"
    getthis(video)
    splitter("") #---------------------------------------------------------------------
    image = requests.get(imageurl)
    info()
    saveas = username + "_" + filename + pic
    getthis(image) # open > DL > Close function
else:
    #INSTAGRAM 1 picture
    #print("single picture link")
    splitter("Instagram picture") #---------------------------------------------------------------------
    image = requests.get(imageurl)
    info()
    saveas = username + "_" + filename + pic
    getthis(image) # open > DL > Close function
