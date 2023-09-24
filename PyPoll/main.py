import os
import csv
total_votes = 0
# defining dictionaty
candidate_votes = {}
winner = ""
winnerVotes = 0
output = ""

# loading and reading election_data.csv
election_csv = os.path.join("Resources", "election_data.csv")
with open(election_csv, "r") as file:
    csvreader = csv.reader(file)
# skipped the header row
    next(csvreader,None)
    # looping on the csv rows
    for row in csvreader:
        # increamenting total_votes
        total_votes=total_votes+1
        # check if candidate is found in the dictionary
        if candidate_votes.get(row[2]):
            # if candidate name found, then incrementing vote by 1 if found in row. 
            candidate_votes[row[2]] = 1+int(candidate_votes.get(row[2]))
        else:
            # adding new candidate with 1 vote if not found in dictionary
            candidate_votes[row[2]] = 1

# creating outout in a variable    
output = output+"\n"
output = output+"Election Results"
output = output+"\n"
output = output+"------------------------------"
output = output+"\n"
output = output+"Total Votes: " +str(total_votes)
output = output+"\n"
output = output+"-------------------------------"

# looping through candidate names and candidates votes from candidate_votes dictionary, percent of 
for candidate in candidate_votes.keys():
    output = output+"\n"
    # getting candidates votes from dictionary
    per_candidate_total_votes = candidate_votes.get(candidate)
    # getting percent of total votes per candidate
    percent_of_total_votes = per_candidate_total_votes*100/total_votes
    # creating per candidate output
    output = output+candidate+ ": "+str(round(percent_of_total_votes, 3)) +" % ("+str(per_candidate_total_votes)+")"
    # checking to see if this candidate in winner
    if winnerVotes < candidate_votes.get(candidate):
        winner = candidate
        winnerVotes = candidate_votes.get(candidate)


# Adding winner in output
output = output+"\n"
output = output+"-------------------------------"
output = output+"\n"
output = output+" Winner : "+ winner

output = output+"\n"
output = output+"-------------------------------"

#printing output in terminal
print(output)

#writing output in analysis folder
with open('analysis/output.txt', 'w') as f:
    f.write(output)


      
