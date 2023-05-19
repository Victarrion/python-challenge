# This will be the main script to run for each analysis.

# resources contains csv files i will use.

# analysis contains a text file that has the results:
# CSV format
#Date,Profit/Losses
#Jan-10,1088983

#Find:
# The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period
#In addition, your final script should both print the analysis to the terminal and export a text file with the results.

#Code:

#import needed libraries
import os
import csv
import pathlib
from pathlib import Path

#pathlib.Path().resolve()

#dir_path = os.path.dirname(os.path.realpath(__file__))
#print("full directory: "+dir_path)

os.chdir(os.path.dirname(os.path.realpath(__file__)))


#cwd = os.getcwd()


#print("cwd is: "+cwd)
net_income=0
greatest_month=0
worst_month=0
month_counter=0
total_change=0
full_data=[]
save_worst=["",""]
save_best=["",""]


csvpath = os.path.join('.', 'Resources', 'budget_data.csv')
# '.'= in current folder, in the resources folder, look for budget_data.scv
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
   csvreader = csv.reader(csvfile, delimiter=',')

   # print(csvreader) #points to memory storage

    # Read the header row first (skip this step if there is no header)
   csv_header = next(csvreader)
   #print(f"CSV Header: {csv_header}") #prints header

    # Read each row of data after the header
   for row in csvreader:
         
         month_counter +=1
         date_extend=row[0].split("-")
         date_extend.extend(row)
         date_extend[2]=float(date_extend[3])
         full_data.append(date_extend)




for x in range(len(full_data)-1):
   
   change=int(full_data[x+1][3])-int(full_data[x][3])

   if int(change)>0 and greatest_month<int(change):
      greatest_month=int(change)
      save_best[0]=full_data[x+1][0]
      save_best[1]=full_data[x+1][1]
      
   elif int(change)<0 and worst_month>int(change):    

      worst_month=int(change)
      save_worst[0]=full_data[x+1][0]
      save_worst[1]=full_data[x+1][1]
      
   total_change=total_change+change
   net_income=net_income+int(full_data[x][3])



print("Financial Analysis")
print("----------------------------")
print("total months: "+str(month_counter))
print("Total: "+str(net_income))
print("average: "+str(round((total_change/(month_counter-1)),2)) )        #compensating counting method
print("Greatest Decrease in Profits: "+save_worst[1]+" "+save_worst[0]+" $"+str(worst_month))
print("Greatest Increase in Profits: "+save_best[1]+" "+save_best[0]+" $"+str(greatest_month))
