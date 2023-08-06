from bs4 import BeautifulSoup
import requests
class score():
    def __init__(self):

        url = "https://www.espncricinfo.com/live-cricket-score"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        #print(soup.prettify())
        print('________________________________')

        match_descrition = soup.select(".description")
        print(match_descrition[1].text)

        print('________________________________')

        obj1 = soup.select(".teams")
        print(obj1[0].text)

        print('________________________________')

        status = soup.select('.status-text')
        print(status[0].text)

        print('________________________________')
