import os
import csv

electiondata_csv = os.path.join("resources", "election_data.csv")

totalvotes = 0
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]


os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open(electiondata_csv) as election_file:
    csv_reader =  csv.reader(election_file, delimiter= ',')
    next(csv_reader, None)

    for each_line in csv_reader:
        totalvotes +=1



        """ votes1 = each_line[2]
        if votes1 is candidates:
            votes1 = 
        
        "for each_row in csv_reader: """

print("Election Results")
print("")
print("Total votes:", totalvotes)
print("")
print("Charles Casper Stockham:", )
print("Diana DeGette:", )
print("Raymon Anthony Doane", )
print("")
print("Winner:", )

"""
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
"""
