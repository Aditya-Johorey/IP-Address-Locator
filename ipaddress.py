# link for the exe file for this code: bit.ly/3IiMeFz
# Devloped by: Aditya Johorey

import json
import folium
import requests
import webbrowser
import os
from tkinter import *
location=r'C:\IP Locator'
if not os.path.exists(location):
    os.makedirs(location)
window = Tk(className=" IP Address Locator")
def getDetails(response):
    ip = response.get('ip')
    city = response.get('city')
    region = response.get('region')
    country = response.get('country')
    location = response.get('loc')
    org = response.get('org')
    timezone = response.get('timezone')
    data = {
        'ip': ip,
        'city': city,
        'region': region,
        'country': country,
        'location': location,
        'organisation': org,
        'timezone': timezone
    }

    return data

def get_ip(ip):
    response = requests.get(f'https://ipinfo.io/{ip}/json').json()
    return response

def fetch_ip(ip = ''):
    if(ip == ''):
        address = requests.get('https://api.ipify.org?format=json').json()
        return getDetails(get_ip(address.get('ip')))
    else:
        return getDetails(get_ip(ip))

def drawMap(lat, long, value, city, country):
    mapLoc = folium.Map(loaction = [lat, long],
                        zoom_start=50,
                        tiles="OpenStreetMap")
    folium.CircleMarker(location=[lat, long],
                        radius= 50, popup = 'FRI').add_to(mapLoc)
    mapLoc.fit_bounds(mapLoc.get_bounds(), padding = (40,40))
    popup = folium.Popup(value, min_width = 100, max_width=300)
    folium.Marker([lat, long],
                  popup= popup,
                  radius=1, weight=1, border_width=10,
                  icon = folium.Icon(color='red', icon = 'map-marker', prefix = 'fa')).add_to(mapLoc)
    mapLoc.save("C:\IP Locator\mapLoc.html")
    warning.config(text = f"IP Address Located Sucessfully in {city}, {country}")
    #filename = "file:///C:\IP Locator\mapLoc.html"
    webbrowser.open_new_tab("C:\IP Locator\mapLoc.html")


def start():
    warning.config(text = '')
    ip = str(ipaddress.get())
    try:
        data = fetch_ip(ip)
    except requests.exceptions.ConnectionError:
        warning.config(text = "No Internet Connection! Please Connect to the internet")
        return
    try:
        print(data)
        lat, long = data['location'].split(',')
        drawMap(lat, long, f'<h4><b>ip</b>: {data["ip"]}<br/><b>City:</b> {data["city"]}<br/><b>State:</b> {data["region"]}<br/><b>Country:</b> {data["country"]}<br/><b>Service:</b> {data["organisation"]}<br/><b>Time Zone:</b> {data["timezone"]}</h4>', data["city"],data["country"])
    except AttributeError:
        warning.config(text = "Invalid IP Address! Please Try Again")
    except UnboundLocalError:
        pass

txt = Label(window, text = "Enter an IP Address : ",font=("Arial", 20))
txt.grid(row = 0, column = 0,
          padx = (10, 5), pady = (10,5))
ipaddress = StringVar()
ipaddress.set('')
entry = Entry(window, textvariable = ipaddress,font=("Arial", 20))
entry.grid(row = 0, column = 1,
           padx = (5, 10), pady = (10, 5))
submit = Button(window, text = "Submit", command = start, font=("Arial", 15))
submit.grid(row = 1, column = 0, columnspan = 2,
            pady = (10, 10))
warning = Label(window, text = '',font=("Arial", 15))
warning.grid(row = 2, column = 0, columnspan = 2,
             pady = (10, 10))
# submit.grid_rowconfigure(1, weight=1)
# submit.grid_columnconfigure(1, weight=1)
window.mainloop()
