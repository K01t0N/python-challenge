import os
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')

# opening the csv file
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    # making lists for each column
    month = []
    net_profit = []
    change = []

    for row in csvreader:

        # adding values to their respective lists
        month.append(row[0])
        net_profit.append(int(row[1]))

        # add the current net profit to the previous one
        if len(net_profit) > 1:
            change.append(int(row[1]) - int(previous_row[1]))
        previous_row = row

# find the greatest increase and its matching month
max_change = max(change)
max_change_index = change.index(max_change) + 1
max_change_month = month[max_change_index]

# find the greatest decrease and its matching month
min_change = min(change)
min_change_index = change.index(min_change) + 1
min_change_month = month[min_change_index]

print("Financial Analysis")
print()
print("--------------------------")
print()
print("Total Months: " + str(len(month)))
print()
print("Total: $" + str(sum(net_profit)))
print()
print("Average Change: $" + str(round(sum(change) / len(change), 2)))
print()
print("Greatest Increase in Profits: " + str(max_change_month) + " ($" + str(max_change) + ")")
print()
print("Greatest Decrease in Profits: " + str(min_change_month) + " ($" + str(min_change) + ")")

# printing the output to a text file
with open("analysis/analysis.txt", "a") as f:

    print("Financial Analysis", file=f)
    print(file=f)
    print("--------------------------", file=f)
    print(file=f)
    print("Total Months: " + str(len(month)), file=f)
    print(file=f)
    print("Total: $" + str(sum(net_profit)), file=f)
    print(file=f)
    print("Average Change: $" + str(round(sum(change) / len(change), 2)), file=f)
    print(file=f)
    print("Greatest Increase in Profits: " + str(max_change_month) + " ($" + str(max_change) + ")", file=f)
    print(file=f)
    print("Greatest Decrease in Profits: " + str(min_change_month) + " ($" + str(min_change) + ")", file=f)
