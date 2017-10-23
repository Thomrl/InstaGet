#! python3.5
import bs4 as bs, requests, sys, os, pyperclip, re

location = "C:\\InstaGet"#------------#THE MEDIA WILL BE SAVED TO THIS FOLDER.
if not os.path.exists(location):      #To make sure there's a folder to save the media in
    os.mkdir(location)                #^^^^^^
os.chdir(location)                    #Change the directory to this folder

if len(sys.argv) > 1: #If windows RUN gets more words than 1 it assumes that the second word is the link and uses it
    uInput = " ".join(sys.argv[1:])
else:                 #If the script just gets started without additional input it will take what's in the clipboard (Ctrl+c)
    uInput = pyperclip.paste()
print("Given url: " +uInput)#Shows the user which URL was given

sauce = requests.get(uInput)                #Python gets the webpage
soup = bs.BeautifulSoup(sauce.text, "lxml") #making the sauce into soup

#REGEX SEARCHES / Other info - To find urls and information
filename = re.findall(r"shortcode\"\S+\s\S\S+",str(soup)) #This way the script finds the exact code/name instead of messing it up. 
filename = "".join(str(filename)[15:-4])                  #Deleting ['shortcode": " and ",'] so we get a code like this -> BYBmz_5DCfC
IGimageUrl = re.findall(r"display_url\S+\s\S+", str(soup))
IGimageUrl = re.findall(r"http\S+\jpg", str(IGimageUrl))
videoUrl = re.findall(r"http\S+.mp4", str(soup))
YTimageURL = re.findall(r"https://i.ytimg.com\S+.jpg", str(soup))
twitchUrl = re.findall(r"http.+?[^\"]*", str(videoUrl))
twitchTitle = soup.select("title")[0].text
twitchTitle = re.findall(r"[^|\\☆\":<>/\*. ]\w+", str(twitchTitle)) #To avoid characters that gives errors in filenames
twitchTitle = " ".join(twitchTitle)
if 10 < len(re.findall(r"instagram", str(soup))): #I only need this on instagram links
    username = re.findall(r"@\w+", str(soup))[0] 
    username = username.split("@", 1)[1]

#Function (Don't repeat yourself)
def infoandget(mediaUrl, fext, sText): #mediaUrl e.g twitchUrl[0] - fext e.g .mp4 - sText e.g "Twitch clip...."
    print("\n-------------------------------------------------------------------\n"+sText+"\n")
    if not 'username' in globals(): #This should be a twitch or youtube link. 
        saveas = filename + fext    #Combining filename and file extension into 1 variable to make it look more clean.
        folder = re.findall(r"\w+", sText)[0] #Finding the first word of the information text, to easily organize folders.
        folder = "".join(folder)    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        if not os.path.exists(folder): #To organize where the different media come  from
            os.mkdir(folder)        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        os.chdir(folder)            #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    else:
        saveas = username + "_" + filename + fext#Combining instagram username_filename and file extension into 1 variable to make it look more clean.
    curpath = os.getcwd()           #Information for the user
    media = requests.get(mediaUrl)  #So python loads the website with the media
    file = open(saveas, "wb")       #Saving the media to the computer
    for chunk in (media).iter_content(100000):#^^^^
        file.write(chunk)           #^^^^^^
    file.close()                    #^^^^^^
    print("Filename = " + filename + fext + "\nFound url = " + mediaUrl + "\nFile = " + saveas +" saved to: " + curpath) #All the info
    
#YOUTUBE, TWITCH or INSTAGRAM?
if len(re.findall(r"youtube", str(soup))) > 10: #YOUTUBE THUMBNAIL------------------------
    filename = re.findall(r"=\w+", uInput)[0]
    filename = filename.split("=", 1)[1]
    infoandget(YTimageURL[0], ".jpg", "Youtube thumbnail")
elif len(re.findall(r"twitch", str(soup))) > 10:#TWITCH CLIPS-----------------------------
    filename = str(twitchTitle)
    infoandget(twitchUrl[0], ".mp4", "Twitch clip - These takes some time. Please be patient")
elif len(IGimageUrl) > 1: #---------------------#INSTAGRAM GALLERY------------------------
    print("Instagram gallery " + "- Images found = " +str(len(IGimageUrl)-1))
    for i in range(1, len(IGimageUrl)):
        filename = re.findall(r"shortcode\"\S+\s\S\S+",str(soup))[0]
        filename = "".join(str(filename)[13:-2]) + str(i)
        infoandget(IGimageUrl[i], ".jpg", "Image "+str(i))
elif len(videoUrl) > 1: #-----------------------#INSTAGRAM VIDEO--------------------------
    infoandget(videoUrl[0], ".mp4", "Instagram video")
    infoandget(IGimageUrl[0], ".jpg", "Video thumbnail")
else: #-----------------------------------------#INSTAGRAM PICTURE------------------------
    infoandget(IGimageUrl[0], ".jpg", "Instagram picture")
