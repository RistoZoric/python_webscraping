# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 21:56:43 2022

@author: Admin
"""

#import module
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
from geopy.geocoders import Nominatim

#import multiprocessing
import sys
import psycopg2


        
        
def main():
    
    site_url="http://localhost/abu/test/jump-start-service-aldgate-london-EC3N-UK%20(1).html"

    req=Request(site_url,headers={'User-Agent': 'Mozilla/5.0'})
    
    #webpage string
    webpage=urlopen(req).read()
    
    #decode webpage
    html=webpage.decode('utf-8')
    #print(html)
    total_page=BeautifulSoup(html,"lxml")
    #print(total_page)
    
    url="http://localhost/abu/areas.html"
    req1=Request(url,headers={'User-Agent': 'Mozilla/5.0'})
    page=urlopen(req1).read()
    page=page.decode('utf-8')
    html1=BeautifulSoup(page,"lxml")
    array=html1.select("#areas .tab-content li")
    
    for item in array:
        default_url="C:/xampp/htdocs/abu"
        real_name=item.text
        print(real_name)
        post_code=item.find("a")["href"].split("-")[len(item.find("a")["href"].split("-"))-2]
        page_url=item.find("a")["href"]
        map_query=item.text.replace("  ","+").replace(" ","")
        print('https://www.google.com/maps?&q=london+'+map_query+"&hl=es&z=12&amp;output=embed")
        content=html.replace("Aldersgate",real_name).replace("EC1A",post_code).replace("Nothing",'https://www.google.com/maps?&q=london+'+map_query+"&hl=es&z=12&amp;output=embed")

        try:   
            print(default_url+page_url.replace(".",""))
            fo = open(default_url+page_url.replace(".","").replace("html",".html"), "w", encoding='utf-8')
            fo.write(content)
            fo.close()
        except:
            print("File io error")   
    #print(array)
    #display site title
    

        
if __name__ == '__main__':
    main()
