# InstaGet
Easily save instagram video/pictures, youtube thumbnails and twitch clips.

Just copy a link from instagram like: "https://www.instagram.com/p/BWlUWkZD0pr/?taken-by=gaming1empire" run the script, and it will get downloaded.

If you add a link for a gallery post it will download all pictures from that post.

# How to use
Things you need: Python3.5. Python modules: bs4, requests, pyperclip, lxml.

You can install them in cmd with "pip install [module]"

By default the downloaded content will be saved at "C:/InstaGet"

# For downloading twitch clips
You also need selenium (python module), firefox and (<a href="https://github.com/mozilla/geckodriver/releases">geckodriver</a>).
On windows, download (<a href="https://github.com/mozilla/geckodriver/releases">geckodriver</a>) and move the exe file into the python folder.

# Setup
If you do not have python 3.5 (<a href="https://www.python.org/downloads/release/python-353/">Download Here</a>). I suggest installing it at e.g C:\Python35 to easier find it in the cmd when you want to install modules, if that is going to be needed.

Then I recommend setting up <a href="https://youtu.be/5CGe3iuDfn0">this</a> to the folder you keep your scripts, to easily run them with windows RUN (windows key + R).

If you dont know how to install modules it's shown here: http://i.imgur.com/Meww3nZ.png)

# Asked Questions
Q: I changed the directories but it has stil chosen the wrong one. | A: Make sure you edit the filepath before the # as the # is a comment.

Q: I've done everything explained here and it still doesnt work. | A: Have you remembered to copy a link from instagram, youtube or twitch, before running the script?
