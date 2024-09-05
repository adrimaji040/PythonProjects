# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""This example turns on the little red LED when button A is pressed."""
import time
from adafruit_circuitplayground import cp


# Fahrenheit to Celsius
def FahrToCel(Temperature):
    Celsius = 5 / 9 * (Temperature - 32)
    return Celsius

#Validation Float
def validateFloat():
    done = 0
    while done == 0:
        try:
            n = float(input("Please enter a temperature?: "))  
            done = 1
    
        except ValueError:
            print("Invalid input")
    return n

# Celsius To Fahrenheit
def CelToFahr(temCelsius):
    temFahrenheit = (temCelsius * 9/5) + 32
    return temFahrenheit

while True:
    print("Slide switch:", cp.switch)
    time.sleep(0.4)
    
    if cp.switch == False and cp.button_a:
        print("Temperature Celsius:", cp.temperature)
    elif cp.switch == True and cp.button_a:
        F = CelToFahr(cp.temperature)
        print("{} Temperature Fahrenheit ".format(F)) 
        
        
    
  
           
           
