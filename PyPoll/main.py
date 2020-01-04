#Import things
import os
import csv

candidate_khan = 0
candidate_correy = 0
candidate_li = 0
candidate_otooley = 0

total_votes = 0

results = []
winner = 0
winnerName = ''

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
            candidate_khan += 1

        elif row[2] == "Correy":
            candidate_correy += 1

        elif row[2] == "Li":
            candidate_li += 1
        
        elif row[2] == "O'Tooley":
            candidate_otooley += 1



#Create list with output
results = [
    f"Election Results",
    f"-------------------------",
    f"Total votes: {total_votes}",
    f"-------------------------",
    f"Khan: {round((100 * candidate_khan / total_votes), 3)}% ({candidate_khan})",
    f"Correy: {round((100 * candidate_correy / total_votes), 3)}% ({candidate_correy})",
    f"Li: {round((100 * candidate_li / total_votes), 3)}% ({candidate_li})",
    f"O'Tooley: {round((100 * candidate_otooley / total_votes), 3)}% ({candidate_otooley})",
    f"-------------------------",
    f"Winner: "
]

#Print results to terminal
for line in results:
    print(line)