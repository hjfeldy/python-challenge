import csv
import os

#Import Data 
file = open('Resources/budget_data.csv', 'r')
reader = csv.reader(file)

#Get from headers to the first row
next(reader) 

#Variable Setup
months = 0
plTotal = 0 
plBest = 0       
plBestMonth = '' 
plBestBefore = ''   
plWorst = 0
plWorstMonth = ''
plWorstBefore = ''
avgChange = []
beforeVars = next(reader) #Grab first row to compare against for the change variable
before = int(beforeVars[1])
beforeMonth = beforeVars[0]


#Iterate
for row in reader:
    #Accumulate
    months += 1
    plTotal += int(row[1])

    #Take not of change (month on month)
    change = int(row[1]) - before #Track month-on-month change every iteration
    avgChange.append(change)
       
    if change > plBest:
        plBest = change
        plBestMonth = row[0]
        plBestBefore = beforeMonth
    if change < plWorst:
        plWorst = change
        plWorstMonth = row[0]
        plWorstBefore = beforeMonth
    
    #reset value of before
    before = int(row[1])
    beforeMonth = row[0]

file.close()
#Reading Done. Write Summary to analysis folder

file = open('analysis/Summary.txt', 'w')

file.write(f"Total Months: {months}\n" )
file.write(f"Total: {plTotal}\n" )
file.write(f"Average Change: ${round(sum(avgChange) / len(avgChange), 2)}\n" )
file.write(f"Greatest Increase in Profits: ${plBest} between {plBestBefore} and {plBestMonth}\n" )
file.write(f"Greatest Decrease in Profits: ${plWorst} between {plWorstBefore} and {plWorstMonth}\n" )

file.close()