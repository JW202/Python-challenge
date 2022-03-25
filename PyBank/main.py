import os
import csv

data_csv = os.path.join("Resources", "budget_data.csv")

Total_Months = int(0)
Total_Profits = 0
Average_Change = 0
Increase = float(0)
Decrease = float(0)
Greatest_Increase = str()
Greatest_Decrease = str()

Change =float(0)
Total_Change = float(0)

with open(data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for rows in csvreader:
       tm = rows[0]
       tp=rows[1]
      
       Total_Months+=1
       

       Total_Profits=Total_Profits+float(tp) 
       if Total_Months==1:
           Last_Month=float(tp)
       Change = float(tp)-Last_Month
       Total_Change=Total_Change+Change
       if Change>Increase: 
           Increase = Change
           Greatest_Increase = tm
       if Change < Decrease:
           Decrease = Change 
           Greatest_Decrease = tm
       Last_Month = float(tp)




print ('Financial Analysis')
print('-------------------------------------------------')
print(f"Total Months: {Total_Months}")
print (f"Total: ${round(Total_Profits,0)}")
print (f"Average Change: ${round(Total_Change/(Total_Months-1),2)}")
print (f"Greatest Increase in Profits: {Greatest_Increase} (${Increase})" )
print(f"Greatest Decrease in Profits: {Greatest_Decrease} (${Decrease}) ")




