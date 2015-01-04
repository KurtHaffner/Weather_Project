def getForecast(latt, lngg):

    import forecastio

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
    print("The probablity of precipitation is", prob,"%")
    print("The nearest storm is", dis, "miles away.")

    #Check to see if the probability is high enough to print storm info.
    if prob >= 50.0:
        typePrec = current.precipType
        print("The precipitation intensity is", intensity,"inches an hour.")
        print("The type of precipitation is", typePrec,".")
        print()
    

    
    return
