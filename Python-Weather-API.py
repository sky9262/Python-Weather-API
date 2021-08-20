#impot all necessary module
import json
import http.client
from nested_lookup import nested_lookup
import os

#Collecting weather info.
def weather(a):
    os.system("clear")
    print("==============================================")
    print(f"    CURRENT WEATHER STATUS OF {nested_lookup('name',a)[0]}")
    print("==============================================")
    print("Current temp :",nested_lookup("temp_c",a)[0],"°C")
    print("Max temp :",nested_lookup("maxtemp_c",a)[0],"°C")
    print("Dewpoint:",nested_lookup("dewpoint_c",a)[0],"°C")
    print("Condition:",nested_lookup("text",a)[0])
    print("Feel like temp :",nested_lookup("feelslike_c",a)[0],"°C")
    print("Chance of rain :",nested_lookup("chance_of_rain",a)[0],"%")
    print("Chance of snow :",nested_lookup("chance_of_snow",a)[0],"%")
             
    input("\nPress ENTER to continue.............") 
    start()       

#Collecting geo info.
def geo_info(a):
    os.system("clear")
    print("==============================================")
    print(f"    GEO INFORMATION OF {nested_lookup('name',a)[0]}")
    print("==============================================")
    print("\nCountry :",nested_lookup("country",a)[0])   
    print("Region :",nested_lookup("region",a)[0])   
    print("Capital :",nested_lookup("name",a)[0])   
    print("Latitude :",nested_lookup("lat",a)[0])   
    print("Longitude :",nested_lookup("lon",a)[0])   
    print("Time zone :",nested_lookup("tz_id",a)[0])   
    print("Time :",(nested_lookup("localtime",a)[0]).split(" ")[1])   
    print("Date:",nested_lookup("date",a)[0])
    print("Wind speed :",nested_lookup("wind_mph",a)[0],"mph")   
    print("Wind degree :",nested_lookup("wind_degree",a)[0],"°")   
    print("Wind direction :",nested_lookup("wind_dir",a)[0])  
    print("Pressure :","↔",nested_lookup("pressure_mb",a)[0],"mb")     
    print("Humidity:",nested_lookup("humidity",a)[0],"%")
    print("Cloud Cover:",nested_lookup("cloud",a)[0],"%")
    print("Visibility:",nested_lookup("vis_km",a)[0],"km")
    print("Wind Gusts:",nested_lookup("gust_kph",a)[0],"kph")
    print("Sunrise:",nested_lookup("sunrise",a)[0])
    print("Sunset:",nested_lookup("sunset",a)[0])
    print("Moonrise:",nested_lookup("moonrise",a)[0])
    print("Moonset:",nested_lookup("moonset",a)[0])
    print("Moon phase:",nested_lookup("moon_phase",a)[0])
    if nested_lookup("is_day",a)[0] == 1:
        print("Here it's day")
    else:    
        print("Here it's night")
    input("\nPress ENTER to continue.............")
    start()

    
#Starting from here
def start():
    conn = http.client.HTTPSConnection("weatherapi-com.p.rapidapi.com")

    # Api-key and Api-host setup
    headers = {
        'x-rapidapi-key': "ff38d881cemsh2d945eede451d0cp119b37jsnea768c2f13b6",
        'x-rapidapi-host': "weatherapi-com.p.rapidapi.com"
        }

    # input Country/State/District name    
    os.system("clear")    
    print("==============================================")
    print(f"          WELCOME TO SKY INFO.")
    print("==============================================")
    location = (input("\nEnter Country/State/District name : ")).replace(" ", "%20").upper()

    # sending request
    conn.request("GET", f"/forecast.json?q={location}", headers=headers)

    # getting response
    res = conn.getresponse()

    # reading the response
    data = res.read()

    # decoading response (string)
    test_string = (data.decode("utf-8"))

    # Converting response to a dictionary (nested)
    a=(json.loads(test_string))

    if str("error" in a) == "True" :
        print("\n\nYou entered wrong name !!!!!!\n\tOR\nTry short name, like uk ....")
    else:
        os.system("clear")
        print("==============================================")
        print(f"         ABOUT, {nested_lookup('name',a)[0]}")
        print("==============================================")
        print("\n\n1. Current Weather status\n2. Geo Information")
        ask = int(input("\nEnter your choice :"))
        if ask == 1:
            weather(a)
        elif ask == 2:
            geo_info(a)
        else:
            print("You entered wrong key please try again later!!!!")
            input("\nPress ENTER to continue.............")
            start()

try:                
    start()
except:
    print("\nError!!!!\n\nPlease check your internet connection.")
