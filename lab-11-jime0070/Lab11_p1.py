import json


jsonFile = 'Red_Light_Camera_Violations_2023.geojson'

#Open and read a json file

with open(jsonFile,'r') as file:

    #Load JSON data from the file
    data = json.load(file)
    listIntersections = [el['properties']['INTERSECTION'] for el in data['features']]

  

    #Using list and string methods, sets as well as for loops or list Comprehension, convert listIntersections to a sorted list of
    listIntersections.sort()

    #print(listIntersections)

#Note that lstStreetNames still include entries like 'Carling / glebe'.
#Write some python statements to extract these entries intro a list called lstToSanitize
#(see lstToSanitize content below)
    lstStreetNames = []
    lstStreetNames = [st.split('@')[1].strip() for st in listIntersections]
    lstStreetNames.sort()
    #print('lstStreetNames {}'.format(lstStreetNames))

    lstToSanitize = [sani for sani in lstStreetNames if '/' in sani]
    print('lstToSanitize {}:'.format(lstToSanitize))


#Using sets and the set method symmetric_difference, remove the elements of lstToSanitize from lstStreetNames. Save the result into a new sorted list lst1
#(see lst1 below)
    lst1 = []    

    #symmetric_difference only work with set.
    setSteetNames = set(lstStreetNames)
    setSanitize = set(lstToSanitize)
    lst1 = setSteetNames.symmetric_difference(setSanitize) 
    list(lst1).sort()
    lst2 = list(lst1) #created lst2 to casting lst1 set to list
    
    #print(lst1)

#Extract street names from the list lstToSanitize, create a list of streets out of if 
#then add each one to lst1.
#Sort the resulting list making sure each element is stored only once
#(See listOfStreets below)    

#print(lstToSanitize)
newStreets = []
for i in  lstToSanitize:
    lstStreet = [st.strip() for st in i.split('/')]
    newStreets.extend(lstStreet)

#print(newStreets)
#add items to the end of the lst1... using lst2 list instead to lst1 set for to can change it

for i in newStreets:
   lst2.append(i)
   lst2.sort()
#print(lst2)

#Remove duplicate. created dictionary which cannot have duplicates keys
listOfStreets  = list(dict.fromkeys(lst2))

print('listOfStreets {}: '.format(listOfStreets))






    
    








    





