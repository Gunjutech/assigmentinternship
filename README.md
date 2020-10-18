# assigmentinternship

internshipassigment.py file contains the python script for scraping the sites mentioned in the assignment pdf.
scrapeddata.json contains the json output for the scraped data.

Since some of the data are dynamic, I have used selenium so that the data can be scraped from javascript code also.
After the page is loaded using selenium, I have used BeautifulSoup library to convert into html data. 

To run the code, need to:
1. install webdriver for chrome which can be done from this site: https://chromedriver.chromium.org/downloads. After running the downloaded file, paste the chrome webdriver in scrpits folder of python folder.
2. pip install selenium
3. pip install beautifulsoup4

The code runs through the 3 websites and stores the scraped data in scrapeddata.json
