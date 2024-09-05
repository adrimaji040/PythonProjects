
def displayInstructions():
    print("Hello there")
    print("This amazing piece of python code")
    print("Converts Fahrenheit to Celsius")
    return

# Fahrenheit to Celsius
def FahrToCel(Temperature):
    Celsius = 5 / 9 * (Temperature - 32)
    return Celsius

# Celsius To Fahrenheit
def CelToFahr(temCelsius):
    temFahrenheit = (temCelsius * 9 / 5) + 32
    return temFahrenheit

#  returns the smallest of the two inputs.
def min(a,b):
    while True:
        try:
            if a < b:
                return a
            elif b < a:
                return b
            elif a == b:
                print("The number are the same. Try again.")
                break
        except ValueError:
            print("Some error")  

# Volume of Sphere
def VolumeOfSphere(radiusNumber):
    R = radiusNumber
    pi = 3.1415926535897931
    V = 4 / 3  * pi * R**3
    return V          


 # Valid a number is Float            
def validateFloat():
    done = 0
    while done == 0:
        try:
            n = float(input("Please enter a temperature?: "))  
            done = 1
    
        except ValueError:
            print("Invalid input")
    return n


 #Valide float radius       
def validateFloatR():
    done = 0
    while done == 0:
        try:
            n = float(input("Please enter Radius: "))  
            done = 1
    
        except ValueError:
            print("Invalid input")
    return n

# Valid a number is Int
def validNumber():
    while True:
        n = input("Enter a Int number:")
        try:    
            n = int(n)
            break  
        except ValueError:
            print("Wrong number. Type int number")
    return n
    
# Ask for Fanrenheit number 
displayInstructions()
F = validateFloat()
C = FahrToCel(F)
print("{} F = {} C".format(F,C))


# Ask for Celsius Number
C = validateFloat()
F = CelToFahr(C)
print("{} C = {} F".format(C,F))


# Ask for two number to calclulade the min  
a = validNumber()
print("The number a is {}".format(a))
b = validNumber()
print("The number a is {}".format(b))

result = min(a,b)
print("{} is the min number between {} and {}".format(result,a,b))

#Ask the radius of Shere
r = validateFloatR()
print(VolumeOfSphere(r))


