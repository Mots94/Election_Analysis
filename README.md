# Election Analysis for Candidates and Counties

![Podium](https://github.com/Mots94/Election_Analysis/blob/main/Resources/podiums.png)

## Using Python to analyze election results

## Introduction

After any election, a large amount of data has been collected that will ultimately determine the winner.  However, it would be extremely time consuming to hand count all of the votes for each candidate in the election.  If the election data is organized and stored in an electronic format, such as a .csv file, it can be "read" by a programming software like Python to pull out relevant data.  Additionally, a programmer can "write" the election data to a text file using Python. That file can contain the most salient details of the election, such as the winner by vote count and percentage of votes each candidate received.  That is exactly what has been done in this challenge in order to verify election results for three candidates across three state counties.  

## Audit Results

![TO](https://github.com/Mots94/Election_Analysis/blob/main/Resources/terminal_output.PNG)

* There were 369,711 votes cast in this election.  
In order to get this number, a total votes variable was initialized at zero using `total_votes = 0`.  Since each row represents a single vote, we could simply loop through all rows and add one vote to `total_votes` for each row.  However, this data file included headers, so to get an accurate count of votes the code `headers = next()` was used to skip the first row of header information.  Looping through all rows with a for loop, the code `total_votes += 1` was used to add 1 for each row in our data file.  This `total_votes` variable was used later on to display the number of total votes in a print() statement. 

* Jefferson county had 38,855 (10.51%) votes, Denver county had 306,055 (82.78%) votes, and Arapahoe county had 24,801 (6.71%) votes in this election.
This data was also gathered utilizing a for loop.  A county names list and county votes dictionary were created to associate each county with its voter turnout.  The list created to hold each county name was initialized using `all_counties = []`.  The dictionary was initialized using the code `county_votes = {}`.  The variable, `counties = row[1]`, was also created to reference the column where our county names were located.  Finally, a for loop and conditional statement were used to add data to the `all_counties` list, and associate that list with the `county_votes` dictionary to get the total number of votes for each county.
```
for row in file_reader:
    
    if counties not in all_counties:

        all_counties.append(counties)

        county_votes[counties] = 0

    county_votes[counties] += 1
```
The percentages of county votes out of total vote were retrieved using the following code:
```
 for counties in county_votes:

    var_county_votes = county_votes[counties]

    county_perc_vote = (float(var_county_votes)/float(total_votes)) * 100

    county_results = (f"{counties} county had a total of {var_county_votes:,} ({county_perc_vote:.2f}%) voters in this election.\n")

    print(county_results)

    txt_file.write(county_results)
```

* Denver county had the highest number of votes in this election at 306,055.  
Although this could clearly be seen from the output of the `county_votes` dictionary, code was written to retrieve the county with the highest vote count and print out that county name.  This was done using the follow code:
```
    if var_county_votes > highest_county:

        highest_county = var_county_votes

        turnout = (f"{counties} county had the highest turnout with {highest_county:,} votes of the total vote.\n")

    final_result = (
        f"------------------------\n"
        f"{turnout}") 

    print(final_result)

    txt_file.write(final_result)
```
This code was included in the for loop referenced in the previous bullet point.  The variable `highest_count` was initialized at zero, and the county with a number of votes greater than `highest_county` was assigned to the variable `highest_county`.  A variable named turnout was used to create an f-string statement with the name of the county that had the highest turnout, and their voting turnout number in the election.  This turnout variable was nested inside of another variable called `final_result`, which was used to correctly format the output of data in the .txt file.

* In this election, Charles Casper Stockham received 85,213 votes (23.0%), Diana DeGette received 272,892 votes (73.8%), and Raymon Anthony Doane received 11,606 votes (3.1%).  This information was gathered using code very similar to the county vote totals and percentages.  The only real difference for this data was using the variable `candidate_name = row[2]` to reference where the candidate names were at.  

* Finally, the winner of this election was Diana Degette with 272,892 votes, comprising 73.8% of the total vote.  A conditional statement was used inside of the `candidate_votes` for loop that looks like the following:
```
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
```
This code utilized a greater than conditional to assign the candidate with the highest number of votes and highest vote percentage to the variables `winning_count`, `winning_percentage`, and `winning_candidate`.  These variables were assigned to the `winning_candidate_summary` variable as f-strings, which was subsequently printed out and written to the results .txt file.

## Audit Summary
In its current state, this script could be used for any election data, even if there were other candidates or counties include in the data set.  However, if the data set had candidate names and county names in different columns this script would need slight modifications to work.  The only modifications that would need to be made would be to the variables `candidate_name = row[]` and `counties = row[]`.  Placing the correct index inside these variables will allow the script to access data that accurately represents what it is supposed to represent.  

---

Additionally, if our data set included data from cities within each county, the `all_counties` list could be modified to contain a list of cities within the counties.  This would likely require a nested if conditional be created inside of a for loop where two variables are used to reference the county data and city data (i.e. `counties = row[3]` and `cities = row[4]`).  As a result, a dictionary of dictionaries could be created that breaks down the city voting data in order to gain more insight into smaller community voting patterns.     
