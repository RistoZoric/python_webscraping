from geopy.geocoders import Nominatim

fo=open("sample.txt","r+")
str=fo.read()

x=str.split("\n")
length=len(x)
content=""
geolocator = Nominatim(user_agent="geoapiExercises")

for i in range(0, length):
    x[i]=x[i].strip()
    location = geolocator.geocode(x[i], addressdetails=True ,timeout=None)
    post_code="nothing"
    try:
        post_code=location.raw['address']['postcode']
        if post_code.index(" ")>0:
                post_code=post_code.split(" ")[0]
    except:
        #print("error")
        post_code="nothing"

    
    content='<li><a href="./jump-start-service-'+x[i].replace(" ","-")+'-london-'+post_code+'-UK.html">'+x[i]+'</a></li>'

    print(content)
