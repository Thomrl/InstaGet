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
IGimageUrl = re.findall(r"display_url\":.+?(?=\")", str(soup))
IGimageUrl = re.findall(r"http\S+\jpg", str(IGimageUrl))
videoUrl = re.findall(r"http\S+.mp4", str(soup))
YTimageURL = re.findall(r"https://i.ytimg.com\S+.jpg", str(soup))
twitchTitle = soup.select("title")[0].text
if 10 < len(re.findall(r"instagram", str(soup))): #I only need this on instagram links
    filename = re.findall(r"shortcode\":\"\w+",str(soup))[0] #This way the script finds the exact code/name instead of messing it up.
    filename = filename.split('\"', 2)[-1]                  #Deleting ['shortcode": " and ",'] so we get a code like this -> BYBmz_5DCfC
    username = re.findall(r"\(@\w+", str(soup))[0] 
    username = username.split("@", 1)[1]


#Function (Don't repeat yourself)
def infoandget(mediaUrl, fext, sText): #mediaUrl e.g twitchUrl[0] - fext e.g .mp4 - sText e.g "Twitch clip...."
    print("\n-------------------------------------------------------------------\n"+sText+"\n")
    if not 'username' in globals(): #This should be a twitch or youtube link.
        saveas = filename + fext    #Combining filename and file extension into 1 variable to make it look more clean.
        folder = re.findall(r"\w+", sText)[0] #Finding the first word of the information text, to easily organize folders.
        if not os.path.exists(folder): #To organize where the different media come  from
            os.mkdir(folder)        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        os.chdir(folder)            #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        if folder == "Twitch":
            for file in os.listdir():
                if saveas == file:
                    extraa = mediaUrl[-8:-4]
                    saveas = filename + "_" + extraa + fext
    else:
        saveas = username + "_" + filename + fext#Combining instagram username_filename and file extension into 1 variable to make it look more clean.
    curpath = os.getcwd()           #Information for the user
    media = requests.get(mediaUrl)  #So python loads the website with the media
    file = open(saveas, "wb")       #Saving the media to the computer
    for chunk in (media).iter_content(100000):#^^^^
        file.write(chunk)           #^^^^^^
    file.close()                    #^^^^^^
    try:
        print("Filename = " + filename + fext + "\nFound url = " + mediaUrl + "\nFile = " + saveas +" saved to: " + curpath) #All the info
    except UnicodeEncodeError:
        print("Error: A character in the filename couldnt be printed but the download should have been completed.\nFilename = " + "Could not be printed" + "\nFound url = " + mediaUrl + "\nFile = " +" saved to: " + curpath)
        
#YOUTUBE, TWITCH or INSTAGRAM?
if len(re.findall(r"youtube", str(soup))) > 10: #YOUTUBE THUMBNAIL------------------------
    filename = re.findall(r"=\S+", uInput)[0]
    filename = filename.split("=", 1)[1]
    infoandget(YTimageURL[0], ".jpg", "Youtube thumbnail")
elif len(re.findall(r"twitch", str(soup))) > 10:#TWITCH CLIPS-----------------------------
    print("Twitch clip - These takes some time. Please be patient")
    filename = str(twitchTitle)
    from selenium import webdriver
    browser = webdriver.Firefox()
    browser.get(uInput)
    elem = browser.find_element_by_css_selector(".tw-font-size-3")
    twitchTitle = re.findall(r"[^[|\\☆\":<>/\*. ]\w+", str(elem.text)) #To avoid characters that gives errors in filenames
    filename = " ".join(twitchTitle)
    elem = browser.find_element_by_css_selector(".player-video > video:nth-child(1)")
    twitchUrl = elem.get_attribute("src")
    browser.quit()
    infoandget(twitchUrl, ".mp4", "Twitch clip - "+filename)
elif len(IGimageUrl) > 1: #---------------------#INSTAGRAM GALLERY------------------------
    print("Instagram gallery " + "- Images found = " +str(len(IGimageUrl)-1))
    for i in range(1, len(IGimageUrl)):
        filename = filename + str(i)
        infoandget(IGimageUrl[i], ".jpg", "Image "+str(i))
elif len(videoUrl) > 1: #-----------------------#INSTAGRAM VIDEO--------------------------
    infoandget(videoUrl[0], ".mp4", "Instagram video")
    infoandget(IGimageUrl[0], ".jpg", "Video thumbnail")
else: #-----------------------------------------#INSTAGRAM PICTURE------------------------
    infoandget(IGimageUrl[0], ".jpg", "Instagram picture")
