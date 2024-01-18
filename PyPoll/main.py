import os
import csv
csvpath = os.path.join('Resources', 'election_data.csv')

# opening the csv file
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    voter_id = []
    county = []
    candidate = []

    # iterating through each row and storing values into seperate lists
    for row in csvreader:

        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

# get a list of all of the unique candidates
candidate_names = list(set(candidate))

# make a dictionary that will store the candidate's votes
candidate_dict = {}

# for every unique candidate
for name in candidate_names:

    # set a counter to zero
    name_count = 0

    # for every vote in the candidate list
    for x in candidate:

        # if the vote is cast for the selected candidate
        if x == name:

            # add one to the candidate's counter
            name_count += 1

    # store each candidate's votes into a dictionary entry
    candidate_dict[name] = name_count
    
# print results
print("Election Results")
print()
print("---------------------------")
print()

# total votes
print("Total Votes: " + str(len(voter_id)))
print()
print("---------------------------")
print()

# votes and percentages for every candidate
for name in candidate_dict:
    print(name + ": " + str(round(candidate_dict[name] / len(voter_id), 5) * 100) + "% " + str(candidate_dict[name]))
    print()

# find the candidate with the most votes from the candidate dictionary
print("---------------------------")
print()
print("Winner: " + str(max(candidate_dict, key=candidate_dict.get)))
print()
print("---------------------------")

# printing the output to a text file
with open("analysis/analysis.txt", "a") as f:

    print("Election Results", file=f)
    print(file=f)
    print("---------------------------", file=f)
    print(file=f)
    print("Total Votes: " + str(len(voter_id)), file=f)
    print(file=f)
    print("---------------------------", file=f)
    print(file=f)
    for name in candidate_dict:
        print(name + ": " + str(round(candidate_dict[name] / len(voter_id), 5) * 100) + "% " + str(candidate_dict[name]), file=f)
    print(file=f)
    print("---------------------------", file=f)
    print(file=f)
    print("Winner: " + str(max(candidate_dict, key=candidate_dict.get)), file=f)
    print(file=f)
    print("---------------------------", file=f)