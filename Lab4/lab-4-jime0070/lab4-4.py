# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""This example prints the status of the slide switch. Try moving the switch back and forth to see
what's printed to the serial console!"""
import time
from adafruit_circuitplayground import cp
#from lab4-1 import FahrToCel

def displayInstructions():
    print("Hello there")
    print("This amazing piece of python code")
    print("Converts Fahrenheit to Celsius")
    return

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
    temFahrenheit = (temCelsius * 9 / 5) + 32
    return temCelsius

while True:
    print("Slide switch:", cp.switch)
    time.sleep(0.2)
    #print("Temperature C:", cp.temperature)
    #print("Temperature F:", cp.temperature * 1.8 + 32)
        
    if cp.switch == False:
        C = FahrToCel(cp.temperature)
        print("{} Celsius".format(C))
    elif  cp.switch == True:
        #print('In True. converts the temperature to Fahrenheit.')
        F = CelToFahr(cp.temperature)
        print("{} Fahrenheit ".format(F))
    
        
    

    
    
    

        
