#Import things
import os
import csv

totalVotes = 0
candidates = {
    "Khan": [0, 0],
    "Correy": [0, 0],
    "Li": [0, 0],
    "O'Tooley": [0, 0]
}
results = []

#Get file to read
filename = os.path.join("Resources", "election_data.csv")

#Start reading file
with open(filename, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Skip header
    next(csvfile)

    for row in csvreader:

        totalVotes += 1

        if row[2] == "Khan":
            candidates["Khan"][0] += 1

        elif row[2] == "Correy":
            candidates["Correy"][0] += 1

        elif row[2] == "Li":
            candidates["Li"][0] += 1
        
        elif row[2] == "O'Tooley":
            candidates["O'Tooley"][0] += 1

#Calculate percentages
for key in candidates:
    candidates[key][1] = 100 * candidates[key][0] / totalVotes

#Create list with output
results = [
    f"Election Results",
    f"-------------------------",
    f"Total votes: {totalVotes}",
    f"-------------------------",
    f"Khan: {round(candidates["Khan"][1], 3)}% ({candidates["Khan"][0]})",
    f"Correy: {round(candidates["Correy"][1], 3)}% ({candidates["Correy"][0]})",
    f"Li: {round(candidates["Li"][1], 3)}% ({candidates["Li"][0]})",
    f"O'Tooley: {round(candidates["O'Tooley"][1], 3)}% ({candidates["O'Tooley"][0]})"
]

#Print results
for item in results:
    print(results[item])