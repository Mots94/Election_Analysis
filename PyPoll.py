import csv
from itertools import count
import os


#Variable assigned to load file from path
file_to_load = os.path.join("Resources", "election_results.csv")

#Variable assigned to save file to path
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Initialize vote count variable
total_votes = 0

# Create list of candidates/list of counties
candidate_options = []

# Create county list
all_counties = []

# Create dictionary for candidate names and # of votes/number of county votes
candidate_votes = {}

# Create dictionary for counties and number of votes per county
county_votes = {}

# Variables created for f-string output
winning_candidate = ""
winning_count = 0
winning_percentage = 0
highest_county = 0


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

        # Counties variable with second column index
        counties = row[1]
        
        # Add candidate_name data to canidate_options list, use if statment 
        # so the name of each candidate appears only once in candidate_options list
        if candidate_name not in candidate_options: 
            
            # Add candidate name to candidate options list
            candidate_options.append(candidate_name)
        
    
           #Tracking candidate vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to the candidate's name 
        candidate_votes[candidate_name] += 1

        if counties not in all_counties:

            all_counties.append(counties)

            county_votes[counties] = 0

        county_votes[counties] += 1

      
with open(file_to_save, "w") as txt_file:

    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    txt_file.write(election_results)

    for candidate_name in candidate_votes:

        votes = candidate_votes[candidate_name]

        vote_percentage = (float(votes)/float(total_votes)) * 100

        # Print out each candidate's name, vote count, and percentage of votes
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        print(candidate_results)

        txt_file.write(candidate_results)

        if (votes > winning_count) and (vote_percentage > winning_percentage):

            winning_count = votes

            winning_percentage = vote_percentage

            winning_candidate = candidate_name

        winning_candidate_summary = (
            f"------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"------------------------\n")

    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)

    # Create header for county results

    county_header = (
        f"County Results\n"
        f"------------------------\n")

    print(county_header)

    txt_file.write(county_header)

    for counties in county_votes:

        var_county_votes = county_votes[counties]

        county_perc_vote = (float(var_county_votes)/float(total_votes)) * 100

        county_results = (f"{counties} county had a total of {var_county_votes:,} ({county_perc_vote:.2f}%) voters in this election.\n")

        print(county_results)

        txt_file.write(county_results)

        if var_county_votes > highest_county:

            highest_county = var_county_votes

            turnout = (f"{counties} county had the highest turnout with {highest_county:,} votes of the total vote.\n")

    final_result = (
        f"------------------------\n"
        f"{turnout}")
    
    print(final_result)

    txt_file.write(final_result)

    
    ##1. Voter turnout for each county

        #1a. Create list and loop through data to add counties

        #1b. Add up number of rows (votes) for each county

    ##2. Percentage of votes from each county out of the total count

        #2a. Use county_votes dictionary to divide county votes by total count  

    ##3. County with the highest turnout

        #3a. Base this on number of county_votes