#Import things
import os
import csv

#Initialize candidate totals with zero
khan = 0
correy = 0
li = 0
otooley = 0
total_votes = 0

#List to string with results
results = []

#Get file to read
filename = os.path.join("Resources", "election_data.csv")

#Start reading file
with open(filename, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Skip header
    next(csvfile)

    for row in csvreader:

        total_votes += 1

        if row[2] == "Khan":
            khan += 1

        elif row[2] == "Correy":
            correy += 1

        elif row[2] == "Li":
            li += 1
        
        elif row[2] == "O'Tooley":
            otooley += 1

#Check for winner
if khan > correy and khan > li and khan > otooley:
    winner = "Khan"

elif correy > khan and correy > li and correy > otooley:
    winner = "Correy"

elif li > khan and li > correy and li > otooley:
    winner = "Li"

else:
    winner = "O'Tooley"

#Create list with output
results = [
    f"Election Results",
    f"-------------------------",
    f"Total votes: {total_votes}",
    f"-------------------------",
    f"Khan: {round((100 * khan / total_votes), 1)}% ({khan})",
    f"Correy: {round((100 * correy / total_votes), 1)}% ({correy})",
    f"Li: {round((100 * li / total_votes), 1)}% ({li})",
    f"O'Tooley: {round((100 * otooley / total_votes), 1)}% ({otooley})",
    f"-------------------------",
    f"Winner: {winner}"
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