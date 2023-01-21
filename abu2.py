#import module
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
from geopy.geocoders import Nominatim

#import multiprocessing
import sys


       
        
def main():
    fo=open("sample.txt","r+")
    str=fo.read()

    x=str.split("\n")
    length=len(x)
    
    url="file:///C:/Users/Marijan/Downloads/1/Colorlib%20_%20Free%20Bootstrap%20Website%20Template_files/mobile-tyre-fitting-areaname.html"
    
    req1=Request(url,headers={'User-Agent': 'Mozilla/5.0'})
    page=urlopen(req1).read()
    page=page.decode('utf-8')
    html1=BeautifulSoup(page,"lxml")
    array=html1.select(".flex-item li")
    print(array)
    geolocator = Nominatim(user_agent="geoapiExercises")
    for i in array:

        location = geolocator.geocode(i.text, addressdetails=True ,timeout=None)
        post_code="nothing"
        url_name=i.text.replace(" ",'-')
        href=i.find('a')['href'].replace('./','')
        print(i.text,"--------------------------",href)
        try:
            post_code=location.raw['address']['postcode']
            if post_code.index(" ")>0:
                post_code=post_code.split(" ")[0]

            
          
       
        except:
            print("error")
        
         
        map_query=i.text.replace(" ","+").replace(" ","")
        print(map_query)
        page1=page.replace("Areaname",i.text).replace('nothing',map_query)    
        default_url="C:/Users/Marijan/Downloads/1/Colorlib _ Free Bootstrap Website Template_files/"+href
        fo = open(default_url, "w", encoding='utf-8')
        fo.write(page1)
        fo.close()
        print(page1)
        
if __name__ == '__main__':
    main()
