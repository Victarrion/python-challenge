



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


votecount_total=0
candidates=[]
candidates_votes=[]
data=[]
leader_count=0
leader_position=0

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
        
  
        
for x in range(len(data)):

    if (data[x][2] in candidates)==False:
               
                candidates.append(data[x][2]) #adds new candidate to the list in  the last position
                candidates_votes.append(0)  #adds a new total vote count to go along in the same position as candidate X. So positon x in either list match

    elif (data[x][2] in candidates)==True:
        for y in range(len(candidates)):
              #goes through each candidate and looks for its position
              if data[x][2]==candidates[y]: # when it finds the candidate add 1 vote to it
                candidates_votes[y]+=1 
    votecount_total+=1      #add 1 to total vote count
for x in range(len(candidates)):
    #looks for which candidate has the most votes
    if candidates_votes[x]>leader_count:
        leader_count=candidates_votes[x]
        leader_position=x               #saves its position in the list


print("Election Results")
print("----------------------------")
print("Total Votes: "+str(votecount_total))
print("----------------------------")
for x in range(len(candidates)):
    print("Votes Obtained by:" +str(candidates[x])+" -> "+str(round((candidates_votes[x]/votecount_total*100),2))+"%"+"("+str(candidates_votes[x])+")")
print("----------------------------")
print("Winner: "+candidates[leader_position])
print("----------------------------")