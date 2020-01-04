#Import os module for the path and csv module to read file.
import os
import csv

#Declare variables
monthCount = 0
netTotal = 0
isFirstRow = True
firstValue = 0
lastValue = 0
prevMonth = 0
monthChange = 0
averageChange = 0
increaseNum = 0
decreaseNum = 0
increaseDate = ''
decreaseDate = ''
results = []

#Create fileName variable
fileName = os.path.join("Resources", "budget_data.csv")

#Calculate data on csv file
with open(fileName, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Skip header
    next(csvfile)

    #Iterate through rows in csv file
    for row in csvreader:

        #Store value for the first and last rows
        if isFirstRow:
            firstValue = int(row[1])
            isFirstRow = False

        #Record values for rows after first row
        else:
            lastValue = int(row[1])
            monthChange = lastValue - prevMonth

        #Update increases and decrease values
        if monthChange > increaseNum:
            increaseNum = monthChange
            increaseDate = row[0]
        
        elif monthChange < decreaseNum:
            decreaseNum = monthChange
            decreaseDate = row[0]

        #Update totalMonth, netTotal, and prevMonth
        monthCount += 1
        netTotal += int(row[1])
        prevMonth = int(row[1])

    #Calculate average change
    averageChange = (lastValue - firstValue) / (monthCount - 1)

#Store results on string list
results = [
    f'Financial Analysis',
    f'----------------------------',
    f'Total Months: {monthCount}',
    f'Total: ${netTotal}',
    f'Average Change: ${round(averageChange, 2)}',
    f'Greatest Increase in Profits: {increaseDate} (${increaseNum})',
    f'Greatest Decrease in Profits: {decreaseDate} (${decreaseNum})'
]

#Print results to terminal
for line in results:
    print(line)

#Create text file
writeFile = open('Output/results.txt', 'w')

#Write results to text file and close when complete
for line in results:
    writeFile.write(line + '\n')
writeFile.close()