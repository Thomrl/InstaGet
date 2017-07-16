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
print(imageurl)
username =  uInput.split("=", 1)[1]
print("Username = " + username)

filename = re.findall(r"[A-Z]\w+",uInput)
filename = str(filename)[2:-2]
print(filename)
pic = ".jpg"

#Look for display url and its img link
imgurl = re.findall(r"display_url\S+\s\S+", str(soup))
imgurl = re.findall(r"http\S+\jpg", str(imgurl))
#print("Regex found = " + str(imgurl))

vidurl = re.findall(r"http\S+.mp4", str(soup))
#print(vidurl)

yt = re.findall(r"youtube", str(soup))

def splitter():
    print("")
    print("-------------------------------------------------------------------")
    print("")

def dlpic():
    file = open(saveas, "wb")
    for chunk in image.iter_content(100000):
        file.write(chunk)
    file.close()
    print("File = " + saveas +" saved to: " + curpath)
#
if len(imgurl) > 1:
    print("instagram gallery detected")
    print("Images found = " +str(len(imgurl)-1))
    count = len(imgurl)
    for i in range(1, count):
        splitter() #-----------------------------------------------------------------
        image = requests.get(imgurl[i])
        print("Imageurl = " + imageurl)
        print("Filename = " + filename + str(i) + ".jpg")
        saveas = username + "_" + filename + str(i) + ".jpg"
        dlpic() # open > DL > Close function
elif len(yt) > 1:
    print("youtube link detected")
    splitter() #---------------------------------------------------------------------
    yt = yt[0]
    os.chdir("notInstagram")
    curpath = os.getcwd()
    #print(imgurl)
    print("a")
    print("Images found = 1")
    image = requests.get(imageurl)
    filename = username
    print("Imageurl = " + imageurl)
    print("Filename = " + filename)
    saveas = username + pic
    dlpic() # open > DL > Close function
elif len(vidurl) > 1:
    print("instagram video detected")
    splitter() #---------------------------------------------------------------------
    vidurl = vidurl[0]
    video = requests.get(vidurl)
    #filename = vidurl[53:]
    print("Videourl = " + vidurl)
    print("Filename = " + filename)
    saveas = username + "_" + filename + ".mp4"
    file = open(saveas, "wb")
    for chunk in video.iter_content(100000):
        file.write(chunk)
    file.close()
    print("File = " + saveas + " saved to: " + curpath)
    splitter()
    #print(imgurl)
    print("Images found = " +str(len(imgurl)))
    image = requests.get(imageurl)
    print("Imageurl = " + imageurl)
    print("Filename = " + filename)
    saveas = username + "_" + filename + pic
    dlpic() # open > DL > Close function
else:
    print("single picture link")
    splitter() #---------------------------------------------------------------------
    #print(imgurl)
    print("Images found = " +str(len(imgurl)))
    image = requests.get(imageurl)
    print("Imageurl = " + imageurl)
    print("Filename = " + filename)
    saveas = username + "_" + filename + pic
    dlpic() # open > DL > Close function
