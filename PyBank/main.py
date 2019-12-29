#Import os module for the path and csv module to read file.
import os
import csv

totalMonth = 0
netTotal = 0
isFirstRow = True
firstValue = 0
lastValue = 0
prevMonth = 0
monthChange = 0
averageChange = 0
greatestIncreaseNum = 0
greatestDecreaseNum = 0
greatestIncreaseDate = ''
greatestDecreaseDate = ''

fileName = os.path.join("Resources", "budget_data.csv")

with open(fileName, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Skip header
    next(csvfile)

    #Iterate through rows in csv file
    for row in csvreader:

        #Stores value for the first and last rows
        if isFirstRow:
            firstValue = int(row[1])
            isFirstRow = False

        else:
            lastValue = int(row[1])
            monthChange = lastValue - prevMonth

        #Update increases and decrease values
        if monthChange > greatestIncreaseNum:
            greatestIncreaseNum = monthChange
            greatestIncreaseDate = row[0]
        
        elif monthChange < greatestDecreaseNum:
            greatestDecreaseNum = monthChange
            greatestDecreaseDate = row[0]

        #Update totalMonth, netTotal, and prevMonth
        totalMonth += 1
        netTotal += int(row[1])
        prevMonth = int(row[1])

    #Calculate average change
    averageChange = (lastValue - firstValue) / (totalMonth - 1)

    #Print out results
    print (f'Financial Analysis')
    print (f'----------------------------')
    print (f'Total Months: {totalMonth}')
    print (f'Total: ${netTotal}')
    print (f'Average Change: ${round(averageChange, 2)}')
    print (f'Greatest Increase in Profits: {greatestIncreaseDate} (${greatestIncreaseNum})')
    print (f'Greatest Decrease in Profits: {greatestDecreaseDate} (${greatestDecreaseNum})')