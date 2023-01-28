import os
import csv

Electionfile = os.path.join("PyPoll","Resources", "election_data.csv")

with open(Electionfile,'r') as election_data:
   reader = csv.reader(election_data,delimiter=',')
   c_header = next(reader)

   total_votes = 0
   candidate_options = []
   candidate_votes = {}
   winning_candidate = ""
   winning_count = 0
   winning_percentage = 0
   test_count=0

   for row in reader:
      total_votes+= 1
      
      candidate_name = row[2]
      
      if candidate_name not in candidate_options:
         candidate_options.append(candidate_name)
         candidate_votes[candidate_name]=0
      candidate_votes[candidate_name]= candidate_votes[candidate_name]+1

      #percentage= (candidate_votes[candidate_name]/total_votes)

      #if candidate_votes[candidate_name]>winning_count:
         #winning_count=candidate_votes[candidate_name]
         #winning_candidate=candidate_name

   #print(candidate_options)
   #print(candidate_votes)

print("Election Results")
print("\n---------------------------------------------------------------------")
print("\nTotal Votes:"+ str(total_votes))
print((candidate_votes))
#print("\nWinner: " + str(winning_candidate))

txtpath = os.path.join("PyPoll","Analysis","outputfile.txt")
with open(txtpath, "a") as f:
   f.write("Election Results")
   f.write("---------------------------------------------------------------------")
   f.write("Total Votes:"+ str(total_votes))
   f.write((str(candidate_votes)))
   #f.write("\nWinner: " + str(winning_candidate))

for candidate in candidate_votes:
   votes= candidate_votes.get(candidate)
   vote_percentage= float(votes)/float(total_votes)*100

   if(votes>winning_count):
      winning_count=votes
      winning_candidate=candidate

   output=f"{candidate}: {vote_percentage:.3f}%({votes})\n"
   print(output,end="")


winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
print(winning_candidate_summary)
