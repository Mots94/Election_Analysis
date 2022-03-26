# Election Analysis for Candidates and Counties

![Podium](https://github.com/Mots94/Election_Analysis/blob/main/Resources/podiums.png)

## Using Python to analyze election results

## Introduction

After any election, a large amount of data has been collected that will ultimately determine the winner of the election.  However, it would be extremely time consuming to hand count all of the votes for each candidate in the election.  If the election data is organized and stored in an electronic format, such as a .csv file, it can be "read" by a programming software like Python to pull out relevant data.  Additionally, a programmer can "write" the election data to a text file using Python. That file can contain the most salient details of the election, such as the winner by vote count and percentage of votes each candidate received.  That is exactly what has been done in this challenge in order to verify election results for three candidates across three state counties.  

## Audit Results

* There were 369,711 votes cast in this election.  
In order to get this number, a total votes variable was initialized at zero using `total_votes = 0`.  Since each row represents a single vote, we could simply loop through all rows and add one vote to `total_votes` for each row.  However, this data file included headers, so to get an accurate count of votes the code `headers = next()` was used to skip the first row of header information.  Looping through all rows with a for loop, the code `total_votes += 1` was used to add 1 for each row in our data file.  This `total_votes` variable was used later on to display the number of total votes in a print() statement. 

* Jefferson county had 38,855 (10.51%) votes, Denver county had 306,055 (82.78%) votes, and Arapahoe county had 24,801 (6.71%) votes in this election.
This data was also gathered utilizing a for loop.  A county names list and county votes dictionary was created to associate each county with its voter turnout.  The list created to hold each county name was created using `all_counties = []`.  The dictionary was created using the code `county_votes = {}`.  The variable, `counties = row[1]`, was also created to refence the column where our county names were located.  Finally, a for loop and conditional statement were used to add data to the `all_counties` list, and associate that list with the `county_votes` dictionary to get the total number of votes for each county.
```
for row in file_reader:
    
    if counties not in all_counties:

        all_counties.append(counties)

        county_votes[counties] = 0

    county_votes[counties] += 1
```
The percentages of county votes out of total vote were retrieved using the follow code:
```
 for counties in county_votes:

    var_county_votes = county_votes[counties]

    county_perc_vote = (float(var_county_votes)/float(total_votes)) * 100

    county_results = (f"{counties} county had a total of {var_county_votes:,} ({county_perc_vote:.2f}%) voters in this election.\n")

    print(county_results)

    txt_file.write(county_results)
```

* Denver county had the highest number of votes in this election at 306,055.  
Although this could clearly be seen from the output of the `county_votes` list, code was written to retrieve the county with the highest vote count and print out that county name.  This was done using the follow code:
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
This code was included in the for loop referenced in the previous bullet point.  The variable `highest_count` was initialized at zero, and the county with a number of votes greater than `highest_county` was assigned to the variable `highest_county`.  A variable named turnout was used to create an f-string statement with the name of the county that had the highest turnout, as well as their voting turnout number in the election.  This turnout variable was nested inside of another variable called `final_result`, which was used to correctly format the output of data in the .txt file.
