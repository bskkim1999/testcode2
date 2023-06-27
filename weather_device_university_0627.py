from urllib import request
from bs4 import BeautifulSoup
import time
import re

while True:

    target = request.urlopen("https://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=2623071000")
    soup = BeautifulSoup(target, 'xml') #data 불러옴

    #print(soup)

    weather = list(soup.select("wfKor"))
    low = list(soup.select("tmn"))
    high = list(soup.select("tmx"))

    weather_list = [item1.text for item1 in weather]
    low_list = [float(re.findall(r"-?\d+\.\d+", str(item))[0]) for item in low]
    high_list = [float(re.findall(r"-?\d+\.\d+", str(item))[0]) for item in high]
    print(weather_list)
    print(low_list)

    print(high_list)


    time.sleep(10)




