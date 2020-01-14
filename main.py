import os
import csv

# Path to collect data from the folder
csv_election_data = os.path.join ("Resources/election_data.csv")

#Path to output data
output_data = os.path.join ("Resources/output.txt")


total_votes = 0
total_candidates = []
unique_candidate = []
percentage_votes = []
winner = []
candidate_votes_count = []




#csv reader
with open (csv_election_data, newline = '') as csvfile:
    csv_reader = csv.reader (csvfile, delimiter = ',')
    next(csv_reader)
   
  
#Loop
    for row in csv_reader:
        total_votes = total_votes + 1
        total_candidates.append (row[2])
    for x in set(total_candidates):
        candidates_count = total_candidates.count(x)
        print(candidates_count)
        unique_candidate.append(x)
        candidate_votes_count.append(candidates_count)
        
        percentage_vote = (candidates_count/total_votes)*100
        percentage_votes.append(percentage_vote)
        winner = unique_candidate[candidate_votes_count.index(max(candidate_votes_count))]
        
#Print results
    print("Election results")
    print("..................")
    print(percentage_votes)
    print("Total votes:" + str(total_votes))
    print(f"Khan: {round(percentage_votes[0], 3)} % ({candidate_votes_count[0]})")
    print("Correy:" + " " + str(round(percentage_votes[1], 3)) + "%" +
            "("+str(candidate_votes_count[1])+")")
    print("Li:" + " " + str(round(percentage_votes[2], 3)) + "%" +
            "("+str(candidate_votes_count[2])+")")
    print("O'Tooley:" + " " + str(round(percentage_votes[3], 3)) + "%" +
            "("+str(candidate_votes_count[3])+")")
    print("winner:" + winner)
        
    #Output results
    with open (output_data, "w") as txt_file:
        txt_file.write("Election results" + "\n")
        txt_file.write(".............." + "\n")
        txt_file.write("Total votes:" + str(total_votes) + "\n")
        txt_file.write("Khan:" + " " + str(round(percentage_votes[0], 3)) + "%" +
                       "("+str(candidate_votes_count[0])+ ")\n")
        txt_file.write("Correy:" + " " + str(round(percentage_votes[1], 3)) + "%" +
                       "("+str(candidate_votes_count[1])+ ")\n")
        txt_file.write("Li:" + " " + str(round(percentage_votes[2], 3)) + "%" +
                       "("+str(candidate_votes_count[2])+ ")\n")
        txt_file.write("O'Tooley:" + " " + str(round(percentage_votes[3], 3)) + "%" +
                       "("+str(candidate_votes_count[3])+ ")\n")
        txt_file.write("winner:" + winner + "\n")
        
   
