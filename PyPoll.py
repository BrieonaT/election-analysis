#1.Open the data file.

import csv
import os

    # Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
    # Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
    print(election_data)


# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

     # Write three counties to the file.
     txt_file.write("Counties in the Election")
     txt_file.write("\n--------")
     txt_file.write("\nArapahoe\nDenver\nJefferson")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)


#2.Write down the names of all the candidates.
#3.Add a vote count for each candidate.
#4.Get the total votes for each candidate.
#5.Get the total votes cast for the election.
