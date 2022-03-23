#Data that needs to be retrived
#1. Total number of votes cast
#2. Complete list of candidates who received votes
#3. Percentage of votes each candidate won
#4. Total number of votes each candidate won
#5. Winner of election based on votes received

# #Creating path to .csv file
# file_to_load = "Resources\election_results.csv"

# #Create variable to open file path variable
# with open(file_to_load) as election_results:

#     #Analysis
#     print(election_results)

# import csv
# import os
# file_to_load = os.path.join("Resources", "election_results.csv")

# with open(file_to_load) as election_results:
#     print(election_results)

import os
file_to_save = os.path.join("Analysis", "election_analysis.txt")

open(file_to_save, "w")
