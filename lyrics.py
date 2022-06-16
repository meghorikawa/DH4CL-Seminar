#this is a code to extract lyrics from a website and save it as txt file for futher processing

import requests
from bs4 import BeautifulSoup
import time
 #this is an example list of the page where the lyrics are located.
list = ["38896","300657","156598","42156","25724","156605","107228","77070"]

#cycle through the lyric pages from the website they are stored on using a loop. You will need to update the URL to the page you will use. 
for item in list:
    URL = "https://www.yoururlhere.com/song/{0}/".format(item)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    htmltitle = soup.title
    htmlresults = soup.find(id="kashi_area")
    #this removes the html tags that will still be in the extracted text
    title = htmltitle.get_text()
    lyrics = htmlresults.get_text()
    kashi = title +" "+ lyrics
    kashi = str(kashi)
    #save to txt file, you will need to update this with your own directory on your computer. 
    with open('{0}.txt'.format(title), 'w+', encoding='utf-8') as f:
        f.write(kashi)
        f.close()
        #add time delay 
        time.sleep(10)
        print("Lyrics to {0} were saved".format(title))
