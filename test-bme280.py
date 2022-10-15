from PiicoDev_BME280 import PiicoDev_BME280

sensor = PiicoDev_BME280() # initialise the sensor
zeroAlt = sensor.altitude() # take an initial altitude reading

while True:
    # Print data
    tempC, presPa, humRH = sensor.values() # read all data from the sensor
    pres_hPa = presPa / 100 # convert air pressurr Pascals -> hPa (or mbar, if you prefer)
    print(str(tempC)+" °C  " + str(pres_hPa)+" hPa  " + str(humRH)+" %RH")
    
    # Altitude demo
    print(sensor.altitude() - zeroAlt) # Print the pressure CHANGE since the script began
    sleep_ms(3000)
