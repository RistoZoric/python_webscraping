#import module
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
#import multiprocessing
import sys
import psycopg2

#function that return data within tags
def displayTitlte(html,tag):
    tag_index=html.find("<"+tag+">")
    start_index=tag_index+len("<"+tag+">")
    end_index=html.find("</"+tag+">")
    tag=html[start_index:end_index]
    return tag

#function that return data from tag
def displayType(html,value_type,value):
    content=""
    if value_type=="tag":    
        tag_array=html.find_all(value)
        for item in tag_array:
            content+=str(item)  
        return content
    elif value_type=="class":
        tag_array=html.select("."+value)
     
        for item in tag_array:
            content+=str(item)
        return content
    elif value_type=="id":
         tag_str=html.select("#"+value)
         return str(tag_str)
    else:
        tag_array=html.find_all(value_type)
        
def doQuery(conn,table,site_url,value_type,value,data):
    cur=conn.cursor()
    query="INSERT INTO "+table+" (url, type, value, data) VALUES ("+"'"+site_url+"',"+"'"+value_type+"',"+"'"+value+"',"+"'"+data+"')"

    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()
        
        
def main():
    
    site_url="https://www.frisco.pl/c,2404/cat,spozywcze/stn,searchResults"


    #site_url=sys.argv[1]
    #value_type=sys.argv[2]
    #value=sys.argv[3]

    req=Request(site_url,headers={'User-Agent': 'Mozilla/5.0'})
    
    #webpage string
    webpage=urlopen(req).read()
    
    #decode webpage
    html=webpage.decode('utf-8')
    
    total_page=BeautifulSoup(html,"lxml")

    content=total_page.find_all("href")
    print(total_page)

    #connection of server
    hostname = 'localhost'
    username = 'postgres'
    password = '123'
    port="5432"
    database = 'scraping'
    myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
    tablename='scrap.scrap'
    
    #insert data into table
    # doQuery(myConnection,tablename,site_url,value_type,value,result_str)
    print("This is saved successfully!")
        
if __name__ == '__main__':
    main()
