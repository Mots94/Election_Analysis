# Election Analysis for Candidates and Counties

![Podium](https://github.com/Mots94/Election_Analysis/blob/main/Resources/podiums.png)

## Using Python to analyze election results
---

## Introduction

After any election, a large amount of data has been collected that will ultimately determine the winner of the election.  However, it would be extremely time consuming to hand count all of the votes for each candidate in the election.  If the election data is organized and stored in an electronic format, such as a .csv file, it can be "read" by a programming software like Python to pull out relevant data.  Additionally, a programmer can "write" the election data to a text file using Python. That file can contain the most salient details of the election, such as the winner by vote count and percentage of votes each candidate received.  That is exactly what has been done in this challenge in order to verify election results for three candidates across three state counties.  

## Audit Results

* There were 369,711 votes cast in this election.  
In order to get this number, a total votes variable was initialized at zero using `total_votes = 0`.  Since each row represents a single vote, we could simply loop through all rows and add one vote to `total_votes` for each row.  However, this data file included headers, so to get an accurate count of votes the code `headers = next()` was used to skip the first row of header information.  Looping through all rows with a for loop, the code `total_votes += 1` was used to add 1 for each row in our data file.  This `total_votes` variable was used later on to display the number of total votes in a print() statement. 

* Jefferson county had 38,855 (10.51%) votes, Denver county had 306,055 (82.78%) votes, and Arapahoe county had 24,801 (6.71%) votes in this election.
This data was also gathered utilizing a for loop.  A county votes dictionary was created to associate each county with its voter turnout.  This was done using the code `county_votes = {}`


