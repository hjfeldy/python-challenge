import csv
import pandas as pd

#Import Data
file = open('employee_data.csv', 'r')
reader = csv.reader(file)

#Iterate past the header
next(reader)

#Reformate names
def splitName(name):
    lst = name.split(' ')
    return lst[0], lst[1]

#Reformat Dates 
def fixDate(date):
    year = date[:4]
    month = date[5:7]
    day = date[8:10]
    return f'{day}/{month}/{year}'

#Given
acroDict = us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
} 

#Easier to just build a new csv afresh since we are changing the number of columns
output = {'ID': [], 'First': [], 'Last': [], 'DOB': [], 'SSN': [], 'State': []}


for row in reader:
    #Use epic multi-value return statement
    firstName, lastName = splitName(row[1]) 
    output['First'].append(firstName)
    output['Last'].append(lastName)
    output['DOB'].append(fixDate(row[2]))
    output['State'].append(acroDict[row[4]])

    #Remember to append the stuff we aren't changing
    output['ID'].append(row[0])
    output['SSN'].append(row[3])

file.close()

#Create
df = pd.DataFrame(output)
#Save
df.to_csv('employee_data_FIXED.csv')