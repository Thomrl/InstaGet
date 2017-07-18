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
username =  uInput.split("=", 1)[1]
soup = bs.BeautifulSoup(sauce.text, "lxml") #making the sauce into soup

#REGEX SEARCHES
filename = re.findall(r"[A-Z]\S\w+",uInput)
filename = str(filename)[2:-2]
IGimageUrl = re.findall(r"display_url\S+\s\S+", str(soup))
IGimageUrl = re.findall(r"http\S+\jpg", str(IGimageUrl))
videoUrl = re.findall(r"http\S+.mp4", str(soup))
youtube = re.findall(r"youtube", str(soup))
ogImage = re.findall(r"https://i.ytimg.com\S+.jpg", str(soup))

def splitter(detected):
    print(detected)
    print("-------------------------------------------------------------------")
    print("")

def info():
    print("Filename = " + filename)
    print("Imageurl = " + imageUrl)

def getthis(ftype):
    file = open(saveas, "wb")
    for chunk in (ftype).iter_content(100000):
        file.write(chunk)
    file.close()
    print("File = " + saveas +" saved to: " + curpath)
#
if len(youtube) > 10:
    #YOUTUBE IS SPECIAL
    splitter("Youtube thumbnail") #---------------------------------------------------------------------
    imageUrl = ogImage[0]
    os.chdir("notInstagram")
    curpath = os.getcwd()
    filename = username
    image = requests.get(imageUrl)
    info()
    saveas = username + ".jpg"
    getthis(image) # open > DL > Close function
elif len(IGimageUrl) > 1:
    #INSTAGRAM GALLERY
    print("Instagram gallery " + "- Images found = " +str(len(IGimageUrl)-1))
    for i in range(1, len(IGimageUrl)):
        splitter("") #-----------------------------------------------------------------
        ImageUrl = IGimageUrl
        image = requests.get(ImageUrl[i])
        print("Filename = " + filename + str(i) + ".jpg")
        print("Imageurl = " + ImageUrl[i])
        saveas = username + "_" + filename + str(i) + ".jpg"
        getthis(image) # open > DL > Close function
elif len(videoUrl) > 1:
    #INSTAGRAM VIDEO
    splitter("Instagram video") #---------------------------------------------------------------------
    videoUrl = videoUrl[0]
    video = requests.get(videoUrl)
    print("Filename = " + filename)
    print("Videourl = " + videoUrl)
    saveas = username + "_" + filename + ".mp4"
    getthis(video)
    splitter("") #---------------------------------------------------------------------
    imageUrl = IGimageUrl[0]
    image = requests.get(imageUrl)
    info()
    saveas = username + "_" + filename + ".jpg"
    getthis(image) # open > DL > Close function
else:
    #INSTAGRAM 1 picture
    splitter("Instagram picture") #---------------------------------------------------------------------
    imageUrl = IGimageUrl[0]
    image = requests.get(imageUrl)
    info()
    saveas = username + "_" + filename + ".jpg"
    getthis(image) # open > DL > Close function
