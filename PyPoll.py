import csv
import os


#Variable assigned to load file from path
file_to_load = os.path.join("Resources", "election_results.csv")

#Variable assigned to save file to path
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Initialize vote count variable
total_votes = 0

# Create list of candidates
candidate_options1 = []

# Creat dictionary for candidate names and # of votes
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open election_results.csv and read file
with open(file_to_load) as election_data:

    #Read and analyze data
    file_reader = csv.reader(election_data)

    #Read the header row
    headers = next(file_reader)

    #Print each row in CSV file
    for row in file_reader:

        #Adding up each row to count total votes
        total_votes += 1

        #Create candidate name variable to add to candidate_options list
        candidate_name = row[2]
        
        # Add candidate_name data to canidate_options list, use if statment 
        # so the name of each candidate appears only once in candidate_options list
        if candidate_name not in candidate_options1: 
            
            # Add candidate name to candidate options list
            candidate_options1.append(candidate_name)
        
    
           #Tracking candidate vote count
            candidate_votes[candidate_name] = 0

        # # Add a vote to the candidate's name 
        candidate_votes[candidate_name] += 1
  

# with open(file_to_save), "w") as txt.file:

    # election_results = (
    #     f"\nElection Results\n"
    #     f"-------------------------\n"
    #     f"Total Votes: {total_votes:,}\n"
    #     f"-------------------------\n")
    # print(election_results, end="")

    # text_file.write(election_results)

    for candidate_name in candidate_votes:

        votes = candidate_votes[candidate_name]

        vote_percentage = (float(votes)/float(total_votes)) * 100

        # Print out each candidate's name, vote count, and percentage of votes
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        if (votes > winning_count) and (vote_percentage > winning_percentage):

            winning_count = votes

            winning_percentage = vote_percentage

            winning_candidate = candidate_name

        winning_candidate_summary = (
            f"------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}\n"
            f"------------------------\n")

    print(winning_candidate_summary)