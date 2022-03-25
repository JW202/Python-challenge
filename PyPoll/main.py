import os
import csv
from turtle import clear

election_csv = os.path.join("Resources", "election_data.csv")
 

Total_Votes=int(0)
Candidate = str(0)


This_Votes={ }

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
          Total_Votes+=1
          Candidate = row[2]  
          if Candidate in This_Votes:
            
            This_Votes[Candidate]+=1
            
          else:
             This_Votes[Candidate] =1


print ("Election Results")
print ("-----------------------")
print (f"Total Votes:  {Total_Votes}") 

print("------------------------")
for x in This_Votes:
  percentage="{:.3%}".format(This_Votes[x]/Total_Votes)
  print (x, percentage, '(', This_Votes[x], ')')
print("------------------------")
Winner = str()
Winner_count=int(0)


for x in This_Votes:
  if This_Votes[x]>Winner_count:
    Winner_count=This_Votes[x]
    Winner = x 

print("Winner: ", Winner)

print("------------------------")

                       
          

          


