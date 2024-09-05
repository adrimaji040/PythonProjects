import json
import Lab11_p1


jsonFile = 'Red_Light_Camera_Violations_2023.geojson'
with open(jsonFile,'r') as file:

    #Load JSON data from the file
     data = json.load(file)
     listIntersections =list(set([feature['properties']['INTERSECTION'].split('@')[0].strip() for feature in data['features']]))
     print("listIntersections second part {}: ".format(listIntersections))   

def getStreetName():
    while True:
        street = input('Name of the street (x to exit)?')
        streetName = street.capitalize()
        if (streetName == 'X'):
            print('Goodbye')
            return False
        elif streetName.upper() in Lab11_p1.listOfStreets:
             redLightViolations(streetName.upper())          
            #print("violations {}".format(violations)) # working here
        else:
            print('The street not exist')
            
            

def redLightViolations(stName):
    stName = stName.strip().upper()  # Prepare the street name
    if stName not in listIntersections:
        print("Street not found")
        return
    print(f"All Red light violations on {stName} street/road:")
    for feature in data['features']:
        intersection = feature['properties']['INTERSECTION'].split('@')[0].strip()
        if intersection == stName:
            for month in ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER','TOTAL_VIOLATIONS']:
                #if feature['properties'][month] != "TBD":
                    filterViolations = print(f"{month}: {feature['properties'][month]}")

    
    return filterViolations 
    
           
           
#main program
while True:
    streetName = getStreetName()
    if streetName == False:
        break
    else:
        print(streetName)
    
  
        
        
        
