import os
import csv
total_months = 0 
total_amount = 0
average_change = 0
greatest_increase = 0
greatest_increase_date = ''
greatest_decrease = 0
greatest_decrease_date = ''
previous_profit_loss = 0
row_change = 0


budget_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_csv, 'r') as file:
  csvreader = csv.reader(file)
  next(csvreader, None)
  for row in csvreader:
    total_months=total_months+1
    total_amount=total_amount+int(row[1])
    if previous_profit_loss==0:
      previous_profit_loss=int(row[1])
    else:
      row_change = int(row[1]) - previous_profit_loss
      average_change = average_change+row_change
      previous_profit_loss = int(row[1])

    if row_change >= greatest_increase:
        greatest_increase = row_change
        greatest_increase_date = row[0]

    if row_change<=greatest_decrease:
        greatest_decrease = row_change
        greatest_decrease_date = row[0]
    

average_change = average_change/(total_months-1)

print("\n")
print("Financial Analysis")
print("\n")
print("------------------------------------------------------------")
print("\n")
print("Total Months: " + str(total_months))
print("\n")
print("Total: $" +str(total_amount))
print("\n")
print("Average Change:"+str(average_change))
print("\n")
print("Greatest Increase in Profits: "+greatest_increase_date +" ($"+str(greatest_increase)+")")
print("\n")
print("Greatest Decrease in Profits: "+greatest_decrease_date +" ($"+str(greatest_decrease)+")")
print("\n")



