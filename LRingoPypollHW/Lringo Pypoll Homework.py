#import dependencies
import os
import csv

#Read csv file
datafile = open("election_data.csv")
reader = csv.DictReader(datafile)

voter_id = []
candidate = []
county = []

for row in reader:
    voter_id.append(row['Voter ID'])
    candidate.append(row['Candidate'])
    county.append(row['County'])

#Total Number of Votes
print(len(candidate))

#Make a list of Candidates
unique_list = []
#The percentage of votes each candidate won
candidate_votes = []
#The total number of votes each candidate won
total_votes = []

for x in candidate:
    if x not in unique_list:
        unique_list.append(x)
        total_votes.append(candidate.count(x))
        candidate_votes.append('{:.3f}%'.format((candidate.count(x)/len(candidate))*100))
print(unique_list)
print(candidate_votes)
print(total_votes)
print(unique_list[total_votes.index(max(total_votes))])    

#write text file
election = open("electiondata.txt","w+")
election.write('Election Results\n')
election.write('-------------------------\n')
election.write('Total Votes: %d\n' % (len(candidate)))
election.write('-------------------------\n')
for i in range(len(unique_list)):
    election.write('%s: ' % (unique_list[i]))
    election.write('%s ' % (candidate_votes[i]))
    election.write('(%d)\n' % (total_votes[i]))
election.write('-------------------------\n')
election.write('Winner: %s\n' % (unique_list[total_votes.index(max(total_votes))]))
election.write('-------------------------\n')
election.write('```')
election.close()