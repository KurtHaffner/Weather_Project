from tkinter import *
from pygeocoder import Geocoder
import forecastio


def getForecast(latt, lngg, results):

    #Set up the box that will hold all the results.
    result = Tk()
    result.title("Weather Results")
    

    api_key = "d747bd6c3aa83c90ecc20dbbb019d5ea"
    lat = latt
    lng = lngg

    forecast = forecastio.load_forecast(api_key, lat, lng)

    #Get the daily forecast and print a nice summary.
    byday = forecast.daily()

    #Add labels with the location and summary.
    something = "The weather for {0}, {1}.".format(results[0].city,results[0].state)
    Label(result, text=something).grid(row=0)
    Label(result, text="").grid(row=1)
    Label(result, text=byday.summary).grid(row=2)

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
    something = "The current temperature is {0} degrees fahrenheit.".format(temp)
    something1 = "The temperature feels like {0} degrees fahrenheit.".format(feelsTemp)
    something2 = "The current humidity is {0}%.".format(humidity*100)

    #Add labels for temperature and feels like temp with humidity.
    Label(result, text="").grid(row=3)
    Label(result, text=something).grid(row=4)
    Label(result, text=something1).grid(row=5)
    Label(result, text=something2).grid(row=6)

    #Print the hourly summary.
    byHour = forecast.hourly()

    #Add hourly summary.
    Label(result, text="").grid(row=7)
    Label(result, text=byHour.summary).grid(row=8)

    #Print the storm and rain/snow information.
    something = "The probablity of precipitation right now is {0}%".format(prob)
    something1 = "The nearest storm is {0} miles away.".format(dis)

    #Add the storm and rain/snow info.
    Label(result, text="").grid(row=9)
    Label(result, text=something).grid(row=10)
    Label(result, text=something1).grid(row=11)

    #Check to see if the probability is high enough to print storm info.
    if prob >= 50.0:
        typePrec = current.precipType
        something = "The precipitation intensity is {0} inches an hour.".format(intensity)
        something1 = "The type of precipitation is {0}.".format(typePrec)

        #Add to the window.
        Label(result, text="").grid(row=12)
        Label(result, text=something).grid(row=13)
        Label(result, text=something1).grid(row=14)
    

    
    return


def do_stuff():
    #Put the input into a geocoder object.
    results = Geocoder.geocode(e1.get())
    
    #Call the getForecast function with lat and long.
    getForecast(results[0].latitude,results[0].longitude, results)

    #End the GUI.
    master.destroy()

#Set up the prompt for finding the lat and long.
master = Tk()
master.title("Weather Widget")
Label(master, text="Please enter an address, city or zip code").grid(row=0)

e1 = Entry(master)
e1.grid(row=1, column=0)

Button(master, text="Get Weather", command=do_stuff).grid(row=2, column=0, sticky=W, pady=4)
Button(master, text="Quit", command=master.destroy).grid(row=2, column=1, sticky=W, pady=4)

mainloop()


