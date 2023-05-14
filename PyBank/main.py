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


csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
# '..'= in current folder, in the resources folder, look for budget_data.scv
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
   csvreader = csv.reader(csvfile, delimiter=',')

   print(csvreader)

    # Read the header row first (skip this step if there is no header)
 #   csv_header = next(csvreader)
 #   print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
 #   for row in csvreader:
#        print(row)


month_counter=0
net_income=0
average_income=0
greatest_month=0
worst_month=0

