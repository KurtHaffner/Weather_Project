from tkinter import *
from pygeocoder import Geocoder
import forecastio


def getForecast(latt, lngg):

    #import forecastio

    api_key = "d747bd6c3aa83c90ecc20dbbb019d5ea"
    lat = latt
    lng = lngg

    forecast = forecastio.load_forecast(api_key, lat, lng)

    #Get the daily forecast and print a nice summary.
    print()
    byday = forecast.daily()
    print(byday.summary)
    print()
    print()

    #Get the current data in a datapoint.
    current = forecast.currently()

    #Set up variables for all the data needed.
    temp = current.temperature
    feelsTemp = current.apparentTemperature
    humidity = current.humidity
    prob = current.precipProbability * 100
    dis = current.nearestStormDistance
    intensity = current.precipIntensity

    #Print the temperature and feels like temp with humidity.
    print("The current temperature is", temp, "degrees fahrenheit.")
    print("The temperature feels like", feelsTemp, "degrees fahrenheit.")
    print("The current humidity is", humidity * 100,"%.")
    print()
    print()

    #Print the hourly summary.
    byHour = forecast.hourly()
    print(byHour.summary)
    print()
    print()

    #Print the storm and rain/snow information.
    print("The probablity of precipitation right now is", prob,"%")
    print("The nearest storm is", dis, "miles away.")

    #Check to see if the probability is high enough to print storm info.
    if prob >= 50.0:
        typePrec = current.precipType
        print("The precipitation intensity is", intensity,"inches an hour.")
        print("The type of precipitation is", typePrec,".")
        print()
    

    
    return


def do_stuff():
    #Put the input into a geocoder object.
    results = Geocoder.geocode(e1.get())
    
    #Print the city and state that the user looked up.
    print("The weather for ", results[0].city, ",", results[0].state, ".")
    
    #Call the getForecast function with lat and long.
    getForecast(results[0].latitude,results[0].longitude)

#Print a description and then prompt for an address.
print("Hello!! This small program will take your address and let you know the weather.")

master = Tk()
master.title("Weather Widget")
Label(master, text="Please enter an address, city or zip code").grid(row=0)

e1 = Entry(master)
e1.grid(row=1, column=0)

Button(master, text="Get Weather", command=do_stuff).grid(row=2, column=0, sticky=W, pady=4)
Button(master, text="Quit", command=master.destroy).grid(row=2, column=1, sticky=W, pady=4)

mainloop()

#userInput = input("Enter your address, city or zip code:")


