# python_challenge
 module3_challenge

In this challange we are analyzing 2 different problems,

# PyBank
In this problem, we are given a csv file(budget_data.csv) to analyze the dataset, and identify the profie/loss and change on monthly basis. 
The dataset is given per month revenue(Profit or loss), expected to calculate, 
- The total number of months included in the dataset
- The net total amount of "Profit/Losses" over the entire period
- The changes in "Profit/Losses" over the entire period, and then the average of those changes
- The greatest increase in profits (date and amount) over the entire period
- The greatest decrease in profits (date and amount) over the entire period

We wrote python program in main.py to solve this problem, 
we wrote to load and read the csv file row by row, and skip the header
the count of the month is number of rows. 
we are also calculating the change of profit/loss between months within the same loop
and storing the change in one variable

This helps in identifying greatest increase and greatest decrease between months.
also helps in identifying average change between months. 

Generated output in String, then printed it in terminal.
Also created a new output.txt file and saved it in analysis directory.

analysis looks like this,


Financial Analysis

------------------------------------------------------------

Total Months: 86

Total: $22564198

Average Change:-8311.11

Greatest Increase in Profits: Aug-16 ($1862002)

Greatest Decrease in Profits: Feb-14 ($-1825558)



# PyPoll
In this problem, we got the dataset of an election voting results in election_data.csv file
This dataset contains 3 columns, ballot id, county and candidate name. 
We are expected to analyze,
- The total number of votes cast
- A complete list of candidates who received votes
- The percentage of votes each candidate won
- The total number of votes each candidate won
- The winner of the election based on popular vote

To analyze the dataset and get desired results, we wrote a python program in main.py
We loaded the csv file, and read each row in it, skipping header row.
We counted number of rows in the voting records to get total votes casted. 
We stored the candidate name, and the vote they got in a dictionary. 
when we read a record in which the vote was for an already known candidate(found in dictionary), then we incremented the vote count in dictionary in value, otherwise added that candidate as new candidate in the dictionary as their first vote in value. 

Ater storing all values, we looped through all the keys of the dictionary, and got votes count of each candidate.
We calculated the % of votes each candidate for, and also found the highest voted candidate as winner of the election. 
We collected the output in a String variable, and then printed that in terminal
We also exported the output in a file in analysis/output.txt 

The analysis result looks like,


Election Results
------------------------------
Total Votes: 369711
-------------------------------
Charles Casper Stockham: 23.049 % (85213)
Diana DeGette: 73.812 % (272892)
Raymon Anthony Doane: 3.139 % (11606)
-------------------------------
 Winner : Diana DeGette
-------------------------------