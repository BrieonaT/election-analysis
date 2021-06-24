counties = ["Arapahoe","Denver","Jefferson"]
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")
for county in counties:
    print(county)
for county in counties_dict:
    print(county)
for county in counties_dict.keys():
    print(county)

    ### Gets Values for Keys
for county in counties_dict:
    print(counties_dict[county])
for county in counties_dict:
    print(counties_dict.get(county))

    ##Getting Key/Value pairs
for county, voters in counties_dict.items():
    print(county, voters)

for county, voters in counties_dict.items():
    print(str(county) + " county has " + str(voters) + " registered voters")


######Dictionary
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)


### prints counties in voting data dictionary
for county in range(len(voting_data)):

      print(voting_data[county]['county'])


### values from dictionary
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict['county'])


#f string
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

### f-string version of previous skill drill
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")



candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)


### above statement but its with percentage point
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")