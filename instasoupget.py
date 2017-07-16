#! python3.5
import bs4 as bs, requests, sys, os, pyperclip, re

if len(sys.argv) > 1:
    uInput = " ".join(sys.argv[1:])
else:
    uInput = pyperclip.paste()
    
os.chdir("E:\\instagram")
curpath = os.getcwd()

sauce = requests.get(uInput) #python looks up the link
print("Given url: " +uInput) #python tells you which link it looks at
#sauce.raise_for_status()
soup = bs.BeautifulSoup(sauce.text, "lxml") #making the sauce into soup

find = soup.find("meta", property="og:image") #python looks for this in the source code
findstr = str(find) 
imageurl = findstr[15:-23]
username =  uInput.split("=", 1)[1]
#print("Imageurl = " + imageurl)
#print("Filename = " + filename)
print("Username = " + username)

imgurl = re.findall(r"display_url\S+\s\S+", str(soup))
imgurl = str(imgurl)
imgurl = re.findall(r"http\S+\jpg", imgurl)
#print(imgurl)

vidurl = re.findall(r"http\S+.mp4", str(soup))
#print(vidurl)

yt = re.findall(r"youtube", str(soup))

#
if len(imgurl) > 1:
    print("instagram gallery detected")
    print("Images found = " +str(len(imgurl)-1))
    count = len(imgurl)
    for i in range(1, count):
        print("")
        print("-------------------------------------------------------------------")
        print("")
        imageurl = imgurl[i]
        image = requests.get(imgurl[i])
        imageurl = imageurl
        filename = imageurl[71:]
        print("Imageurl = " + imageurl)
        print("Filename = " + filename)
        file = open(username + "_" + filename, "wb")
        for chunk in image.iter_content(100000):
            file.write(chunk)
        file.close()
        print("File = " + username + "_" + filename + " saved to: "+curpath)
elif len(vidurl) > 1:
    print("instagram video detected")
    print("")
    print("-------------------------------------------------------------------")
    print("")
    vidurl = vidurl[0]
    video = requests.get(vidurl)
    filename = vidurl[53:]
    print("Videourl = " + vidurl)
    print("Filename = " + filename)
    file = open(username + "_" + filename, "wb")
    for chunk in video.iter_content(100000):
        file.write(chunk)
    file.close()
    print("File = " + username + "_" + filename + " saved to: " + curpath)
    print("")
    print("-------------------------------------------------------------------")
    print("")
    #print(imgurl)
    print("Images found = " +str(len(imgurl)))
    image = requests.get(imageurl)
    filename = imageurl[71:]
    print("Imageurl = " + imageurl)
    print("Filename = " + filename)
    file = open(username + "_" + filename, "wb")
    for chunk in image.iter_content(100000):
        file.write(chunk)
    file.close()
    print("File = " + username + "_" + filename+" saved to: " + curpath)
elif len(yt) > 1:
    print("youtube link detected")
    print("")
    print("-------------------------------------------------------------------")
    print("")
    yt = yt[0]
    os.chdir("notInstagram")
    curpath = os.getcwd()
    #print(imgurl)
    print("Images found = 1")
    image = requests.get(imageurl)
    filename = username
    print("Imageurl = " + imageurl)
    print("Filename = " + filename)
    file = open(username+".jpg", "wb")
    for chunk in image.iter_content(100000):
        file.write(chunk)
    file.close()
    print("File = " + filename + ".jpg"+" saved to: " + curpath)
else:
    print("single picture link")
    print("")
    print("-------------------------------------------------------------------")
    print("")
    #print(imgurl)
    print("Images found = " +str(len(imgurl)))
    image = requests.get(imageurl)
    filename = imageurl[57:]
    print("Imageurl = " + imageurl)
    print("Filename = " + filename)
    file = open(username + "_" + filename, "wb")
    for chunk in image.iter_content(100000):
        file.write(chunk)
    file.close()
    print("File = " + username + "_" + filename+" saved to: " + curpath)
