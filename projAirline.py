#Jaymond Lei
#CSC110
#Airline Project 
#Due 5/1/23

#---------------------------------------------------------------------------

#File handling. This function (or openfile/getdata functions) will be
#reflective of previous coding assignments that read a file. I will attempt
#to transfer my code over to this new project, which will then read
#flights.csv. The file contains 5 different things to split: The airline
#(string), flight number (int), departure time (an int converted to a string
#), arrival time (int converted to string), and price (float). This
#has exception handling in case of a bad input. This will return the
#5 types of data.

def getData():
    #Boolean for if a file name is acceptable/valid
    valid = False
    #While valid is false,
    while valid == False:
        #Input file name
        fname = input("Please enter the name of the data file: ")
        #Try to open the file using the name given
        try:
            dataFile = open(fname, 'r')
            #If the name is valid, set valid to true to exit loop
            valid = True
        except IOError:
            #If the name is not valid, exception occurs and prints 
            print("Invalid filename, try again ... ")
            
    #This is the imported getData function, modified for the new data
            
    #Opens file
    infile = dataFile
    #Reads Lines
    line = infile.readline()

    #Lists for all different data
    
    airlines = []
    flightNums = []
    depTimes = []
    arrTimes = []
    prices = []

    #Splits lines and adds to lists
    
    while line != "":
        #strips the \n
        line = line.strip()
        #splits for all different data
        airline, flightNum, depTime, arrTime, price = line.split(',')
        #adds the indexed airline to list
        airlines = airlines + [airline]
        flightNums = flightNums + [flightNum]
        depTimes = depTimes + [depTime]
        arrTimes = arrTimes + [arrTime]
        prices = prices + [price]
        line = infile.readline()

    #closes file

    infile.close()

    #Returns lists
            
    return airlines, flightNums, depTimes, arrTimes, prices

#Time Conversion function. This function converts the time into a numerical
#integer for most operations.

def timeConvert(depTimes, arrTimes):
    depInt = []
    arrInt = []
    
    for t in depTimes:
        depInt[t] = int(depTimes[t])

    for y in arrTimes:
        arrInt[y] = int(arrTimes[t])
        
    return depInt, arrInt

#Menu Function. As per suggestions, this function would print out the
#menu items instead of printing everything in the main print function.

def menu():
    print("Please choose one of the following options:")
    print("1 -- Find flight information by airline and flight number")
    print("2 -- Find flights shorter than a specified duration")
    print("3 -- Find the cheapest flight by a given airline")
    print("4 -- Find flight departing after a specified time")
    print("5 -- Fine the average price of all flights")
    print("6 -- Write a file with flights sorted by departure time")
    print("Quit")
    goodChoice = False
    while goodChoice == False:
        try:
            choice = int(input("Choice ==> "))
            goodChoice == True
        except IOError:
            print("Entry must be a number")
        except choice < 0 or choice > 7:
            print("Number must be between 1 and 7")
    return choice
        

#Search function. This allows the user to input their desired airline
#and flight number and returns information about the flight (the other 3
#types of data from the file). There should be exception handling.
#It takes all data from getData.

def search(airline, flightNum, depInt, arrInt, price):
    return flightInfo

#Shorter Flights function. This function asks the user to specify a
#max flight duration and returns flight info for flights that are less than
#or equal to the max duration. This is presumably from shortest to longest.
#Duration = arrival - departure. It will return a list of flights.
#It will take all data.

def shorterFlights(airline, flightNum, depInt, arrInt, price):
    return shorterList

#Cheapest Flights function. This function asks the user for an airline
#and returns the cheapest flight from that airline. Exception handling req.
#It takes all data.

def cheapestFlights(airline, flightNum, depInt, arrInt, price):
    return cheapest

#Timed Flight function. This function asks the user for a time in the
#format HH:MM. The clock is 24 hours. Excemption handling req. It returns
#all flights that depart after the time (presumably before 24:00).

def timedFlight(airline, flightNum, depInt, arrInt, price):
    return timedList

#Average Price function. This function adds all prices together and
#returns the average price of all flights. The algorithm is basically
#adding all prices together and dividing it by the total number of flights.
#Only prices are needed. 

def averagePrice(price):
    return average

#8. Sort Flights function. This function sorts out all flights by departure
#time and writes the resulting lists time-sorted-flights.csv. A list of
#indexes for the other data correlates with the order of departure time.
#A selection sort will be chosen for this step, and it returns the file.

def sortFlights(airline, flightNum, depInt, arrInt, price):
    return sortFlightList

#Print function. This function prints results and such from other
#functions based on their returned value. It returns nothing.

def print(flightInfo, shorterList, cheapest, timedList, average, outFile):
    
    return

#Main function. This function calls all other functions by setting
#their returned values to equal the function. This function also tests
#the conditional in which the desired choice is given, returning
#the correct function to display. It has no parameters and returns nothing.

def main():
    airlines, flightNums, depTimes, arrTimes, prices = getData()
    depInt, arrInt = timeConvert(depTimes, arrTimes)
    choice == menu()
    flightInfo = search(airline, flightNum, depInt, arrInt, price)
    shorterList = shorterFlights(airline, flightNum, depInt, arrInt, price)
    cheapest = cheapestFlights(airline, flightNum, depInt, arrInt, price)
    timedList = timedFlight(airline, flightNum, depInt, arrInt, price)
    average = averagePrice(price)
    outFile = sortFlights(airline, flightNum, depInt, arrInt, price)
    print(flightInfo, shorterList, cheapest, timedList, average, outFile)
    

