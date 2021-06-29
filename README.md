## Overview of Election Audit: ##

The Colorado Board of Elections has presented a task for us to help with an audit of a recent election. He wanted us to use Python specifically to help with this audit, and also provided us with the file with all the untallied votes. In addition, we were tasked with not only finding out the winner of the election, but also finding the voter turnout of each county, the percentage of votes from each county out of the total turnout, and which county had the highest turn out.




## Election Audit Results: ##

- There were a total number of 369,711 votes cast during the election.
- The total number of votes and the percentage of votes for each county were as follows:
    Jefferson: 10.5% (38,855)
    Denver: 82.8% (306,055)
    Arapahoe: 6.7% (24,801)
- The county with the largest number of votes was Denver County.

![County Turnout](https://github.com/BrieonaT/election-analysis/blob/main/Resources/County_Turnout.png)

- The total number of votes and the percentage of votes for each candidate were as follows:
    Charles Casper Stockham: 23.0% (85,213)
    Diana DeGette: 73.8% (272,892)
    Raymon Anthony Doane: 3.1% (11,606)
- The candidate who won the election was Diana DeGette, who had 272,892 total votes, 73.8% of all votes.

![Winning Candidate](https://github.com/BrieonaT/election-analysis/blob/main/Resources/Winning_Canidate.png)

## Election-Audit Summary: ##
In addition, this script can be modified to be used in similar situations, such as future elections. A way you could modify the script for further use comes with the fact you could easily swap out current candidates for future ones, along with other information that was provided, such as total votes and which counties the votes were from. You can simply take the skeleton of the current code and use it for another data set of a similar set up with little changes. You could also expand upon the data you're extracting if you were using a data set with additional information, such as getting percentages of voter's genders, age ranges, ethnicities, affiliated political parties, etcetera. It would be easy to take the pre-existing code and add those factors by adding in more code that's similar to what's already been provided.
