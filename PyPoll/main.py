import os
import csv
total_votes = 0
candidate_votes = {}
winner = ""
winnerVotes = 0
output = ""


election_csv = os.path.join("Resources", "election_data.csv")
with open(election_csv, "r") as file:
    csvreader = csv.reader(file)
    next(csvreader,None)
    for row in csvreader:
        total_votes=total_votes+1
        if candidate_votes.get(row[2]):
            candidate_votes[row[2]] = 1+int(candidate_votes.get(row[2]))
        else:
            candidate_votes[row[2]] = 1
    
output = output+"\n"
output = output+"Election Results"
output = output+"\n"
output = output+"------------------------------"
output = output+"\n"
output = output+"Total Votes: " +str(total_votes)
output = output+"\n"
output = output+"-------------------------------"


for candidate in candidate_votes.keys():
    output = output+"\n"
    output = output+candidate+ ": "+str(round(candidate_votes.get(candidate)*100/total_votes, 3)) +" % ("+str(candidate_votes.get(candidate))+")"
    if winnerVotes < candidate_votes.get(candidate):
        winner = candidate
        winnerVotes = candidate_votes.get(candidate)



output = output+"\n"
output = output+"-------------------------------"
output = output+"\n"
output = output+" Winner : "+ winner

output = output+"\n"
output = output+"-------------------------------"

print(output)

with open('Resources/output.txt', 'w') as f:
    f.write(output)


      
