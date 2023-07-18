import os
import csv

budgetdata_csv = os.path.join("resources", "budget_data.csv")

cmonths = 0
nettotal = 0
profit_list = []
changes = []
prev_profit = None
change_total = 0
max_inc_value = -999999
min_inc_value = 999999
current_change = 0

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

            if current_change < min_inc_value:
                min_inc_month = current_month
                min_inc_value = current_change

        prev_profit = current_profit

print("Financial Analysis")
print("")
print("Total months:", cmonths)
print("Total:", "${:,.2f}".format(nettotal))
print("Average change:", "${:,.2f}".format(round(change_total / (cmonths-1), 2)))
print("Greatest Increase in Profits:", max_inc_month, "${:,.2f}".format(max_inc_value))
print("Greatest Decrease in Profits:", min_inc_month, "|", "${:,.2f}".format(min_inc_value))


output_path = os.path.join("Analysis", "PyBank")
with open(output_path, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("\n")
    txtfile.write(f"Total months: {cmonths}\n")
    txtfile.write(f"Total: {nettotal}\n")
    txtfile.write(f"Average Change in PL: ${change_total / (cmonths-1)}\n")
    txtfile.write(f"Greatest Increase in Profits: {max_inc_month} ( ${max_inc_value})\n")
    txtfile.write(f"Greatest Decrease in Profits: {min_inc_month} (${min_inc_value})\n")