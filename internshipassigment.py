from bs4 import BeautifulSoup
from selenium import webdriver
import time,selenium,json

mainurls=["https://www.instructables.com/Building-a-Self-Driving-Boat-ArduPilot-Rover/","https://www.instructables.com/Hydraulic-Craft-Stick-Box/","https://www.instructables.com/How-to-Make-a-Self-Watering-Plant-Stand/"]
data=[]
for url in mainurls:
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver= webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(5)
    sitesoup= BeautifulSoup(driver.page_source,"html.parser")
    image_url=sitesoup.find("a",{"class":"gallery-link"}).get('href')
    youtube_url=sitesoup.find("div",{"class":"videoset-item"}).find('iframe').get('src')
    header_title=sitesoup.find("h1",{"class":"header-title"}).getText().strip()
    view_count=sitesoup.find("p",{"class":"view-count"}).getText()
    favorite_count=sitesoup.find("p",{"class":"favorite-count"}).getText()
    comments=sitesoup.find("p",{"class":"comment-count"})
    if(comments):
        comment_count=comments.getText()
    else:
        comment_count="Not Found"
    steps=sitesoup.findAll("section",{"class":"step"})
    stepslist=[]
    for i in steps[1:]:
        stepslist.append(i.find("h2").getText().strip())

    supplieslist=[]
    if(sitesoup.find("h3",{"class":"supplies-heading"})):
        if(sitesoup.find("div",{"class":"step-body"}).find("ul")):
            supplies=sitesoup.find("div",{"class":"step-body"}).find("ul").findAll("li")
            for supply in supplies:
                supplieslist.append(supply.getText().strip())
        else:
            supplies=sitesoup.find("div",{"class":"step-body"}).findAll("p")
            for supply in supplies[2:]:
                supplieslist.append(supply.getText().strip())
    else:
        supplieslist.append("No Supplies found")

    data.append({'scraped_url':url, 'header_title':header_title,'youtube_url': youtube_url,'image_url':image_url , 'view_count':view_count,
    'favorite_count':favorite_count,'comment_count':comment_count,'steps':stepslist, 'supplies':supplieslist
    })
    driver.close()

jsondump=json.dumps(data, ensure_ascii=False, indent=4)
with open("scrapeddata.json", "w") as outfile: 
    outfile.write(jsondump) 