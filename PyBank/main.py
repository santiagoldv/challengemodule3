import os
import csv

budgetdata_csv = os.path.join("resources", "budget_data.csv")

cmonths = 0
nettotal = 0
profit_list = []
changes = []
prev_profit = None
change_total = 0
max_inc_value = -9999


os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open(budgetdata_csv ) as budget_file:
    csv_reader =  csv.reader(budget_file, delimiter= ',')
    next(csv_reader, None)
    
    for each_line in csv_reader:
        cmonths += 1
        current_month = each_line[0]
        current_profit = int(each_line[1])
        nettotal += current_profit
        profit_list += [current_profit]
        
        if prev_profit is not None:
            current_change = current_profit - prev_profit        
            change_total += current_change
          
            if current_change > max_inc_value:
                max_inc_month = current_month               
                max_inc_value = current_change
                



print("Financial Analysis")
print("Total months:", cmonths)
print("Total:", nettotal)
print("Average change:", )
print("Greatest Increase in Profits:", max_inc_month, max_inc_value)
print("Greatest Decrease in Profits:")

'''
output = (         
    "Financial Analysis\n"
    "\n"       
    f"Total months: {cmonths}\n"
    f"Total: {nettotal}\n"
    #f"Average change: {}\n"
    #f"Greatest Increase in Profits: {current_month} {current_change}\n"
    )
'''
#("Average change: ", "${:,.2f}".format(round(change_total / (cmonths-1), 2)))
#p(f"Greatest Increase in Profits: {max_inc_month} {max_inc_value}")
#print("Greatest Decrease in Profits:") """

#print(output)

#with open(OUTPUT_PATH, "w") as outfile:
    #   outfile.write(output) """
