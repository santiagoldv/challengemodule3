import os
import csv

electiondata_csv = os.path.join("resources", "election_data.csv")

totalvotes = 0
candidates =[]
candidate_votes = {}
winner = ("")
vote_count = 0

os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open(electiondata_csv) as election_file:
    csv_reader =  csv.reader(election_file, delimiter= ',')
    next(csv_reader, None)

    for each_line in csv_reader:
        totalvotes +=1
        candidate =  each_line[2]
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 0
    
        candidate_votes[candidate] +=1

print("Election Results")
print("")
print("Total votes:", totalvotes)
print("")

with open(electiondata_csv) as election_file:
    csv_reader =  csv.reader(election_file, delimiter= ',')
    next(csv_reader, None)

    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        percentaje = float(votes)/float(totalvotes)*100
        if votes > vote_count:
            vote_count = votes
            winner = candidate
            
        print(candidate, "|", "{:,.2%}".format(percentaje/100),"|", "{:,.0f}".format(votes))
print("")
print("Winner:", winner)

output_path = os.path.join("Analysis", "PyPoll")
with open(output_path, "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("\n")
    txtfile.write(f"Total votes: {totalvotes}\n")
    txtfile.write("\n")
    for candidate in candidate_votes:
            votes = candidate_votes.get(candidate)
            percentaje = float(votes)/float(totalvotes)*100
            if votes > vote_count:
                vote_count = votes
                winner = candidate                               
            votes = ("{:,.0f}".format(votes))
            percentaje = ("{:,.2%}".format(percentaje/100))
            txtfile.write(f"{candidate, percentaje, votes}\n")
    txtfile.write("\n")
    txtfile.write(f"Winner: {winner}\n")
