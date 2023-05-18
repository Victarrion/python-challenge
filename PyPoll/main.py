



    # The total number of votes cast

    # A complete list of candidates who received votes

    # The percentage of votes each candidate won

    # The total number of votes each candidate won

    # The winner of the election based on popular vote





#import needed libraries
import os
import csv
import pathlib
from pathlib import Path


votecount=0
candidates=[]
data=[]
os.chdir(os.path.dirname(os.path.realpath(__file__)))
csvpath = os.path.join('.', 'Resources', 'election_data.csv')


#csv:
# Ballot ID,County,Candidate

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

   # print(csvreader) #points to memory storage
    
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)


    for row in csvreader:
        data.append(row)
        
print(data)      
        
for x in range(len(data)):
    print(data[x][2]) 
    if (data[x][2] in candidates)==False:
                print(data[x][2])
                candidates.append(data[x][2]) #adds new candidate to the row
                candicate_counter=+1
        
  
