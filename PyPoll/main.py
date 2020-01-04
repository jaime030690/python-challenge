#Import things
import os
import csv

totalVotes = 0

candidates = {
    "Correy": [0, 0],
    "Khan": [0, 0],
    "Li": [0, 0],
    "O'Tooley": [0, 0]
}

sortedCandidates = {}
results = []

filename = os.path.join("Resources", "election_data.csv")

with open(filename, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Skip header
    next(csvfile)

    for row in csvreader:

        totalVotes += 1

        if row[2] == "Correy":
            candidates["Correy"][0] += 1

        elif row[2] == "Khan":
            candidates["Khan"][0] += 1

        elif row[2] == "Li":
            candidates["Li"][0] += 1
        
        elif row[2] == "O'Tooley":
            candidates["O'Tooley"][0] += 1

for key in candidates:
    candidates[key][1] = 100 * candidates[key][0] / totalVotes

sortedCandidates = sorted(candidates.items(), key = lambda kv:(kv[1], kv[0]), reverse = True)

results = [
    f"Election Results",
    f"-------------------------",
    f"Total votes: {totalVotes}",
    f"------------------------",
]

print(f'Total votes: {totalVotes}')
print(f'Results: {sortedCandidates}')