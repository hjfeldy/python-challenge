import csv

#Variables to accumulate
voteTotal = 0
voteDict = {} 
#Keys = Candidate, Values = Candidate-specific Vote Totals

#Import Data
file = open('Resources/election_data.csv')
reader = csv.reader(file)

#Iterate past the header
next(reader)

#Iterate and Accumulate
for row in reader:
    candidate = row[2]
    voteTotal += 1
    if candidate not in voteDict.keys():
        voteDict[candidate] = 1
    else:
        voteDict[candidate] += 1
file.close()
#Done Accumulating - Now Summarize and write to analysis file

file = open('analysis/Summary.txt', 'w')

file.write('Election Results\n')
file.write('-------------------------\n')
file.write(f'Total Votes: {voteTotal}\n')
file.write('-------------------------\n')
winner = list(voteDict.keys())[0]
for key in voteDict.keys():
    pct = round((voteDict[key] / voteTotal) * 100, 3)
    amt = voteDict[key]
    if amt > voteDict[winner]:
        winner = key
    file.write(f"{key}: {pct}% ({amt})\n")
file.write(f'-------------------------\nWinner: {winner}\n-------------------------')
    

file.close()