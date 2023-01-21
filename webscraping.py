#import module
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import multiprocessing
import sys

#function that return data within tags
def displayTag(html,tag):
    tag_index=html.find("<"+tag+">")
    start_index=tag_index+len("<"+tag+">")
    end_index=html.find("</"+tag+">")
    tag=html[start_index:end_index]
    return tag

#function to extract code from address
def extractFile(td_data,head_url,filename):
    
    code_url=head_url+"address/"+td_data+"#code"
    print(code_url,td_data)

    try:
        code_req = Request(code_url, headers={'User-Agent': 'Mozilla/5.0'})
        #code page string
        code_page = urlopen(code_req).read()
        #decode code page
        code_html=code_page.decode('utf-8')
        code=BeautifulSoup(code_html,"lxml")
        code_text=code.select('.js-sourcecopyarea')[0].getText()
       
        #file io
        try:
            fo = open("./sol/"+td_data[0]+filename+".sol", "x")
        except:
            print('It is already exist')
        else:
            fo = open("./sol/"+td_data[0]+filename+".sol", "w", encoding='utf-8')
            fo.write(code_text)
            fo.close()
    except:
        print('error')



#scrap  data form table
def singlePage(page,head_url,filename):
    tr_tag=page.select("table tbody tr")
    for td in tr_tag:
        adress=td.select('td')[0].select('a')[0].getText()
        td_data=adress 
        # extractFile(td_data,head_url,filename)
        p = multiprocessing.Process(target=extractFile, args=(td_data,head_url,filename,))
        p.start()
        p.join()

def getresult():
    print('successful!')

def main():
    #input url
    #input_url=input("SITE NAME:")

    if sys.argv[0]=="etherscan" or sys.argv[1]=="etherscan":
        url="https://etherscan.io/contractsVerified"
        head_url="https://etherscan.io/"
        filename="-ETH"
    elif sys.argv[0]=="bscscan" or sys.argv[1]=="bscscan":
        url="https://bscscan.com/contractsVerified/"
        head_url="https://bscscan.com/"
        filename="-BSC"
    else:
        print("url error!")
        exit()

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    #webpage string
    webpage = urlopen(req).read()
    #decode webpage
    html=webpage.decode('utf-8')

    total_page=BeautifulSoup(html,"lxml")

    #display title
    title=displayTag(html,"title")
    print('Title of this site is',title)

    #total pages of table
    page=total_page.select(".font-weight-medium")[1]
    total_pages=page.getText()
    print("Totalpage is ",total_pages)

    #extracting data from page
    for page in range(int(total_pages)):
        
        page=page+1

        #url by pagination
        url_page=url+"/"+(str(page))
        
        req_pagin = Request(url_page, headers={'User-Agent': 'Mozilla/5.0'})

        #page string
        pagin_page = urlopen(req_pagin).read()

        #decode page
        pagin_html=pagin_page.decode('utf-8')

        singlepage=BeautifulSoup(pagin_html,"lxml")

        singlePage(singlepage,head_url,filename)
      
        
if __name__ == '__main__':
    main()
