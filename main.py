import os
import csv
# Path to collect data from the folder
csv_budget_data = os.path.join ("Resources/budget_data.csv")

#Path to output data
output_data = os.path.join ("Resources/output.txt")

total_months = []
total_net_revenue = []
revenue_change = []


#csv reader
with open (csv_budget_data, newline = '') as csvfile:
    csv_reader = csv.reader (csvfile, delimiter = ',')
    next(csv_reader, None)
  
#Loop
    for row in csv_reader:
        total_net_revenue.append(int(row[1]))
        total_months.append(row[0])
        
    for x in range (1, len(total_net_revenue)):
            revenue_change.append((int(total_net_revenue[x]) - 
                                       int(total_net_revenue[x-1])))
        #Revenue average
            revenue_average = sum(revenue_change) / len(revenue_change)
            totalMonths = len(total_months)
        #Greatest increase
            greatest_increase = max(revenue_change)
        #Greatest decrease
            greatest_decrease = min(revenue_change)             
        
        #Print results
            print("Financial Analysis")
            print("..................")
            print("Total Months:" + str(totalMonths))
            print("Total Revenue:" + "$" + str(sum(total_net_revenue)))
            print("Average change:" + "$" + str(revenue_average))
            print("Greatest Increase in Profits:" + 
                  str(total_months[revenue_change.index(max(revenue_change))+1]) + 
                  " " + "$" + str(greatest_increase))
            print("Greatest Decrease in Profits: " + 
                  str(total_months[revenue_change.index(min(revenue_change))+1]) + 
                  " " + "$" + str(greatest_decrease))
        #Output results
            with open (output_data, "w") as txt_file:
                txt_file.write("Financial Analysis" + "\n")
                txt_file.write(".............." + "\n")
                txt_file.write("Total Months:" + str(totalMonths) + "\n")
                txt_file.write("Total Revenue:" + "$" + str(sum(total_net_revenue)) + "\n")
                txt_file.write("Average change:" + "$" + str(revenue_average) + "\n")
                txt_file.write("Greatest Increase in Profits:" + 
                               str(total_months[revenue_change.index(max(revenue_change))+1]) + 
                               " " + "$" + str(greatest_increase) + "\n")
                txt_file.write("Greatest Decrease in Profits: " + 
                               str(total_months[revenue_change.index(min(revenue_change))+1]) + 
                               " " + "$" + str(greatest_decrease) + "\n") 
                