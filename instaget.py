#! python3.5
import bs4 as bs, requests, sys, os, pyperclip, re

if len(sys.argv) > 1: #If windows RUN gets more words than 1 it assumes that the seconds word is the link and uses it
    uInput = " ".join(sys.argv[1:])
else:                 #If the script just gets started without additional input it will take what's in the clipboard (Ctrl+c)
    uInput = pyperclip.paste()

sauce = requests.get(uInput)                #Python gets the webpage
soup = bs.BeautifulSoup(sauce.text, "lxml") #making the sauce into soup

print("Given url: " +uInput)        #Shows the user which URL was passed
if len(re.findall(r"twitch", str(soup))) < 10:
    username =  uInput.split("=", 1)[1] #Gets the instagram username to better organize downloaded pictures

#REGEX SEARCHES
filename = re.findall(r"[A-Z]\S\w+",uInput)
filename = str(filename)[2:-2]
IGimageUrl = re.findall(r"display_url\S+\s\S+", str(soup))
IGimageUrl = re.findall(r"http\S+\jpg", str(IGimageUrl))
videoUrl = re.findall(r"http\S+.mp4", str(soup))
YTimageURL = re.findall(r"https://i.ytimg.com\S+.jpg", str(soup))
twitchUrl = re.findall(r"http.+?[^\"]*", str(videoUrl))
twitchTitle = re.findall(r"channel_title:.+\"", str(soup))
twitchTitle = re.findall(r"\".+\"", str(twitchTitle))
twitchTitle = str(twitchTitle)[3:-3]

def splitter(detected):
    print(detected+"\n-------------------------------------------------------------------\n")

def infoandget(typeUrl, ftype, fext): #typeUrl e.g imageUrl - filetype e.g image - fileextension e.g .jpg
    if filename == username: #If it's a youtube or twitch link
        saveas = filename + fext
        os.chdir("E:\\instagram\\notInstagram")  #Chosen directory
    else:
        saveas = username + "_" + filename + fext
        os.chdir("E:\\instagram") #Chosen directory
    curpath = os.getcwd()         #puts the dir into a variable
    file = open(saveas, "wb")
    for chunk in (ftype).iter_content(100000):
        file.write(chunk)
    file.close()
    print("Filename = " + filename + fext + "\nFound url = " + typeUrl + "\nFile = " + saveas +" saved to: " + curpath) #All the info
#
if len(re.findall(r"youtube", str(soup))) > 10:
    #YOUTUBE IS SPECIAL
    splitter("Youtube thumbnail") #---------------------------------------------------------------------
    imageUrl = YTimageURL[0]
    image = requests.get(imageUrl)
    filename = username
    infoandget(imageUrl, image, ".jpg")
elif len(re.findall(r"twitch", str(soup))) > 10:
    #TWITCH CLIPS
    splitter("Twitch clip - These takes some time. Please be patient") #---------------------------------------------------------------------
    videoUrl = twitchUrl[0]
    video = requests.get(videoUrl)
    filename = re.split('\"|:', str(twitchTitle))[0] #Lots of clip titles seem to have | or : and windows cant use that for filenaming
    username = filename
    infoandget(videoUrl, video, ".mp4")
elif len(IGimageUrl) > 1:
    #INSTAGRAM GALLERY
    print("Instagram gallery " + "- Images found = " +str(len(IGimageUrl)-1))
    for i in range(1, len(IGimageUrl)):
        splitter("") #-----------------------------------------------------------------
        imageUrl = IGimageUrl
        image = requests.get(imageUrl[i])
        filename = filename + str(i)
        imageUrl = imageUrl[i]
        infoandget(imageUrl, image, ".jpg")
elif len(videoUrl) > 1:
    #INSTAGRAM VIDEO
    splitter("Instagram video") #---------------------------------------------------------------------
    videoUrl = videoUrl[0]
    video = requests.get(videoUrl)
    infoandget(videoUrl, video, ".mp4")
    splitter("") #---------------------------------------------------------------------
    imageUrl = IGimageUrl[0]
    image = requests.get(imageUrl)
    infoandget(imageUrl, image, ".jpg")
else:
    #INSTAGRAM 1 picture
    splitter("Instagram picture") #---------------------------------------------------------------------
    imageUrl = IGimageUrl[0]
    image = requests.get(imageUrl)
    infoandget(imageUrl, image, ".jpg")
