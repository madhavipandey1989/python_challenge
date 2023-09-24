import os
import csv

total_months = 0 
total_amount = 0
average_change = 0
total_change = 0
greatest_increase = 0
greatest_increase_date = ''
greatest_decrease = 0
greatest_decrease_date = ''
previous_profit_loss = 0
row_change = 0

# Loading and reading budget_data.csv

budget_csv = os.path.join("Resources", "budget_data.csv")
# opend with csv file
with open(budget_csv, 'r') as file:
  csvreader = csv.reader(file)
  #skipped the header row
  next(csvreader, None)
  #Looping with the cvs rows
  for row in csvreader:
    #Countig total months
    total_months=total_months+1
    #calculating the total amount
    total_amount=total_amount+int(row[1])
    # Storing profit/loss of previous row
    if previous_profit_loss==0:
      previous_profit_loss=int(row[1])
    else:
      # Calculating change from the previous months
      row_change = int(row[1]) - previous_profit_loss
      # Calculating total change  
      total_change = total_change+row_change
      previous_profit_loss = int(row[1])

    #Assigning greatest increase
    if row_change >= greatest_increase:
        greatest_increase = row_change
        greatest_increase_date = row[0]
    #Assigning greatest decrease
    if row_change<=greatest_decrease:
        greatest_decrease = row_change
        greatest_decrease_date = row[0]
    
#Calculating avarege change
average_change = total_change/(total_months-1)

#Storing output in string variable
output = ""

output= output+"\n"
output= output+"\n"
output= output+"Financial Analysis"
output= output+"\n"
output= output+"\n"
output= output+"------------------------------------------------------------"
output= output+"\n"
output= output+"\n"
output= output+"Total Months: " + str(total_months)
output= output+"\n"
output= output+"\n"
output= output+"Total: $" +str(total_amount)
output= output+"\n"
output= output+"\n"
output= output+"Average Change:"+str(round(average_change,2))
output= output+"\n"
output= output+"\n"
output= output+"Greatest Increase in Profits: "+greatest_increase_date +" ($"+str(greatest_increase)+")"
output= output+"\n"
output= output+"\n"
output= output+"Greatest Decrease in Profits: "+greatest_decrease_date +" ($"+str(greatest_decrease)+")"
output= output+"\n"
output= output+"\n"

#Printing output in terminal
print(output)

#exporting output in txt file
with open('analysis/output.txt', 'w') as f:
    f.write(output)
