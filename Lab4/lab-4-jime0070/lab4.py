

def displayInstructions():
    print("Hello there")
    print("This amazing piece of python code")
    print("Converts Fahrenheit to Celsius")
    return


def FahrToCel(Temperature):
    Celsius = 5/9*(Temperature-32)
    return Celsius

def validateFloat():
    done = 0
    while done == 0:
        try:
            n = float(input("Please enter a temperature?"))  
            done = 1
    
        except ValueError:
            print("Invalid input")
    return n
        

displayInstructions()
F = validateFloat()

C = FahrToCel(F)
print("{} F = {} C".format(F,C))

'''
F = float(input("Value in Fahrenheit?>"))
C = 5 / 9 * (F - 32)
'''